# Customer Microservice

Those instructions are valid for all microservices under this repository.

### Prerequisites
You must pass all steps firstly on this [document](../README.md). 

### Database Initialization
Firstly initialize models on PostgresSQL
```bash
start order_database.bat
``` 
### Running project
Write this command on your terminal
```bash
cd /2_order_service/
poetry run python run.py
```     