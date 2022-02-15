# Customer Microservice

Those instructions are valid for all microservices under this repository.

### Prerequisites
You must pass all steps firstly on this [document](../README.md). 

### Database Initialization
Create a database PostgresSQL
```sql
create database burgerzilla_customer
```
Initialize models on PostgresSQL
```bash
start customer_database.bat
``` 
Run the project with this command
```bash
cd /1_customer_service/
poetry run python run.py
```     