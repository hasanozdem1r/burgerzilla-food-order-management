"""
This script created to initialize configurations for Restaurant Microservice
Hasan Özdemir 02-07-2022
"""
# path : root/2_restaurant_service/config.py
# TODO typing implementation
from os import path
from dotenv import load_dotenv

#dDotenv adds .env support to your flask project.
# This is the file where we pass the environment variables.
dotenv_path = path.join(path.dirname(__file__), '.env')
if path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# Global Environment Configurations
# This class contains the configurations common to all environments like development, QA and production, etc.
class Config:
    DEBUG=False
    TESTING=False
    # generated with secrets library
    # secrets.url_tokensafe() method is used
    SECRET_KEY = "mrfrIMEngCl0pAKqIIBS_g"
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:Hsn58.34@localhost:5432/burgerzilla_restaurant'
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

