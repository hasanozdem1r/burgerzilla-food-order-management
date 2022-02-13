
# BurgerZilla REST API Documentation

### Current APIs
1. Customer-API
2. Order-API
3. Restaurant-API


## Customer-API-Reference

#### Get all customers
```http
  GET http://0.0.0.0:5001/burgerzilla/v1/customers
```
#### Get all orders based on customer id (This method use Order-API)
```http
  GET http://0.0.0.0:5001/burgerzilla-customer/1.0.0/orders?customer-id=1
```
#### Create a new customer

```http
  Reference to routes.py
```

## Order-API Reference


####  Get all orders based on customer-id (actual endpoint)
```http
  GET localhost:5002/burgerzilla-order/1.0.0/orders?customer-id
```


####  Get all orders based on customer-id and order-id
```http
  GET localhost:5002/burgerzilla-order/1.0.0/order?customer-id&order-id
```

#### Create a new order
```http
  POST http://0.0.0.0:5001/burgerzilla-order/1.0.0/order
```
Form data
```json
  {
  "o-id":[
    {
       "o-d-id":1,
       "o-id":32,
       "p-id":1,
       "o-quantity":2,
       "order-price":2
    },
    {
       "o-d-id":1,
       "o-id":1,
       "p-id":1,
       "o-quantity":2,
       "order-price":2
    },
    {
       "o-d-id":1,
       "o-id":1,
       "p-id":1,
       "o-quantity":2,
       "order-price":2
    }
  ],

  "c-id": 1,
  "o-address": "Metro City",
  "o-city": "2016",
  "o-postal-code": "12",
  "o-status":"OK",
  "o-phone-number":"123456",
  "o-date":"12/02/02"
}
```