from conftest import *
from scripts.advanced_collectible.deploy_and_create import deploy_and_create
import time


def test_can_create_advanced_collectible_integration():
    skip_if_local_env()
    # Arrange
    # Act
    advanced_collectible, creation_transaction = deploy_and_create()
    time.sleep(60)
    # Assert
    assert advanced_collectible.tokenCounter() == 1
