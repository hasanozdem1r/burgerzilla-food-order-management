"""
This script is used to test helper's functionality
Hasan Özdemir 02-20-2022
"""
# path : root/order_ms/tests/test_helpers.py
from utils.helpers import generate_secret_key, get_postgres_configurations


def test_generate_secret_key():
    """
    TBD
    :return:
    """
    assert any(generate_secret_key(12)) is not None


def test_get_postgres_configurations():
    """
    TBD
    :return:
    """
    assert any(get_postgres_configurations()) is not None
