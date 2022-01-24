from scripts.helpful_scripts import *
from brownie import AdvancedCollectible


def deploy_and_create():
    account = get_account()
    advanced_collectible = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        network_config["keyhash"],
        network_config["fee"],
        {"from": account},
    )
    fund_with_link(advanced_collectible.address)
    creating_tx = advanced_collectible.createCollectible({"from": account})
    creating_tx.wait(1)
    print("New token has been created!")
    return advanced_collectible, creating_tx


def verify_contract():
    advanced_collectible = AdvancedCollectible[-1]
    is_verified = AdvancedCollectible.publish_source(advanced_collectible)
    if is_verified:
        print("Contract verified!")
    else:
        print("Verification failed!")


def main():
    deploy_and_create()
