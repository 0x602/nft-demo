from scripts.helpful_scripts import *
from scripts.simple_collectible.deploy_and_create import deploy_and_create
from conftest import skip_if_not_local_env


def test_can_create_simple_collectible():
    skip_if_not_local_env()
    simple_collectible = deploy_and_create()
    assert simple_collectible.ownerOf(0) == get_account()
