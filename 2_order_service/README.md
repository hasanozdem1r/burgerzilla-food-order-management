# Customer Microservice

Those instructions are valid for all microservices under this repository.

### Prerequisites
You must pass all steps firstly on this [document](../README.md). 

### Database Initialization
Create a database PostgresSQL
```sql
create database burgerzilla_order
```
Initialize models on PostgresSQL
```bash
start order_database.bat
``` 
### Let's run our application
Run the project with this command
```bash
cd /2_order_service/
poetry run python run.py
```     