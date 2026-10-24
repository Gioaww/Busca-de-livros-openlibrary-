from projeto import traduz_genero

def test_inDict():
    assert traduz_genero("poesia") == "poetry"

def test_offDict():
    assert traduz_genero("xyz") == "xyz"

def test_numero():
    assert traduz_genero(0) == 0