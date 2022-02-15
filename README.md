`
# Food Order Management with Microservices

This project aim to create bridge between customer and restaurant owners. 

Customers and restaurant owners can run their own operations based on products 

I decided to provide solutions with microservices approach regarding to suitability

## Prerequisites
1. Python 3.9 
2. [Poetry](https://python-poetry.org/)  for dependency management
3. PostgresSQL Local Server
4. PyCharm / Visual Studio Code

## Installation

I used Poetry for virtual environment because it's easier to use and manage the dependencies.

In this section I will be providing installations about prerequisites. 
1. [Python 3.9](https://python.org/)
2. [Python Poetry](https://python-poetry.org/docs/)
3. [PostgresSQL](https://www.postgresql.org/)
4. [Pycharm](https://www.jetbrains.com/pycharm/) & [Visual Studio Code](https://code.visualstudio.com/)


## Features
Please follow the links for further reading about microservices
- [Customer Microservice](1_customer_service/README.md)
- [Order Microservice](2_order_service/README.md)
- [Restaurant Microservice](3_restaurant_service/README.md)

## API Reference
Please follow the link for further reading about [API's reference](4_project_docs/burgerzilla_api_reference.md)


## Tech Stack
**Language:** Python 3.9 

**Database Server:** PostgresSQL

**Libraries** : Please follow the [link](4_project_docs/burgerzilla_libraries_reference.md) for details.



## Lessons Learned

1. What did you learn while building this project? 
    * I get used to more to Poetry
    * I increased my know how about relational databases for big projects


2. What challenges did you face and how did you overcome them?
   * My biggest challenge was about microservices. I knew definition, but I had no experience on it.
   * As a solution full one week I've done reading on microservices.io then I connected with Chris Richardson via Linkedin and find out answers for my question.
   * Finally, after 1 week I was able to design my architecture and database diagram
   

## Burgerzilla Architecture
![](4_project_docs/images/burgerzilla_architectrue.jpg)


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
|  9  | Flake8 Lint Format | OK     |



## License

[Massachusetts Institute of Technology](https://choosealicense.com/licenses/mit/)

`