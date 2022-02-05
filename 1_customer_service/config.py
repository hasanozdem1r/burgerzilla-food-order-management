"""
This script created to initialize configurations for Customer Microservice
Hasan Özdemir 02-05-2022
"""
# root/1_customer_service/config.py

from os import path
from dotenv import load_dotenv

dotenv_path = path.join(path.dirname(__file__), '.env')
if path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# Global Environment Configurations
class Config:
    DEBUG=False
    TESTING=False
    SECRET_KEY = "mrfrIMEngCl0pAKqIIBS_g"
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:Hsn58.34@localhost:5432/burgerzilla_customer'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Development Environment Configurations
class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_ECHO = True

# Production Environment Configurations
class ProductionConfig(Config):
    ENV = "production"
    DEBUG = False
    SQLALCHEMY_ECHO = False

