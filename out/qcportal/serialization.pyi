import json
from typing import Any, Union

class _JSONEncoder(json.JSONEncoder):
    def default(self, obj: Any) -> Any: ...

def deserialize(data: Union[bytes, str], content_type: str): ...
def serialize(data, content_type: str) -> bytes: ...
def convert_numpy_recursive(obj, flatten: bool = False): ...
