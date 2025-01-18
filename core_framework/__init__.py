from .merge import deep_copy, deep_merge_in_place, deep_merge, set_nested
from .models import (
    get_artefacts_path,
    get_files_path,
    get_packages_path,
    get_artefact_key,
    generate_task_payload,
    generate_package_details,
    generate_deployment_details_from_stack,
    generate_deployment_details,
)
from .common import (
    split_prn,
    split_branch,
    split_portfolio,
    get_prn,
    get_prn_alt,
    get_region,
    get_client,
    get_client_name,
    get_client_region,
    get_storage_volume,
    get_log_dir,
    get_temp_dir,
    get_delivered_by,
    get_aws_profile,
    get_automation_scope,
    get_automation_account,
    generate_branch_short_name,
    generate_bucket_name,
    get_api_lambda_name,
    get_api_lambda_arn,
    get_invoker_lambda_arn,
    get_invoker_lambda_name,
    get_invoker_lambda_region,
    get_execute_lambda_arn,
    get_start_runner_lambda_arn,
    get_deployspec_compiler_lambda_arn,
    get_component_compiler_lambda_arn,
    get_dynamodb_host,
    get_dynamodb_region,
    get_bucket_region,
    get_bucket_name,
    get_step_function_arn,
    get_artefact_bucket_name,
    get_artefact_bucket_region,
    get_provisioning_role_arn,
    get_environment,
    get_mode,
    is_local_mode,
    is_use_s3,
    is_enforce_validation,
    to_json,
    from_json,
    read_json,
    write_json,
    to_yaml,
    from_yaml,
    read_yaml,
    write_yaml,
)

from ._version import __version__

# import everything from prn_utils
from .prn_utils import (
    get_prn_scope,
    validate_item_prn,
    validate_portfolio_prn,
    validate_app_prn,
    validate_branch_prn,
    validate_build_prn,
    validate_component_prn,
    generate_portfolio_prn,
    generate_app_prn,
    generate_branch_prn,
    generate_build_prn,
    generate_component_prn,
    branch_short_name,
    extract_app,
    extract_portfolio,
    extract_branch,
    extract_build,
    extract_component,
    extract_portfolio_prn,
    extract_app_prn,
    extract_branch_prn,
    extract_build_prn,
    extract_component_prn,
)

__all__ = [
    "deep_copy",
    "deep_merge_in_place",
    "deep_merge",
    "set_nested",
    "get_artefacts_path",
    "get_files_path",
    "get_packages_path",
    "get_artefact_key",
    "generate_task_payload",
    "generate_package_details",
    "generate_deployment_details_from_stack",
    "generate_deployment_details",
    "split_prn",
    "split_branch",
    "split_portfolio",
    "get_prn",
    "get_prn_alt",
    "get_region",
    "get_client",
    "get_client_name",
    "get_client_region",
    "get_storage_volume",
    "get_log_dir",
    "get_temp_dir",
    "get_delivered_by",
    "get_aws_profile",
    "get_automation_scope",
    "get_automation_account",
    "generate_branch_short_name",
    "generate_bucket_name",
    "get_api_lambda_name",
    "get_api_lambda_arn",
    "get_invoker_lambda_arn",
    "get_invoker_lambda_name",
    "get_invoker_lambda_region",
    "get_execute_lambda_arn",
    "get_start_runner_lambda_arn",
    "get_deployspec_compiler_lambda_arn",
    "get_component_compiler_lambda_arn",
    "get_dynamodb_host",
    "get_dynamodb_region",
    "get_bucket_region",
    "get_bucket_name",
    "get_step_function_arn",
    "get_artefact_bucket_name",
    "get_artefact_bucket_region",
    "get_provisioning_role_arn",
    "get_environment",
    "get_mode",
    "is_local_mode",
    "is_use_s3",
    "is_enforce_validation",
    "to_json",
    "from_json",
    "read_json",
    "write_json",
    "to_yaml",
    "from_yaml",
    "read_yaml",
    "write_yaml",
    "get_prn_scope",
    "validate_item_prn",
    "validate_portfolio_prn",
    "validate_app_prn",
    "validate_branch_prn",
    "validate_build_prn",
    "validate_component_prn",
    "generate_portfolio_prn",
    "generate_app_prn",
    "generate_branch_prn",
    "generate_build_prn",
    "generate_component_prn",
    "branch_short_name",
    "extract_app",
    "extract_portfolio",
    "extract_branch",
    "extract_build",
    "extract_component",
    "extract_portfolio_prn",
    "extract_app_prn",
    "extract_branch_prn",
    "extract_build_prn",
    "extract_component_prn",
    "get_version",
]


def get_version():
    return __version__
