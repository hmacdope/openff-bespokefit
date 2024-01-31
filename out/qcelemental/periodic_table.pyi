from .exceptions import NotAnElementError as NotAnElementError
from _typeshed import Incomplete
from decimal import Decimal
from typing import Union

class PeriodicTable:
    Z: Incomplete
    E: Incomplete
    name: Incomplete
    EA: Incomplete
    A: Incomplete
    mass: Incomplete
    def __init__(self) -> None: ...
    def to_mass(self, atom: Union[int, str], *, return_decimal: bool = False) -> Union[float, 'Decimal']: ...
    def to_A(self, atom: Union[int, str]) -> int: ...
    def to_Z(self, atom: Union[int, str], strict: bool = False) -> int: ...
    def to_E(self, atom: Union[int, str], strict: bool = False) -> str: ...
    def to_element(self, atom: Union[int, str], strict: bool = False) -> str: ...
    to_mass_number = to_A
    to_atomic_number = to_Z
    to_symbol = to_E
    to_name = to_element
    def to_period(self, atom: Union[int, str]) -> int: ...
    def to_group(self, atom: Union[int, str]) -> Union[int, None]: ...

def run_comparison() -> None: ...
def write_c_header(filename: str = 'masses.h') -> None: ...

periodictable: Incomplete
