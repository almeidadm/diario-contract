from diario_contract.version import CONTRACT_VERSION

def test_contract_version_defined():
    assert CONTRACT_VERSION.count(".") == 2
