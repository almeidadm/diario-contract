from diario_contract.version import __version__

def test_contract_version_defined():
    assert str(__version__).count(".") == 2
