# BurgerZilla Project Database Schema
![](images/burgerzilla_db_schema.jpg)

With this document, it is aimed to make database and ORM developments easier in the future.

I will be providing information about table relationships and for each table fields and constrains

### Table Relationships

1. Between Customers & Orders Table
   - One-to-Many Relationship
   - One c_id can have one or more o_id
   - One o_id can have only one c_id
   <br><br>
2. Between Orders & Order_Details 
   - One-to-Many Relationship (Orders -> Order_Details)
   - One o_id on Orders can have one or more o_id on OrderDetails 
   - One or more o_id on OrderDetails can have only one o_id on Orders
   <br><br>
3. Between Order_Details & Products
   - Many-to-Many Relationship
   - One or more item_id on OrderDetails can have one or more item_id on Products
   - One or more item_id on Products can have one or more item_id on OrderDetails
   
4. Between Restaurants & Products
   - One-to-Many Relationship
   - One r_id can have one or more p_id
   - One p_id can have only one s_id
   <br><br>
5.Between Restaurant_Owners and Restaurants 
   - One-to-Many Relationship
   - One r_o_id can have one or more r_id
   - One r_id can have only one r_o_id

   
### Footnotes
1. I decided to create one-to-many relationship between Restaurant_Owners and Restaurants because of franchise situation can occur one day and system still will work efficiently for this scenario

### Key Takeaways
1. This type of order management system requires all of your transactions to have strong consistency.
2. Strong consistency refers to all access to your restaurant’s inventory being processed sequentially and read from the same state in your restaurant’s inventory system.

### Acknowledgements

 - [ResearchGate | Order Placement System](https://www.researchgate.net/publication/323230406_An_Android-based_Order_Placement_System_for_Restaurants)
 - [Princeton EDU | E-Commerce Database Design](https://www.princeton.edu/~rcurtis/ultradev/ecommdatabase.html)
 - [StackOverflow | Design Thinking](https://stackoverflow.com/)

### Database Design is not fun, how I've done it :)
 - [Ano Vidovic - Austrias](https://www.youtube.com/watch?v=inBKFMB-yPg)
 - [Erkan Oğur - Gnossienne No. 1](https://www.youtube.com/watch?v=53iLc9NRtYs)
 - [Руки Вверх! - 18 мне уже](https://www.youtube.com/watch?v=Hxab_Sr132o)
