"""
This script is used to provide helper methods for customer microservice
Hasan Özdemir 02-09-2022
"""
# path : root/3_restaurant_service/helpers.py

from configparser import ConfigParser

def generate_connection_uri(configuration_file: str) -> str:
    """
    This method is used to create CONNECTION_URI for PostgresSQL server
    :param configuration_file: <str> path of configuration file
    :return: <str> PostgresSQL CONNECTION_URI
    """
    # ConfigParser object
    c_obj = ConfigParser()
    # read from file
    c_obj.read(configuration_file)
    # get subtree from configuration file
    c_postgres = c_obj["POSTGRES"]
    c_postgres_credentials = c_obj["POSTGRES_CREDENTIALS"]
    # connection_uri
    connection_uri = f"{str(c_postgres['driver'])}://{str(c_postgres_credentials['username'])}:" \
                     f"{str(c_postgres_credentials['pwd'])}@{str(c_postgres['host'])}:{str(c_postgres['port'])}" \
                     f"/{str(c_postgres['db'])}"
    return str(connection_uri)

def generate_secret_key(length:int)->str:
    """
    This method generated from secrets package to generate application secret key
    :param length: <int> secret key length
    :return: <str> secret key
    """
    from secrets import token_urlsafe
    return str(token_urlsafe(length))

if __name__=='__main__':
    print(generate_connection_uri("db_config.ini"))
    print(generate_secret_key(12))