-- create schema ecommerce;


-- CREATE TABLE users (id INTEGER primary key,
-- name varchar(100) NOT NULL,
-- email varchar(100) UNIQUE,
-- created_at timestamp DEFAULT CURRENT_TIMESTAMP);

-- Create table products(
-- id Integer PRIMARY KEY,
-- product_name varchar(200),
-- price Numeric CHECK(price>0),
-- stock_quantity Numeric CHECK(stock_quantity>=0)
-- )

-- create table orders(
-- id Integer PRIMARY KEY,
-- user_id Integer References users(id),
-- total_amount Numeric CHECK(total_amount>0),
-- order_date Timestamp DEFAULT current_timestamp
-- )

-- create table order_items(
-- id Integer PRIMARY KEY,
-- order_id Integer References orders(id),
-- product_id Integer References products(id),
-- quantity Numeric CHECK(quantity>0)
-- )

-- Alter table order_items alter column id
-- ADD GENERATED ALWAYS AS IDENTITY;

INSERT INTO users (name, email)
VALUES
-- ('Sheik', 'sheik@test.com'),
-- ('Yogesh', 'yogesh@test.com'),
-- ('Bala', 'bala@test.com'),
-- ('Shemo','shemo@test.com'),
-- ('Mohideen','Mohideen@test.com'),
-- ('Nithish','nithish@test.com');
('surya','surya@test.com');
-- INSERT INTO products (product_name, price)
-- VALUES
-- ('Laptop', 70000),
-- ('Phone', 40000),
-- ('Headphones', 5000),
-- ('Mic',200),
-- ('Mouse',400),
-- ('Night Lamp',600),
-- ('Backpack',800);

INSERT INTO orders (user_id, total_amount)
VALUES
(1, 75000),
-- (1, 40000),
(2, 5000),
-- (3, 75000),
(3, 40000);
-- (4, 5000),
-- (5, 75000),
-- (5, 40000),
-- (6, 5000);

-- INSERT INTO order_items (order_id, product_id, quantity)
-- VALUES
-- (1, 1, 1),
-- (1, 3, 1),
-- (2, 2, 1),
-- (3, 3, 1),
-- (2, 1, 1),
-- (3, 3, 1),
-- (3, 1, 1),
-- (4, 2, 1),
-- (4, 5, 1),
-- (5, 4, 1),
-- (6, 4, 1),
-- (6, 4, 1);


-- QUERY 1 Get all users.
SELECT * FROM order_items;
SELECT * FROM products;
SELECT * FROM orders;

-- QUERY 2 Get products whose price > 10000.
SELECT * FROM products where price>10000;

-- QUERY 3 Show:
-- username
-- total order amount
SELECT name,total_amount
from users INNER JOIN orders
ON users.id=orders.user_id;

-- Query 4 Find users who never ordered.
SELECT name 
from users
LEFT JOIN
orders ON
users.id=orders.user_id
where orders.id
IS NULL;

-- QUERY 5 total spending per user
SELECT name,SUM(total_amount) as totalSpending,COUNT(total_amount) as noOfOrders from users
INNER JOIN orders
on users.id=orders.user_id
GROUP by name;

-- QUERY 6 & 7 Find users whose spending > 50000. & Find top 3 spending users.
SELECT name,SUM(total_amount) as totalSpending,COUNT(orders.id) as noOfOrders from users
INNER JOIN orders
on users.id=orders.user_id
GROUP by name
HAVING SUM(total_amount)>50000
ORDER BY SUM(total_amount) DESC
LIMIT 3;


-- QUERY 8 Find most sold product.
SELECT products.product_name,SUM(order_items.quantity) AS totalSold from products 
INNER JOIN order_items
ON products.id=order_items.product_id
GROUP BY product_id,product_name
ORDER BY totalSold DESC
Limit 1;

-- QUERY 9 Find products never purchased.
SELECT products.id,products.product_name from products 
LEFT JOIN order_items
ON products.id=order_items.product_id
where order_items.id is NULL;

-- QUERY 10 Find average order amount per user.
SELECT users.id,users.name,AVG (orders.total_amount) as avg_total_amt from users
INNER JOIN orders
on users.id=orders.user_id
GROUP BY users.id, users.name
ORDER BY avg_total_amt DESC;

-- QUERY 11 Show all products purchased by: Sheik
SELECT users.name,product_name from users
INNER JOIN orders
on users.id=orders.id
INNER JOIN order_items
on orders.id=order_items.order_id
INNER JOIN products
on products.id=order_items.product_id
where users.name='Sheik';












