# Customer Microservice

Those instructions are valid for all microservices under this repository.

### Prerequisites
You must pass all steps firstly on this [document](../README.md). 

### Database Initialization
Create a database PostgresSQL
```sql
create database burgerzilla_restaurant
```
Initialize models on PostgresSQL
```bash
start restaurant_database.bat
```
Run the project with this command
```bash
cd /3_restaurant_service/
poetry run python run.py
```     