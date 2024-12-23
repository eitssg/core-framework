"""
This module provides a list of constants that are used throughout the Core-Automation framework.

The constants prevent mistyping and provide a single source of truth for the values used in the framework.

This includes values for the Task Payload, Task Results, Task Result, and other objects used in the framework.

"""

# Good to go
HTTP_OK = 200
""" \\- "200 OK" """
HTTP_CREATED = 201
""" \\- "201 Created" " """
HTTP_ACCEPTED = 202
""" \\- "202 Accepted" " """
HTTP_NO_CONTENT = 204
""" \\- "204 No Content" """

# Bad to go
HTTP_BAD_REQUEST = 400
""" \\- "400 Bad Request" """
HTTP_UNAUTHORIZED = 401
""" \\- "401 Unauthorized" """
HTTP_PAYMENT_REQUIRED = 402
""" \\- "402 Payment Required" """
HTTP_FORBIDDEN = 403
""" \\- "403 Forbidden" """
HTTP_NOT_FOUND = 404
""" \\- "404 Not Found" """
HTTP_METHOD_NOT_ALLOWED = 405
""" \\- "405 Method Not Allowed" """
HTTP_NOT_ACCEPTABLE = 406
""" \\- "406 Not Acceptable" """
HTTP_PROXY_AUTHENTICATION_REQUIRED = 407
""" \\- "407 Proxy Authentication Required" """
HTTP_REQUEST_TIMEOUT = 408
""" \\- "408 Request Timeout" """
HTTP_CONFLICT = 409
""" \\- "409 Conflict" """

# Can't process data
HTTP_UNPROCESSABLE_ENTITY = 422
""" \\- "422 Unprocessable Entity" """

# Server Error
HTTP_INTERNAL_SERVER_ERROR = 500
""" \\- "500 Internal Server Error" """
HTTP_NOT_IMPLEMENTED = 501
""" \\- "501 Not Implemented" """

# Task Types
TASK_PACKAGE = "package"
""" \\- "package" """
TASK_UPLOAD = "upload"
""" \\- "upload" """
TASK_COMPILE = "compile"
""" \\- "compile" """
TASK_DEPLOY = "deploy"
""" \\- "deploy" """
TASK_PLAN = "plan"
""" \\- "plan" """
TASK_APPLY = "apply"
""" \\- "apply" """
TASK_RELEASE = "release"
""" \\- "release" """
TASK_TEARDOWN = "teardown"
""" \\- "teardown" """
TASK_COMPILE_PIPELINE = "compile-pipeline"
""" \\- "compile-pipeline" """
TASK_COMPILE_DEPLOYSPEC = "compile-deployspec"
""" \\- "compile-deployspec" """

# Feild values
V_CORE_AUTOMATION = "core-automation"
""" \\- "core-automation" """
V_PACKAGE_ZIP = "package.zip"
""" \\- "package.zip" """
V_PACKAGE_TAR = "package.tar"
""" \\- "package.tar" """
V_PIPELINE = "pipeline"
""" \\- "pipeline" """
V_DEPLOYSPEC = "deployspec"
""" \\- "deployspec" """
V_DEPLOYSPEC_FILE_YAML = "deployspec.yaml"
""" \\- "deployspec.yaml" """
V_DEPLOYSPEC_FILE_YML = "deployspec.yml"
""" \\- "deployspec.yml" """
V_DEPLOYSPEC_FILE_JSON = "deployspec.json"
""" \\- "deployspec.json" """
V_LAMBDA_MODULES_FILE = "lambda_modules.txt"
""" \\- "lambda_modules.txt" """
V_SERVICE = "service"
""" \\- "service" """
V_LOCAL = "local"
""" \\- "local" """
V_FULL = "full"
""" \\- "full" """
V_PLATFORM = "platform"
""" \\- "platform" """
V_CREATE_STACK = "create_stack"
""" \\- "create_stack" """
V_DEFAULT_REGION = "us-east-1"
""" \\- "ap-southeast-1" """
V_DEFAULT_REGION_NAME = "US East (N. Virginia)"
""" \\- "Singapore" """
V_DEFAULT_REGION_ALIAS = "use"
""" \\- "sin" """
V_DEFAULT_BRANCH = "master"
""" \\- "master" """
V_DEFAULT_ENVIRONMENT = "prod"
""" \\- "prod" """
V_TRUE = "true"
""" \\- "true" """
V_FALSE = "false"
""" \\- "false" """
V_EMPTY = ""
""" \\- "" """

# Authorization Context Object
AUTH_CREDENTIALS = "Credentials"
""" \\- "Credentials" """
AUTH_ROLE = "Role"
""" \\- "Role" """
AUTH_ACCOUNT = "Account"
""" \\- "Account" """
AUTH_USER = "User"
""" \\- "User" """
AUTH_ACCESS_KEY = "AccessKey"
""" \\- "AccessKey" """
AUTH_SECRET_KEY = "SecretKey"
""" \\- "SecretKey" """
AUTH_TOKEN = "Token"
""" \\- "Token" """
AUTH_ACCESS_KEY_ID = "AccessKeyId"
""" \\- "AccessKeyId" """
AUTH_SECRET_ACCESS_KEY = "SecretAccessKey"
""" \\- "SecretAccessKey" """
AUTH_SESSION_TOKEN = "SessionToken"
""" \\- "SessionToken" """

# Account object in Authorization Context
ACCOUNT_ID = "Id"
""" \\- "Id" """
ACCOUNT_REGION = "Region"
""" \\- "Region" """
ACCOUNT_USER_ARN = "UserArn"
""" \\- "UserArn" """
ACCOUNT_USER_ID = "UserId"
""" \\- "UserId" """

# Task Payload Object
TP_TASK = "Task"
""" \\- "Task" """
TP_FORCE = "Force"
""" \\- "Force" """
TP_DRY_RUN = "DryRun"
""" \\- "DryRun" """
TP_IDENTITY = "Identity"
""" \\- "Identity" """
TP_TYPE = "Type"
""" \\- "Type" """
TP_DEPLOYMENT_DETAILS = "DeploymentDetails"
""" \\- "DeploymentDetails" """
TP_PACKAGE_DETAILS = "Package"
""" \\- "Package" """
TP_FACTS = "Facts"
""" \\- "Facts" """
TP_ACTIONS = "Actions"
""" \\- "Actions" """
TP_DEPLOY_ACTIONS = "DeployActions"
""" \\- "DeployActions" """
TP_STATE = "State"
""" \\- "State" """
TP_FLOW_CONTROL = "FlowControl"
""" \\- "FlowControl" """

# TP_ACTIONS/TP_STATE Actions Object Attributes
ACT_VERSION = "VersionId"
""" \\- "VersionId" """
ACT_BUCKETNAME = "BucketName"
""" \\- "BucketName" """
ACT_BUCKET_REGION = "BucketRegion"
""" \\- "BucketRegion" """
ACT_KEY = "Key"
""" \\- "Key" """
ACT_MIME_TYPE = "ContentType"
""" \\- "ContentType" """

# Deployment Details object
DD_CLIENT = "Client"
""" \\- "Client" """
DD_APP = "App"
""" \\- "App" """
DD_PORTFOLIO = "Portfolio"
""" \\- "Portfolio" """
DD_BRANCH = "Branch"
""" \\- "Branch" """
DD_BRANCH_SHORT_NAME = "BranchShortName"
""" \\- "BranchShortName" """
DD_BUILD = "Build"
""" \\- "Build" """
DD_COMPONENT = "Component"
""" \\- "Component" """
DD_ENVIRONMENT = "Environment"
""" \\- "Environment" """
DD_DATA_CENTER = "DataCenter"
""" \\- "DataCenter" """
DD_SCOPE = "Scope"
""" \\- "Scope" """
DD_ECR = "Ecr"  # ECR object for docker containers
""" \\- "Ecr" """
DD_TAGS = "Tags"  # A place to hold tags for the deployment
""" \\- "Tags" """

# Docker Image
ECR_REGISTRY_URI = "RegistryUri"
""" \\- "RegistryUri" """

# Standard Tags / Tagging Policy
TAG_NAME = "Name"  # This is actually the PRN or component name with PRN prefix
""" \\- "Name" """
TAG_CLIENT = "Client"
""" \\- "Client" """
TAG_PORTFOLIO = "Portfolio"
""" \\- "Portfolio" """
TAG_APP = "App"
""" \\- "App" """
TAG_BRANCH = "Branch"
""" \\- "Branch" """
TAG_BUILD = "Build"
""" \\- "Build" """

# Prod/NotProd/Dev/UAT1/UAT2 (a.k.a. Zone or Data Center)
TAG_ENVIRONMENT = "Environment"
""" \\- "Environment" """

TAG_COMPONENT = "Component"
""" \\- "Component" """
TAG_ZONE = "Zone"
""" \\- "Zone" """
TAG_REGION = "Region"
""" \\- "Region" """
TAG_CAPEX_CODE = "CapexCode"
""" \\- "CapexCode" """
TAG_OPEX_CODE = "OpexCode"
""" \\- "OpexCode" """
TAG_JIRA_CODE = "JiraCode"
""" \\- "JiraCode" """
TAG_OWNER = "Owner"
""" \\- "Owner" """
TAG_CONTACTS = "Contacts"
""" \\- "Contacts" """

# Package Object
PKG_BUCKET_REGION = "BucketRegion"
""" \\- "BucketRegion" """
PKG_BUCKET_NAME = "BucketName"
""" \\- "BucketName" """
PKG_S3_KEY = "Key"
""" \\- "Key" """
PKG_VERSION_ID = "VersionId"
""" \\- "VersionId" """
PKG_MODE = "Mode"
""" \\- "Mode" """
PKG_APP_PATH = "AppPath"
""" \\- "AppPath" """
PKG_COMPILE_MODE = "CompileMode"
""" \\- "CompileMode" """
PKG_DEPLOYSPEC = "DeploySpec"
""" \\- "DeploySpec" """
PKG_TEMPDIR = "TempDir"
""" \\- "TempDir" """


# Deployspec Object
DS_LABEL = "label"
""" \\- "label" """
DS_TYPE = "type"
""" \\- "type" """
DS_PARAMS = "params"
""" \\- "params" """
# array of DS_LABEL (only useful in deployspec with more than one deployment)
DS_DEPENDS_ON = "depends_on"
""" \\- "depends_on" """

# Deployspec Types
DS_TYPE_AWS_CREATE_STACK = "aws.create_stack"
""" \\- "aws.create_stack" """
DS_TYPE_CREATE_STACK = "create_stack"
""" \\- "create_stack" """
DS_TYPE_AWS_DELETE_STACK = "aws.delete_stack"
""" \\- "aws.delete_stack" """
DS_TYPE_DELETE_STACK = "delete_stack"
""" \\- "delete_stack" """
DS_TYPE_AWS_DELETE_USER = "aws.delete_user"
""" \\- "aws.delete_user" """
DS_TYPE_DELETE_USER = "delete_user"
""" \\- "delete_user" """
DS_TYPE_AWS_CREATE_USER = "aws.create_user"
""" \\- "aws.create_user" """
DS_TYPE_CREATE_USER = "create_user"
""" \\- "create_user" """

# Deployspec Params Object
DSP_TEMPLATE = "template"
""" \\- "template" """
DSP_STACK_NAME = "stack_name"
""" \\- "stack_name" """
DSP_PARAMETERS = "parameters"
""" \\- "parameters" """
DSP_ACCOUNT = "account"
""" \\- "account" """
DSP_ACCOUNTS = "accounts"
""" \\- "accounts" """
DSP_REGION = "region"
""" \\- "region" """
DSP_REGIONS = "regions"
""" \\- "regions" """
DSP_USER_NAME = "user_name"
""" \\- "user_name" """
DSP_STACK_POLICY = "stack_policy"
""" \\- "stack_policy" """

# Scopes
SCOPE_CLIENT = "client"
""" \\- "client" """
SCOPE_ZONE = "zone"
""" \\- "zone" """
SCOPE_PORTFOLIO = "portfolio"
""" \\- "portfolio" """
SCOPE_APP = "app"
""" \\- "app" """
SCOPE_BRANCH = "branch"
""" \\- "branch" """
SCOPE_BUILD = "build"
""" \\- "build" """
SCOPE_COMPONENT = "component"
""" \\- "component" """
SCOPE_ENVIRONMENT = "environment"
""" \\- "environment" """
SCOPE_SHARED = "shared"
""" \\- "shared" """
SCOPE_RELEASE = "release"
""" \\- "release" """

# Object Types
OBJ_FILES = "files"
""" \\- "files" """
OBJ_ARTEFACTS = "artefacts"
""" \\- " artefacts " """
OBJ_PACKAGES = "packages"
""" \\- "packages" """

# Task Results Object
TASK_RESULTS = "Results"
""" \\- "Results" """

# Task Result Object
TR_COMPILE_RESULTS = "CompileResults"
""" \\- "CompileResults" """
TR_STATUS = "Status"
""" \\- "Status" """
TR_MESSAGE = "Message"
""" \\- "Message" """
TR_DETAILS = "Details"
""" \\- "Details" """
TR_ERRORS = "Errors"
""" \\- "Errors" """
TR_WARNINGS = "Warnings"
""" \\- "Warnings" """
TR_RESPONSE = "Response"
""" \\- "Response" """

# Step Function Execution Object
SF_EXECUTION_ARN = "StepFunctionArn"
""" \\- "StepFunctionArn" """
SF_INPUT = "Input"
""" \\- "Input" """

# Environment Variables
ENV_AWS_PROFILE = "AWS_PROFILE"
""" \\- "AWS_PROFILE" """
ENV_AWS_REGION = "AWS_REGION"
""" \\- "AWS_REGION" """
ENV_CLIENT = "CLIENT"
""" \\- "CLIENT" """
# Alias for CLIENT
ENV_CLIENT_NAME = "CLIENT_NAME"
""" \\- "CLIENT_NAME" """
ENV_PORTFOLIO = "PORTFOLIO"
""" \\- "PORTFOLIO" """
ENV_APP = "APP"
""" \\- "APP" """
ENV_BRANCH = "BRANCH"
""" \\- "BRANCH" """
ENV_BUILD = "BUILD"
""" \\- "BUILD" """
ENV_COMPONENT = "COMPONENT"
""" \\- "COMPONENT" """
ENV_ENVIRONMENT = "ENVIRONMENT"
""" \\- "ENVIRONMENT" """
ENV_SCOPE = "SCOPE"
""" \\- "SCOPE" """
ENV_TASKS = "TASKS"
""" \\- "TASKS" """
ENV_UNITS = "UNITS"
""" \\- "UNITS" """
ENV_ENFORCE_VALIDATION = "ENFORCE_VALIDATION"
""" \\- "ENFORCE_VALIDATION" """
ENV_LOCAL_MODE = "LOCAL_MODE"
""" \\- "LOCAL_MODE" """
ENV_API_LAMBDA_ARN = "API_LAMBDA_ARN"
""" \\- "API_LAMBDA_ARN" """
ENV_API_LAMBDA_NAME = "API_LAMBDA_NAME"
""" \\- "API_LAMBDA_NAME" """
ENV_INVOKER_LAMBDA_ARN = "INVOKER_LAMBDA_ARN"
""" \\- "INVOKER_LAMBDA_ARN" """
ENV_INVOKER_LAMBDA_NAME = "INVOKER_LAMBDA_NAME"
""" \\- "INVOKER_LAMBDA_NAME" """
ENV_INVOKER_LAMBDA_REGION = "INVOKER_LAMBDA_REGION"
""" \\- "INVOKER_LAMBDA_REGION" """
ENV_DYNAMODB_REGION = "DYNAMODB_REGION"
""" \\- "DYNAMODB_REGION" """
ENV_DYNAMODB_HOST = "DYNAMODB_HOST"
""" \\- "DYNAMODB_HOST" """
ENV_AUTOMATION_TYPE = "AUTOMATION_TYPE"
""" \\- "AUTOMATION_TYPE" """
ENV_BUCKET_NAME = "BUCKET_NAME"
""" \\- "BUCKET_NAME" """
ENV_BUCKET_REGION = "BUCKET_REGION"
""" \\- "BUCKET_REGION" """
ENV_EXECUTE_LAMBDA_ARN = "EXECUTE_LAMBDA_ARN"
""" \\- "EXECUTE_LAMBDA_ARN" """
ENV_START_RUNNER_LAMBDA_ARN = "START_RUNNER_LAMBDA_ARN"
""" \\- "RUNNER_LAMBDA_ARN" """
ENV_DEPLOYSPEC_COMPILER_LAMBDA_ARN = "DEPLOYSPEC_COMPILER_LAMBDA_ARN"
""" \\- "DEPLOYSPEC_COMPILER_LAMBDA_ARN" """
ENV_COMPONENT_COMPILER_LAMBDA_ARN = "COMPONENT_COMPILER_LAMBDA_ARN"
""" \\- "COMPONENT_COMPILER_LAMBDA_ARN" """
ENV_CLIENT_REGION = "CLIENT_REGION"
""" \\- "CLIENT_REGION" """
ENV_MASTER_REGION = "MASTER_REGION"
""" \\- "MASTER_REGION" """
ENV_AUTOMATION_ACCOUNT = "AUTOMATION_ACCOUNT"
""" \\- "AUTOMATION_ACCOUNT" """
ENV_ARTEFACT_BUCKET_REGION = "ARTEFACT_BUCKET_REGION"
""" \\- "ARTEFACT_BUCKET_REGION" """
ENV_ARTEFACT_BUCKET_NAME = "ARTEFACT_BUCKET_NAME"
""" \\- "ARTEFACT_BUCKET_NAME" """
ENV_LOG_AS_JSON = "LOG_AS_JSON"
""" \\- "LOG_AS_JSON" """
ENV_STORE_VOLUME = "STORE_VOLUME"
""" \\- "STORE_VOLUME" """
ENV_DELIVERED_BY = "DELIVERED_BY"
""" \\- "DELIVERED_BY" """

# Jina2 Context Fitler Constants
CTX_TAGS = "tags"
""" \\- "tags" """
CTX_APP = "app"
""" \\- "app" """
CTX_CONTEXT = "context"
""" \\- "context" """
CTX_COMPONENT_NAME = "component_name"
""" \\- "component_name" """
CTX_FILES_BUCKET_URL = "FilesBucketUrl"
""" \\- "FilesBucketUrl" """
CTX_SHARED_FILES_PREFIX = "SharedFilesPrefix"
""" \\- "SharedFilesPrefix" """
CTX_PORTFOLIO_FILES_PREFIX = "PortfolioFilesPrefix"
""" \\- "PortfolioFilesPrefix" """
CTX_APP_FILES_PREFIX = "AppFilesPrefix"
""" \\- "AppFilesPrefix" """
CTX_BRANCH_FILES_PREFIX = "BranchFilesPrefix"
""" \\- "BranchFilesPrefix" """
CTX_BUILD_FILES_PREFIX = "BuildFilesPrefix"
""" \\- "BuildFilesPrefix" """
CTX_SNAPSHOT_ALIASES = "SnapshotAliases"
""" \\- "SnapshotAliases" """
CTX_ACCOUNT_ALIASES = "AccountAliases"
""" \\- "AccountAliases" """

# Source Types for security rules
ST_CIDR = "cidr"
""" \\- "cidr" """
ST_IP_ADDRESS = "ip"
""" \\- "ip" """
ST_COMPONENT = "component"
""" \\- "component" """
ST_PREFIX = "prefix"
""" \\- "prefix" """
ST_SECURITY_GROUP = "sg-attachment"
""" \\- "sg-attachment" """

# Facts
FACTS_ACCOUNT = "AccountFacts"
""" \\- "AccountFacts" """
FACTS_REGION = "RegionFacts"
""" \\- "RegionFacts" """
FACTS_IMAGE = "ImageAliases"
""" \\- "ImageAliases" """
FACTS_TAGS = "TagFacts"
""" \\- "TagFacts" """
FACTS_VPC = "VpcAliases"
""" \\- "VpcAliases" """
FACTS_SUBNET = "SubnetAliases"
""" \\- "SubnetAliases" """
FACTS_ENVIRONMENT = "Environment"
""" \\- "Environment" """
FACTS_SECURITY = "SecurityAliases"
""" \\- "SecurityAliases" """
FACTS_SECURITY_GROUP = "SecurityGroupAliases"
""" \\- "SecurityGroupAliases" """

# In Development
CORE_AUTOMATION_API_WRITE_ROLE = "CoreAutomationApiWriteRole"
""" \\- "CoreAutomationApiWriteRole" """
CORE_AUTOMATION_API_READ_ROLE = "CoreAutomationApiReadRole"
""" \\- "CoreAutomationApiReadRole" """
CORE_AUTOMATION_DEPLOYMENT_WRITE_ROLE = "CoreAutomationDeploymentWriteRole"
""" \\- "CoreAutomationDeploymentWriteRole" """
CORE_AUTOMATION_DEPLOYMENT_READ_ROLE = "CoreAutomationDeploymentReadRole"
""" \\- "CoreAutomationDeploymentReadRole" """
CORE_AUTOMATION_SESSION_ID_PREFIX = "Pipeline"
""" \\- "Pipeline" """
CORE_AUTOMATION_PIPELINE_PROVISIONING_ROLE = "PipelineProvisioningRole"
