from brownie import SimpleStorage,accounts

def test_deploy():
    # Arrange
    account = accounts[0]
    #ACt
    simple_storage = SimpleStorage.deploy({"from":account})
    starting_value = 0
    # asert
    assert starting_value == simple_storage.retrieve()

def test_updating():
    account = accounts[0]
    simplestorage = SimpleStorage.deploy({"from":account})
    expected  = 15
    simplestorage.store(15,{"from":account})
    assert expected == simplestorage.retrieve()