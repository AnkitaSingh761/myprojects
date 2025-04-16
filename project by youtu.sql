CREATE DATABASE cust;

use cust;


CREATE  TABLE Books(
     Book_ID SERIAL PRIMARY KEY,
	Title VARCHAR(100),
    Author VARCHAR(100),
    Genre VARCHAR(100),
    Published_Year INT,
    Price  NUMERIC(10,2),
    Stock int
);

CREATE TABLE Customers(
       Customer_ID	SERIAL 	PRIMARY KEY,
       Name	VARCHAR(100),	
       Email VARCHAR(100),	
	   Phone VARCHAR(15),	
       City	VARCHAR(50),	
       Country	VARCHAR(150)
       );
       
       
CREATE TABLE Orders(
      Order_ID	SERIAL	PRIMARY KEY,
      Customer_ID	INT	REFERENCES Customers(Customer_ID),
       Book_ID	INT REFERENCES Books(Book_ID),	
       Order_Date DATE,		
      Quantity	INT,
      Total_Amount	 NUMERIC(10,2)
      );
      
      

SELECT * FROM Books;

SELECT * FROM Customers;

SELECT * FROM Orders;



SELECT * FROM Books
WHERE Genre = "Fiction";


-- Find books published after the year 1950:
SELECT * FROM Books
WHERE Published_Year > 1950;


-- List all the customers from the canada:
SELECT * FROM Customers
WHERE Country = "Canada";


-- Show orders placed in november 2023:
SELECT * FROM Orders
WHERE Order_Date BETWEEN "2023-11-01" AND "2023-11-30";


-- Retrieve the total stock of books available:
SELECT SUM(Stock) AS Total_stock
FROM Books;


-- Find the details of the most expensive book:
SELECT MAX(Price)
FROM Books;

SELECT * FROM Books 
ORDER BY Price DESC
LIMIT 1;


-- Show all customers who ordered more than 1 quantity of a book:
SELECT * FROM Orders
WHERE Quantity > 1;


-- Retrieve all orders where the total amount exceeds $20:
SELECT * FROM Orders
WHERE Total_Amount > 20;


-- List all genre available in the books table:
SELECT DISTINCT(Genre)
FROM Books;


-- Find the book with the lowest stock:
SELECT * FROM Books
ORDER BY Stock ASC
LIMIT 1;


-- Calculate the total revenue generated from all orders:
SELECT SUM(Total_Amount) AS Revenue
 FROM Orders;
 
 
 
 -- Retrieve the total number of books sold for each genre:
 SELECT b.Genre, SUM(o.Quantity) AS total_book_sold
 FROM Orders o
 JOIN Books b 
 ON o.book_id = b.book_id
 GROUP BY b.Genre;
 
 
 
 -- Find the average price of books in the 'Fantasy' genre:
 SELECT  AVG(Price) as avg_price
 FROM Books
 WHERE Genre = "Fantasy";

 
 -- List customers who have placed at least 2 orders:
 SELECT customer_id, COUNT(order_id) AS Order_count
 FROM Orders
 GROUP BY customer_id
 HAVING COUNT(order_id) >= 2;
 
 

    









