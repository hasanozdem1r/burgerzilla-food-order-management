"""
This script is used to configure PostgresSQL environment variables
Hasan Özdemir 02-09-2022
"""
# path : root/order_ms/utils/helpers.py


def get_postgres_configurations() -> tuple:
    """
    This method is created to get environment variables for PostgresSQL configurations
    :return: <tuple> configurations
    """
    from os import getenv

    POSTGRES_HOST = getenv("POSTGRES_HOST")
    POSTGRES_PORT = getenv("POSTGRES_PORT")
    POSTGRES_USER = getenv("POSTGRES_USER")
    POSTGRES_PWD = getenv("POSTGRES_PWD")

    return str(POSTGRES_HOST), str(POSTGRES_PORT), str(POSTGRES_USER), str(POSTGRES_PWD)


def generate_secret_key(length: int) -> str:
    """
    This method used to generate secret key
    :param length: <int> length of secret key
    :return: <str> secret key
    """
    from secrets import token_urlsafe

    return str(token_urlsafe(length))


# script based test
if __name__ == "__main__":
    print(get_postgres_configurations())
    print(generate_secret_key(12))
