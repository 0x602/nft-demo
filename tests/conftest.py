from scripts.helpful_scripts import *
import pytest


def skip_if_not_local_env():
    if not is_local_env():
        pytest.skip("Only for local testing")


def skip_if_local_env():
    if is_local_env():
        pytest.skip("Only for integration testing")


def is_local_env():
    return (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    )
