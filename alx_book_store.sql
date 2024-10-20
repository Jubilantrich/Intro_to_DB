CREATE DATABASE IF NOT EXISTS alx_book_store;

USE alx_book_store;

-- author table

CREATE TABLE Authors(
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(215) NOT NULL
);


--create the books table
CREATE TABLE Books( 
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR (130) NOT NULL,
    author_id INT,
    price DOUBLE NOT NULL,
    publication_date DATE,
    FOREIGN KEY(author_id) REFERENCES Authors(author_id) on DELETE CASCADE

);

--create customer table
CREATE TABLE customers(
    customer_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    customer_nane VARCHAR(215),
    email VARCHAR(215),
    address TEXT

):

--create the orders table

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES (customer_id) ON DELETE CASCADE

);

CREATE TABLE Order_Details(
    orderdatailid INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    book_id INT,
    quantity DOUBLE NOT NULL,
    FOREIGN KEY (order_id) REFERENCES (order_id) ON DELETE CASCADE
    FOREIGN KEY (book_id) REFERENCES (book_id) ON DELETE CASCADE
);
