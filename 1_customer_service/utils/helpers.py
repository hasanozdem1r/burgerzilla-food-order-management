"""
This script is used to configure PostgresSQL environment variables
Hasan Özdemir 02-09-2022
"""
from os import getenv

def get_postgres_configurations()->tuple:
    """
    This method is created to get environment variables for PostgresSQL configurations
    :return: <tuple> configurations
    """
    POSTGRES_HOST=getenv('POSTGRES_HOST')
    POSTGRES_PORT=getenv('POSTGRES_PORT')
    POSTGRES_USER=getenv('POSTGRES_USER')
    POSTGRES_PWD=getenv('POSTGRES_PWD')

    return str(POSTGRES_HOST),str(POSTGRES_PORT),str(POSTGRES_USER),str(POSTGRES_PWD)


# script based test
if __name__=="__main__":
    print(get_postgres_configurations())