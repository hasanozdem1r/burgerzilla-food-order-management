"""
This script created to initialize configurations for Restaurant Microservice
Hasan Özdemir 02-07-2022
"""
# path : root/3_restaurant_service/config.py
# TODO typing implementation
from os import path
from dotenv import load_dotenv
from helpers import generate_connection_uri,generate_secret_key


# dDotenv adds .env support to your flask project.
# This is the file where we pass the environment variables.
dotenv_path = path.join(path.dirname(__file__), '.env')
if path.exists(dotenv_path):
    load_dotenv(dotenv_path)


# Global Environment Configurations
# This class contains the configurations common to all environments like development, QA and production, etc.
class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = generate_secret_key(32)
    SQLALCHEMY_DATABASE_URI = generate_connection_uri('db_config.ini')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# Development Environment Configurations
# Contains configuration settings used during development.
class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_ECHO = True


# Production Environment Configurations
# It contains configuration settings being used in production
class ProductionConfig(Config):
    ENV = "production"
    DEBUG = False
    SQLALCHEMY_ECHO = False
