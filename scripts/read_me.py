from brownie import accounts,config , network,SimpleStorage

def Read_contract():
    print(len(SimpleStorage))
    simple_storage = SimpleStorage[1]
    print(simple_storage.retrieve())
    print(SimpleStorage[0].retrieve())


    # same contract can be deployed to different account ex once I done my trasaction from myccoutn then
    # from somoneelse account
    print(simple_storage)


def main():
    Read_contract()