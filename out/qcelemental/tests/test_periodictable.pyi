from qcelemental.exceptions import NotAnElementError as NotAnElementError

def test_id_resolution(inp, expected) -> None: ...
def test_id_resolution_error(inp) -> None: ...
def test_id_resolution_strict(inp, expected) -> None: ...
def test_id_resolution_strict_error(inp) -> None: ...
def test_to_mass_krypton_decimal() -> None: ...
def test_to_mass(inp, expected) -> None: ...
def test_to_mass_number(inp, expected) -> None: ...
def test_to_atomic_number(inp, expected) -> None: ...
def test_to_atomic_number_strict(inp, expected) -> None: ...
def test_to_symbol(inp, expected) -> None: ...
def test_to_symbol_strict(inp, expected) -> None: ...
def test_to_element(inp, expected) -> None: ...
def test_to_element_strict(inp, expected) -> None: ...
def test_to_period(inp, expected) -> None: ...
def test_to_group(inp, expected) -> None: ...
def test_c_header() -> None: ...
def test_periodic_table_comparison() -> None: ...
