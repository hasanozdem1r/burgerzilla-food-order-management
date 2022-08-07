# Customer Microservice

Those instructions are valid for all microservices under this repository.

### Prerequisites
You must pass all steps firstly on this [document](../README.md).

### Database Initialization
Create a database on PostgresSQL UI or from plsql console
```sql
create database burgerzilla_restaurant
```
Initialize ORM models after successfully connected to database
```bash
start db_initialize.bat
```
### Let's run our application
Run the project with this command
```bash
poetry run python run.py
```
