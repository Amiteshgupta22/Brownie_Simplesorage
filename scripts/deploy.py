from brownie import accounts,config,SimpleStorage,network
# importing Simpestorage from the deployed contract

from dotenv import load_dotenv 
import os


load_dotenv()

def deploy_simple_storage():
#    '''acccount = accounts.load("AMitesh")
#     account = accounts.add(config["wallets"]["from_key"])
#     print((account))'''
    account = get_account()
    # adding the account brownie account new Amitesh
    simple_storage = SimpleStorage.deploy({"from":account})
    store_value = simple_storage.retrieve()
    print(store_value)
    transaction = simple_storage.store(15,{"from":account})
    transaction.wait(1)
    updated_store_value = simple_storage.retrieve()
    simple_storage_ = SimpleStorage.deploy({"from":account})
    print(updated_store_value)

   # safest way to access the account even than evn variable dont use env variable 
def get_account():
    # if (network.show.active == "development"):
    #     return 
    print(os.getenv("PRIVATE_KEY"))
    account = accounts.add(config["wallets"]["from_key"])
    return account

def main():
    # print("Hello word!")
    deploy_simple_storage()