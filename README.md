`
![Burgerzilla Cover Photo](4_project_docs/images/burgerzilla_cover_photo.png)
# BurgerZilla (Yemeksepeti & Patika.dev)

This microservice aims to manage customer orders from hamburger restaurants.
I provide this solution with microservice architecture under the limitation of REST-API


## Installation

I used Poetry for virtual environment because it's easier to use and manage the dependencies.

Those instructions valid for every microservice
Firstly initialize models on PostgresSQL 
```bash
flask db init
flask db migrate
flask db upgrade
``` 
Run microservices
```bash
poetry run python run.py
```     

## Features

- Customer Order Management [CRUD]
- Restaurant Order Management [CRUD]

## API Reference
Redirect to burgerzilla_api_ref.md file

## Tech Stack
**Language:** Python 3.9 

**Database Server:** PostgresSQL

**Libraries used during project** : Please follow the [link](4_project_docs/burgerzilla_libraries_reference.md)


## Lessons Learned

What did you learn while building this project? 

1. My awareness of microservice increased.
2. I get used to more features of Poetry



## Burgerzilla Architecture
![](4_project_docs/images/burgerzilla_architectrue.jpg)

**NOTE** : I knew normally for this project also webhook and load balancer is mandatory, unfortunately I had no time for it.

## Project Management

| ID  | Title                     | Status     |
|:---:|:--------------------------|:-----------|
|  1  | Project Started           | 01/29/2022 |
|  2  | Project Delivery Date     | 02/13/2022 |
|  3  | Total time I worked on it | 30 hours   |


## Project Evaluation

| ID  | Task               | Status |
|:---:|:-------------------|:-------|
|  1  | Project Structure  | OK     |
|  2  | PEP Standards      | OK     |
|  3  | Typing             | OK     |
|  4  | Testing            | NONE   |
|  5  | Documentation      | OK     |
|  6  | Dockerization      | NONE   |
|  7  | RabbitMQ Queue     | NONE   |
|  8  | JWT Implementation | NONE   |

## License

[Massachusetts Institute of Technology](https://choosealicense.com/licenses/mit/)

`