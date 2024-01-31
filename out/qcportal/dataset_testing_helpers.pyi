from qcportal import PortalRequestError as PortalRequestError
from qcportal.record_models import PriorityEnum as PriorityEnum, RecordStatusEnum as RecordStatusEnum
from qcportal.utils import now_at_utc as now_at_utc

def run_dataset_model_add_get_entry(snowflake_client, ds, test_entries, entry_extra_compare) -> None: ...
def run_dataset_model_add_entry_duplicate(snowflake_client, ds, test_entries, entry_extra_compare) -> None: ...
def run_dataset_model_delete_entry(snowflake_client, ds, test_entries, test_specs) -> None: ...
def run_dataset_model_add_get_spec(snowflake_client, ds, test_specs) -> None: ...
def run_dataset_model_add_spec_duplicate(snowflake_client, ds, test_specs) -> None: ...
def run_dataset_model_delete_spec(snowflake_client, ds, test_entries, test_specs) -> None: ...
def run_dataset_model_remove_record(snowflake_client, ds, test_entries, test_specs) -> None: ...
def run_dataset_model_submit(ds, test_entries, test_spec, record_compare) -> None: ...
def run_dataset_model_submit_missing(ds, test_entries, test_spec) -> None: ...
def run_dataset_model_iterate_updated(ds, test_entries, test_spec) -> None: ...
def run_dataset_model_modify_records(ds, test_entries, test_spec) -> None: ...
