""" The common module provides a suite of function that are used throughout the Core Automation framework.

These functions assist wtih generating and using model instances as well as environment variables and
other very commont tasks.

"""

import warnings
from typing import Any, IO
import tempfile
import json
import datetime
from decimal import Decimal
import os
import re
import io
import boto3
from botocore.exceptions import ProfileNotFound

from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import DoubleQuotedScalarString

from .constants import (
    # Environment Variables
    ENV_AUTOMATION_ACCOUNT,
    ENV_API_LAMBDA_NAME,
    ENV_API_LAMBDA_ARN,
    ENV_COMPONENT_COMPILER_LAMBDA_ARN,
    ENV_DEPLOYSPEC_COMPILER_LAMBDA_ARN,
    ENV_RUNNER_STEP_FUNCTION_ARN,
    ENV_START_RUNNER_LAMBDA_ARN,
    ENV_EXECUTE_LAMBDA_ARN,
    ENV_INVOKER_LAMBDA_ARN,
    ENV_INVOKER_LAMBDA_NAME,
    ENV_INVOKER_LAMBDA_REGION,
    ENV_ENFORCE_VALIDATION,
    ENV_LOCAL_MODE,
    ENV_AWS_PROFILE,
    ENV_AWS_REGION,
    ENV_CLIENT,
    ENV_CLIENT_NAME,
    ENV_CLIENT_REGION,
    ENV_DYNAMODB_REGION,
    ENV_DYNAMODB_HOST,
    ENV_BUCKET_NAME,
    ENV_BUCKET_REGION,
    ENV_ARTEFACT_BUCKET_NAME,
    ENV_MASTER_REGION,
    ENV_ENVIRONMENT,
    ENV_SCOPE,
    ENV_VOLUME,
    ENV_DELIVERED_BY,
    ENV_LOG_DIR,
    ENV_USE_S3,
    # Data Values
    V_CORE_AUTOMATION,
    V_DEFAULT_REGION,
    V_DEFAULT_BRANCH,
    V_DEFAULT_REGION_ALIAS,
    V_DEPLOYSPEC_FILE_YAML,
    V_DEPLOYSPEC_FILE_JSON,
    V_FALSE,
    V_TRUE,
    V_LOCAL,
    V_SERVICE,
    V_EMPTY,
    # Dpeloyment Scopes (NOT Automation SCOPE.  That's different!  ENV_SCOPE is a "prefix" to all automation objects)
    SCOPE_PORTFOLIO,
    SCOPE_APP,
    SCOPE_BRANCH,
    SCOPE_BUILD,
    SCOPE_COMPONENT,
    CORE_AUTOMATION_PIPELINE_PROVISIONING_ROLE,
)


def generate_branch_short_name(branch: str | None) -> str | None:
    """
    Generates a shortened version of the branch name.

    FIRST: the entire thing is converted to lowercase.
    THEN Anything that is not a-z or 0-9 is replaced with a dash.
    THEN only the 1st 20 characters of the branch name are used.
    Trailing hyphens are removed.

    Args:
        branch: The branch name to shorten

    Returns:
        str: The shortened branch name
    """
    if branch is None:
        return None

    return re.sub(r"[^a-z0-9-]", "-", branch.lower())[0:20].rstrip("-")


def split_prn(
    prn: str,
) -> tuple[str | None, str | None, str | None, str | None, str | None]:
    """
    Splits the prn and returns the parts relevant to the deployment details.

    The PRN is in the format: prn:portfolio:app:branch:build:component

    If you have too many colons, at most it will return the first 5 parts after prn:

    Args:
        prn (str): The PRN to split (ex: prn:portfolio:app:branch:build)

    Returns:
        tuple[str, str | None, str | None, str | None, str | None, str | None]: portfolio, app, branch, build, component

    """
    parts = prn.split(":")

    if len(parts) == 1:
        return None, None, None, None, None
    if len(parts) < 3:
        return parts[1], None, None, None, None
    if len(parts) < 4:
        return parts[1], parts[2], None, None, None
    if len(parts) < 5:
        return parts[1], parts[2], parts[3], None, None
    if len(parts) < 6:
        return parts[1], parts[2], parts[3], parts[4], None

    return parts[1], parts[2], parts[3], parts[4], parts[5]


def split_portfolio(
    portfolio: str | None,
) -> tuple[str | None, str | None, str | None, str]:
    """
    Split the portfolio into it component parts.  Company, Group, Owner, Application
    The portfolio must have at least 2 parts separated by a hyphen('-').

    For:
       owner-bizapp -> returns Owner and BizApp parts. Company and Group is None
       group-owner-bizapp -> returns Group and Owner and BizApp parts. Company is None
       company-group-owner-bizapp -> returns Company, Group, Owner and BizApp parts

    Deprecated: I don't wnt to do this anymore.  Was a bad idea.

    Args:
        portfolio (str): Name of the portfolio to parse
    Return:
        tuple: Company, Group, Owner, Application
    """
    warnings.warn(
        "The split_portfolio function is deprecated and will be removed in a future version.",
        DeprecationWarning,
        stacklevel=2,
    )

    if not portfolio:
        raise IOError("Portfolio name must be specified.")

    parts = portfolio.split("-")
    if len(parts) == 1:
        return None, None, None, parts[0]
    if len(parts) == 2:
        return None, None, parts[0], parts[1]
    if len(parts) == 3:
        return None, parts[0], parts[1], parts[2]
    if len(parts) == 4:
        return parts[0], parts[1], parts[2], parts[3]

    raise IOError('Portfolio should have 1 to 4 segments separated by a dash "-"')


def split_branch(
    branch: str, default_region_alias: str | None = None
) -> tuple[str, str | None]:
    """
    Splits the branch into the environment and data_center parts.  If the data center is not specified,
    the DEFAULT_DATA_CENTER is used.  Currently, this is the value "sin" to identify the Singapore data center.

    Args:
        branch: The branch name to split
        default_region_alias: The default region alias to use if the data center (region) is not specified.

    Returns:
        tuple: The environment and data center parts

    """
    parts = branch.split("-")
    if len(parts) < 2:
        return (branch, default_region_alias or V_DEFAULT_REGION_ALIAS)
    return (parts[0], default_region_alias) if len(parts) < 2 else (parts[0], parts[1])


def load_deployspec(app_dir: str | None = None) -> Any:
    """
    Load the Deployspec with YAML/JSON validation from the current directory.

    Filenames are:
        * deployspec.yaml
        * deployspec.json

    Return:
        Any: return Any so I don't get a type error on Pydantic DeplySpec Model parser
    """
    try:

        if not app_dir:
            app_dir = os.getcwd()  # We assume we are running in the project folder

        data: dict | list | None = None

        fn = os.path.join(app_dir, V_DEPLOYSPEC_FILE_YAML)
        if os.path.exists(fn):
            with open(fn, "r") as f:
                data = YAML(typ="safe").load(f)
        else:
            fn = os.path.join(app_dir, V_DEPLOYSPEC_FILE_JSON)
            if os.path.exists(fn):
                with open(fn, "r") as f:
                    data = json.load(f)

        if isinstance(data, dict):
            return [data]

        if isinstance(data, list):
            return data

        return None

    except Exception:
        return None


def get_prn(
    portfolio: str,
    app: str | None = None,
    branch: str | None = None,
    build: str | None = None,
    component: str | None = None,
    scope: str = SCOPE_BUILD,
    delim: str = ":",
) -> str:
    """
    Generates a PRN with a delimter between the parts as specified in the 'delim' parameter.

    The "Scope" argument is used to determine how many parts of the PRN are included in the result.

    Args:
        portfolio (str): Business application (portfolio) name.
        app (str | None, optional): Deployment part of the Business application (app). Defaults to None.
        branch (str | None, optional): Branch of the source-code repository. Defaults to None.
        build (str | None, optional): Build Number or Commit ID of the deployment. Defaults to None.
        component (str | None, optional): Component Part of the deployment. Defaults to None.
        scope (str, optional): Socpe of the PRN. Defaults to SCOPE_BUILD.
        delim (_type_, optional): _description_. Defaults to ":".

    Returns:
        str: The Pipeline Reference Number (PRN)
    """
    result = portfolio
    if scope == SCOPE_PORTFOLIO:
        return result
    if app:
        result = f"{result}{delim}{app}"
        if scope == SCOPE_APP:
            return result
    if branch:
        result = f"{result}{delim}{branch}"
        if scope == SCOPE_BRANCH:
            return result
    if build:
        result = f"{result}{delim}{build}"
        if scope == SCOPE_BUILD:
            return result
    if component:
        result = f"{result}{delim}{component}"
        if scope == SCOPE_COMPONENT:
            return result
    return result


def generate_bucket_name(
    client: str = "", branch: str = V_DEFAULT_BRANCH, scope_prefix: str = ""
) -> str:
    """
    Get the configuration bucket name from the environment variables

    Args:
        client: The client name
        branch: The branch name
        scope_prefix: The scope prefix

    Returns:
        str: The bucket name
    """

    return f"{scope_prefix}{client}-{V_CORE_AUTOMATION}-{branch}".lower().strip("-")


def get_bucket_name(client: str | None = None) -> str:
    """
    Return the bucket name specified in the environment variabe BUCKET_NAME.  If not specified, generate a bucket name
    based on the client name, branch name and automation scope prefix.

    Returns:
        str: The bucket name for the core automation objects
    """

    client = client or get_client() or ""
    automation_scope_prefix = get_automation_scope() or ""

    return os.environ.get(
        ENV_BUCKET_NAME,
        generate_bucket_name(client, V_DEFAULT_BRANCH, automation_scope_prefix),
    )


def get_artefact_bucket_name(client: str | None = None) -> str:
    """
    Return the bucket nmame for the artefacts.  This is specified in the environment variable ARTEFACT_BUCKET_NAME.
    If not specified, the bucket name is the same as the core automation bucket name.

    Returns:
        str: The bucket name for the artefacts
    """
    return os.environ.get(ENV_ARTEFACT_BUCKET_NAME, get_bucket_name(client))


def get_artefact_bucket_region() -> str:
    """
    Return the region of the artefact bucket.  This is specified in the environment variable ARTEFACT_BUCKET_REGION.
    If not specified, the region is the same as the core automation bucket region.

    Returns:
        str: Region of the artefact bucket
    """
    return os.environ.get(ENV_BUCKET_REGION, get_bucket_region())


def get_prn_alt(
    portfolio,
    app: str | None = None,
    branch: str | None = None,
    build: str | None = None,
    component: str | None = None,
    scope: str = SCOPE_BUILD,
) -> str:
    """
    Helper functon to generate a PRN with a hyphen delimiter.

    Returns a result like: prn-portfolio-app-branch-build-component

    Args:
        portfolio (_type_): Portfolio Business Application Name
        app (str | None, optional): Deployment component of the Business Application Portfolio. Defaults to None.
        branch (str | None, optional): Repository Branch for the source code. Defaults to None.
        build (str | None, optional): Branch build reference or Commit ID. Defaults to None.
        component (str | None, optional): Infrastructure Component part. Defaults to None.
        scope (str, optional): Scope of the Pipeline Reference Number. Defaults to SCOPE_BUILD.

    Returns:
        str: The Pipeline Reference Number (PRN)
    """
    return get_prn(portfolio, app, branch, build, component, scope, delim="-")


def get_automation_scope() -> str | None:
    """
    The automation scope is a prefix on all automation objects.  This is typically an empty string or None.

    This is NOT the same thing as the deployment scope.  The deployment scope is a part of the PRN.

    This is the "Automation Scope"  Typically ued to differentiate mutiple core automation engines in the same AWS account.

    Returns:
        str | None: The prefix for all automation objects
    """
    return os.getenv(ENV_SCOPE, None)


def get_provisioning_role_arn(account: str) -> str:
    """
    Get the provisioning role ARN for the specified account.  This is specified in the environment variable ENV_AUTOMATION_ACCOUNT.
    If not specified, the default value is used based on the region and account number.

    Args:
        account (str): The AWS account number

    Returns:
        str: The ARN for the provisioning
    """

    scope_prefix = get_automation_scope()

    return "arn:aws:iam::{}:role/{}{}".format(
        account, scope_prefix, CORE_AUTOMATION_PIPELINE_PROVISIONING_ROLE
    )


def is_use_s3() -> bool:
    """
    Check if the deployment is using S3 for storage.  This is specified in the environment variable LOCAL_MODE.
    If not specified, the default value is used based on the region and account number.

    Returns:
        bool: True if the deployment is using S3 for storage
    """
    return os.getenv(ENV_USE_S3, str(not is_local_mode())).lower() == V_TRUE


def is_local_mode() -> bool:
    """
    You may set the mode to local in the PACKAGE_DETAILS object or the ENV_LOCAL_MODE environment variable.

    Args:
        package_details (dict | None, optional): PACKAGE_DETAILS object. Defaults to None.

    Returns:
        bool: True of the mode is local
    """
    return os.getenv(ENV_LOCAL_MODE, V_FALSE).lower() == V_TRUE


def get_storage_volume(region: str | None = None) -> str:
    """
    If you enable the envoronment variable LOCAL_MODE=true, you can specify a local storage volume for the core automation
    objects.  This is specified in the environment variable VOLUME.  If not specified, the current working directory
    is used.

    When using docker, this is your volume mount point.

        export LOCAL_MODE=true
        export VOLUME=/mnt/data/core

    Then the engine will use /mnt/data/core/artefacts/**, /mnt/data/core/packages/**, /mnt/data/core/files/** as
    the storage locations.

    setting LOCAL_MODE=false will store artefacts on S3.

    And, thus the storage volume is the S3 URL https://s3-{region}.amazonaws.com.

    Args:
        region (str | None, optional): The AWS region. Defaults to get_region() (envionment setting BUCKET_REGION).

    Returns:
        str: Storage Volumen Path.
    """
    if is_use_s3():
        if not region:
            region = get_region()
        return f"https://s3-{region}.amazonaws.com"
    else:
        return os.getenv(ENV_VOLUME, os.path.join(os.getcwd(), V_LOCAL))


def get_temp_dir(path: str | None = None) -> str:
    """
    Get the temporary directory for the application.  This is specified in the environment variable TEMP_DIR.

    Args:
        path (str | None, optional): The path to append to the temporary directory. Defaults to None.

    Returns:
        str: The temporary directory
    """
    flder = os.getenv("TEMP_DIR", os.getenv("TEMP", tempfile.gettempdir()))
    return os.path.join(flder, path) if path else flder


def get_mode() -> str:
    """
    Get the mode from the environment variable ENV_LOCAL_MODE.  The default value is "service".

    Returns:
        str: The mode of the deployment
    """
    return V_LOCAL if is_local_mode() else V_SERVICE


def is_enforce_validation() -> bool:
    return os.environ.get(ENV_ENFORCE_VALIDATION, "true").lower() == "true"


def get_client() -> str | None:
    """
    Get the client name from the environment variable ENV_CLIENT.

    Returns:
        str | None: The client name
    """
    return os.getenv(ENV_CLIENT, os.getenv(ENV_AWS_PROFILE, None))


def get_client_name() -> str | None:
    """
    Get the client name from the environment variable ENV_CLIENT.

    Returns:
        str | None: The client name
    """
    return os.getenv(ENV_CLIENT_NAME, None)


def get_log_dir() -> str:
    """
    Get the log directory for the core automation engine.  This is specified in the environment variable LOG_DIR.
    If not specified, the current working directory is used.

    Returns:
        str: The log directory
    """
    return os.getenv(ENV_LOG_DIR, os.path.join(os.getcwd(), "local", "logs"))


def get_delivered_by() -> str:
    """
    Get the delivered by value from the environment variable ENV_DELIVERED_BY.

    Returns:
        str: The delivered by value. Default is "automation"
    """
    return os.getenv(ENV_DELIVERED_BY, "automation")


def get_aws_profile() -> str:
    """
    Return an AWS profile name that is based on the client region specified.

    Looks at the environment variable ENV_AWS_PROFILE.

    Returns:
        str: Value of the environment variable or client name or default
    """
    profile = os.getenv(ENV_AWS_PROFILE, get_client() or "default")

    try:
        # if the profile is not in the boto3.session credentials, then return "default"
        boto3.session.Session(profile_name=profile)
    except ProfileNotFound:
        return "default"

    return profile


def get_aws_region() -> str:
    """
    Get the AWS region from the environment variable ENV_AWS_REGION or V_DEFAULT_REGION.

    Returns:
        str: The AWS region
    """
    profile = get_aws_profile()

    try:
        # if the profile is not in the boto3.session credentials, then return "default"
        session = boto3.session.Session(profile_name=profile)
        return session.region_name
    except ProfileNotFound:
        return V_DEFAULT_REGION


def get_client_region() -> str:
    """
    Get the client region from the environment variable ENV_CLIENT_REGION or V_DEFAULT_REGION.

    This is the BASE region where all other regions are derived from.

    Returns:
        str: The AWS region for the client
    """
    return os.getenv(ENV_CLIENT_REGION, get_aws_region())


def get_master_region() -> str:
    """
    The AWS region of the Core-Automation engine.  If you don't specify this value, it will
    be derived from the client region.

    Returns:
        str: The AWS region for the Core Automation Engine
    """
    return os.getenv(ENV_MASTER_REGION, get_client_region())


def get_region() -> str:
    """
    Return the AWS region for the Deployment .  If not specified, the region will
    be derived from the master region.

    Returns:
        str: THe AWS region for the deployment
    """
    return os.getenv(ENV_AWS_REGION, get_master_region())


def get_bucket_region() -> str:
    """
    Get the bucket region from the environment variable ENV_BUCKET_REGION or the master region.

    Returns:
        str: The AWS region for the bucket where core automation objects are stored.
    """
    return os.environ.get(ENV_BUCKET_REGION, get_master_region())


def get_dynamodb_region() -> str:
    """
    Get the DynamoDB region from the environment variable ENV_DYNAMODB_REGION or the master region

    Returns:
        str: The AWS region for the DynamoDB table
    """
    return os.getenv(ENV_DYNAMODB_REGION, get_master_region())


def get_invoker_lambda_region() -> str:
    """
    Get the invoker lambda region from the environment variable ENV_INVOKER_LAMBDA_REGION or the master region.

    Returns:
        str: The AWS region for the invoker lambda
    """
    return os.getenv(ENV_INVOKER_LAMBDA_REGION, get_master_region())


def get_automation_account() -> str | None:
    """
    Return the AWS account number for the automation account.  This is specified in the environment variable ENV_AUTOMATION_ACCOUNT.

    Returns:
        str | None: The AWS account number for the automation account where the core automation is installed or None
    """
    return os.getenv(ENV_AUTOMATION_ACCOUNT, None)


def get_dynamodb_host() -> str:
    """
    The URL for the DynamoDB host.  This is specified in the environment variable ENV_DYNAMODB_HOST.  It is typically
    the AWS DynamoDB endpoint for the region.  However, you can specify a different endpoint if you are using a local
    DynamoDB instance or a different DynamoDB service.

    Returns:
        str: URL for the DynamoDB host
    """
    region = get_dynamodb_region()
    return os.getenv(ENV_DYNAMODB_HOST, f"https://dynamodb.{region}.amazonaws.com")


def get_step_function_arn() -> str:
    """
    Core Automation Step Function ARN.  This is specified in the environment variable RUNNER_STEP_FUNCTION_ARN.
    If not specified, the default value is used based on the region and account number.

    Returns:
        str: The ARN for the Core Automation Step Function
    """
    region = get_region()

    if is_local_mode():
        return f"arn:aws:states:{region}:local:execution:stateMachineName:CoreAutomationRunner"

    account = get_automation_account()
    return os.environ.get(
        ENV_RUNNER_STEP_FUNCTION_ARN,
        f"arn:aws:states:{region}:{account}:stateMachine:CoreAutomationRunner",
    )


def get_invoker_lambda_name() -> str:
    """
    The name of the invoker lambda.  This is specified in the environment variable ENV_INVOKER_LAMBDA_NAME.

    The default value is "core-automation-invoker"

    Returns:
        str: The name of the invoker lambda
    """
    return os.getenv(ENV_INVOKER_LAMBDA_NAME, f"{V_CORE_AUTOMATION}-invoker")


def get_api_lambda_name() -> str:
    """
    The name of the Core Automation API Lambda.  This is specified in the environment variable ENV_API_LAMBDA_NAME.

    The default value is "core-automation-api"

    Returns:
        str: The name of the Core Automation API Lambda
    """
    return os.getenv(ENV_API_LAMBDA_NAME, f"{V_CORE_AUTOMATION}-api")


def get_api_lambda_arn() -> str:
    """
    The ARN of the Core Automation API Lambda.  This is specified in the environment variable ENV_API_LAMBDA_ARN.
    If not specified, the default value is used based on the region and account number.

    Returns:
        str: The ARN for the Core Automation API Lambda
    """
    region = get_region()
    account = get_automation_account()
    name = get_api_lambda_name()
    return os.getenv(
        ENV_API_LAMBDA_ARN,
        f"arn:aws:lambda:{region}:{account}:function:{name}",
    )


def get_invoker_lambda_arn() -> str:
    """
    The ARN of the invoker lambda.  This is specified in the environment variable ENV_INVOKER_LAMBDA_ARN.
    If not specified, the default value is used based on the region and account number.

    Returns:
        str: The ARN for the Core Automation Invoker lambda
    """
    region = get_region()
    account = get_automation_account()
    invoker_name = get_invoker_lambda_name()
    return os.getenv(
        ENV_INVOKER_LAMBDA_ARN,
        f"arn:aws:lambda:{region}:{account}:function:{invoker_name}",
    )


def get_execute_lambda_arn() -> str:
    """
    The ARN of the execute lambda.  This is specified in the environment variable ENV_EXECUTE_LAMBDA_ARN.
    If not specified, the default value is used based on the region and account number.

    Returns:
        str: The ARN for the Core Automation Execute lambda
    """
    region = get_region()
    account = get_automation_account()
    return os.getenv(
        ENV_EXECUTE_LAMBDA_ARN,
        f"arn:aws:lambda:{region}:{account}:function:{V_CORE_AUTOMATION}-execute",
    )


def get_start_runner_lambda_arn() -> str:
    """
    The ARN of the start runner lambda.  This is specified in the environment variable ENV_START_RUNNER_LAMBDA_ARN.
    If not specified, the default value is used based on the region and account number

    Returns:
        str: The ARN for the Core Automation Start Runner lambda
    """
    region = get_region()
    account = get_automation_account()
    return os.getenv(
        ENV_START_RUNNER_LAMBDA_ARN,
        f"arn:aws:lambda:{region}:{account}:function:{V_CORE_AUTOMATION}-runner",
    )


def get_deployspec_compiler_lambda_arn() -> str:
    """
    The ARN of the deployspec compiler lambda.  This is specified in the environment variable ENV_DEPLOYSPEC_COMPILER_LAMBDA_ARN.
    If not specified, the default value is used based on the region and account number.

    Returns:
        str: The ARN for the Core Automation Deployspec Compiler lambda
    """
    region = get_region()
    account = get_automation_account()
    return os.getenv(
        ENV_DEPLOYSPEC_COMPILER_LAMBDA_ARN,
        f"arn:aws:lambda:{region}:{account}:function:{V_CORE_AUTOMATION}-deployspec-compiler",
    )


def get_component_compiler_lambda_arn() -> str:
    """
    The ARN of the component compiler lambda.  This is specified in the environment variable ENV_COMPONENT_COMPILER_LAMBDA_ARN.
    If not specified, the default value is used based on the region and account number

    Returns:
        str: The ARN for the Core Automation Component Compiler lambda
    """
    region = get_region()
    account = get_automation_account()
    return os.getenv(
        ENV_COMPONENT_COMPILER_LAMBDA_ARN,
        f"arn:aws:lambda:{region}:{account}:function:{V_CORE_AUTOMATION}-component-compiler",
    )


def get_environment() -> str:
    """
    Get the environment name from the environment variable ENV_ENVIRONMENT.

    Returns:
        str: The environment name
    """
    return os.getenv(ENV_ENVIRONMENT, "prod")


def __custom_serializer(obj: Any) -> Any:
    """
    Handy tool for deserializing json objects that contain datetime objects as for SOME reason
    the standard json deserializer does not support datetime objects. (No one knows why)

    Args:
        obj: The object to serialize

    Returns:
        Any: The serialized object
    """
    """Custom serializer for objects not serializable by default json code"""
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    elif isinstance(obj, datetime.date):
        return obj.isoformat()
    elif isinstance(obj, datetime.time):
        return obj.isoformat()
    elif isinstance(obj, Decimal):
        return float(obj)  # or str(obj) if precision is important
    # No need to handle strings, ints, lists, dicts, etc. as they are already supported
    raise TypeError(f"Type {type(obj)} not serializable")


def to_json(data: Any, pretty: int | None = None) -> str:
    """
    The Json serializer for the data object.  This will serialize datetime objects and other objects that are not
    serializable by the default json serializer.

    !!! NOTICE !!!

    This function will convert date time objects to strings in the ISO8601 format.

    Args:
        data (dict): The data object to serialize
        pretty (int, optional): The pretty print indent level. Defaults to None

    Returns:
        str: JSON string
    """
    if data is None:
        return V_EMPTY  # or should we return "[]" or "{}"?

    return json.dumps(data, indent=pretty, default=__custom_serializer)


def write_json(data: Any, output_stream: IO, pretty: int | None = None) -> None:
    """Write the json data dict or list to a JSON file on the output_stream.

    !!! NOTICE !!!

    This function will convert date time objects to strings in the ISO8601 format.

    Args:
        data (Any): The data to write to the output stream
        output_stream (Any): The output stream to write the data to.
        pretty (int, optional): The pretty print indent level. Defaults to None

    """
    json.dump(data, output_stream, indent=pretty, default=__custom_serializer)


def __iso8601_parser(data: Any) -> Any:

    if isinstance(data, str):
        try:
            return datetime.datetime.fromisoformat(data)
        except ValueError:
            return data
    elif isinstance(data, dict):
        return {key: __iso8601_parser(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [__iso8601_parser(item) for item in data]
    return data


def from_json(data: str) -> Any:
    """
    The Json deserializer for the data object.  This will deserialize
    datetime objects and other objects that are not standard JSON objects.

    !!! WARNING !!!

    This function will convert date time strings in the json data to datetime objects.

    If you want strings, you will have to reconvert them back to strings yourself.

    Args:
        data (str): The JSON string to deserialize

    Returns:
        dict: The deserialized data object
    """
    return json.loads(data, object_hook=__iso8601_parser)


def read_json(input_stream: IO) -> Any:
    """Load the json data from the input stream. and respond with a dict or list object.

    !!! WARNING !!!

    This function will convert date time strings in the json data to datetime objects.

    If you want strings, you will have to reconvert them back to strings yourself.

    Args:
        input_stream (Any): The input stream to read the json data from

    Returns:
        Any: The json data as a dict or list object

    """
    return json.load(input_stream, object_hook=__iso8601_parser)


def __quote_strings(data: Any):
    """Recursively quote all strings in the data."""
    if isinstance(data, dict):
        return {k: v if k == "Label" else __quote_strings(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [__quote_strings(v) for v in data]
    elif isinstance(data, str):
        return DoubleQuotedScalarString(data)
    elif isinstance(data, datetime.datetime):
        return DoubleQuotedScalarString(data.isoformat())
    elif isinstance(data, datetime.date):
        return DoubleQuotedScalarString(data.isoformat())
    elif isinstance(data, datetime.time):
        return DoubleQuotedScalarString(data.isoformat())
    else:
        return data


def to_yaml(data: Any) -> str:
    """Convert data dict or list to a YAML string.

    Strings are "Quoted" so you won't run into issues with string "000001" being converted to an integer "1".

    """
    quoted_data = __quote_strings(data)

    y = YAML(typ="rt")
    y.default_flow_style = False
    y.preserve_quotes = True
    y.indent(mapping=2, sequence=4, offset=2)

    s = io.StringIO()
    y.dump(quoted_data, s)
    return s.getvalue()


def write_yaml(data: Any, stream: IO) -> None:
    """Write the dictionary (or list) data to the proided output stream as YAML.

    !!! NOTICE !!!

    datetime object will be converted to strings in the ISO8601 format.

    Args:
        data (Any): The data to write to the output stream
        stream (Any): The output stream to write the data to.

    """

    quoted_data = __quote_strings(data)

    y = YAML(typ="rt")
    y.default_flow_style = False
    y.preserve_quotes = True
    y.indent(mapping=2, sequence=4, offset=2)

    y.dump(quoted_data, stream)


def __iso8601_constructor(loader, node):
    value = loader.construct_scalar(node)
    try:
        return datetime.datetime.fromisoformat(value)
    except ValueError:
        return value


def from_yaml(data: str) -> Any:
    """Convert yaml str to a dict or list.

    # TODO - compare this to the from_yaml in the yamlmerge object and
    # let's do a lot of testing and see if they can be combined into
    # a single function.  The yamlmerge object is a bit more complex

    !!! WARNING !!!

    This is not entirely a RoundTrip parser.  If you have dates in your data
    this function will convert them to datetime objects.

    If you are expecing dates to be a string.  Sorry, you will need to convert
    them back to a string yourself.

    Args:
        data (str): The yaml string to convert to a dict or list

    Returns:
        Any: The yaml data as a dict or list object

    """
    y = YAML(typ="rt")
    y.Constructor.add_constructor("tag:yaml.org,2002:str", __iso8601_constructor)
    return y.load(data)


def read_yaml(input_stream: IO) -> Any:
    """Load the yaml data from the input stream.

    This uses the "rount-trip" yaml parser. so you will get an OrderedDict
    as a response.  But it is not entirely "round Trip"

    !!! WARNING !!!

    This is not entirely a RoundTrip parser.  If you have dates in your data
    this function will convert them to datetime objects.

    If you are expecing dates to be a string.  Sorry, you will need to convert
    them back to a string yourself.

    Args:
        input_stream (Any): The input stream to read the yaml data from

    Returns:
        Any: The yaml data is a dict or list object
    """
    y = YAML(typ="rt")
    y.Constructor.add_constructor("tag:yaml.org,2002:str", __iso8601_constructor)
    return y.load(input_stream)
