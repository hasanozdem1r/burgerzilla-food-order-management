
# Food Order Management with Microservices

This project aim to create bridge between customer and restaurant owners. 

Customers and restaurant owners can run their own operations based on products 

I decided to provide solutions with microservices approach regarding to suitability

## 1.Prerequisites
1. Python 3.9 
2. [Poetry](https://python-poetry.org/)  for dependency management
3. PostgresSQL Local Server
4. PyCharm / Visual Studio Code

## 2.Installation

I used Poetry for virtual environment because it's easier to use and manage the dependencies.

In this section I will be providing installations about prerequisites. 

1. [Python 3.9](https://python.org/)
2. [Python Poetry](https://python-poetry.org/docs/)
3. [PostgresSQL](https://www.postgresql.org/)
4. [Pycharm](https://www.jetbrains.com/pycharm/) & [Visual Studio Code](https://code.visualstudio.com/)

**NOTE** : You can freely click the item which you need to install then you will be redirected official installation docs

## 3.Features
Please follow the links for further reading about current microservices
- [Customer Microservice](1_customer_service/README.md)
- [Order Microservice](2_order_service/README.md)
- [Restaurant Microservice](3_restaurant_service/README.md)

## 4.API Reference
Please follow the link for further reading about [API's reference](4_project_docs/burgerzilla_api_reference.md)

## 5.Tech Stack
**Language:** Python 3.9 

**Database Server:** PostgresSQL

**Libraries** : Please follow the [link](4_project_docs/burgerzilla_libraries_reference.md) for furher details.


## 6.Burgerzilla Architecture
![](4_project_docs/images/burgerzilla_architectrue.jpg)


## 7.Environment Variables

To run this project, you will need to add the following environment variables to your environment variables file

`POSTGRES_HOST`, `POSTGRES_PORT`,`POSTGRES_USER`,  `POSTGRES_PWD`








## License

[Massachusetts Institute of Technology](https://choosealicense.com/licenses/mit/)

`