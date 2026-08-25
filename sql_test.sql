-- Step 1: Create and select the database
CREATE DATABASE IF NOT EXISTS BookstoreDB;
USE BookstoreDB;

-- Step 2: Drop existing tables if re-running the script
DROP TABLE IF EXISTS OrderItems;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Books;
DROP TABLE IF EXISTS Customers;

-- Step 3: Create tables with constraints and relationships

CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    JoinedDate DATE DEFAULT (CURRENT_DATE)
);

CREATE TABLE Books (
    BookID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(150) NOT NULL,
    Author VARCHAR(100) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0),
    StockQuantity INT NOT NULL DEFAULT 0
);

CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT NOT NULL,
    OrderDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    TotalAmount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

CREATE TABLE OrderItems (
    OrderItemID INT AUTO_INCREMENT PRIMARY KEY,
    OrderID INT NOT NULL,
    BookID INT NOT NULL,
    Quantity INT NOT NULL CHECK (Quantity > 0),
    Subtotal DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (BookID) REFERENCES Books(BookID)
);

-- Step 4: Insert sample data

INSERT INTO Customers (FirstName, LastName, Email) VALUES 
('Alice', 'Johnson', 'alice.j@example.com'),
('Bob', 'Smith', 'bob.smith@example.com'),
('Charlie', 'Brown', 'charlie.b@example.com');

INSERT INTO Books (Title, Author, Price, StockQuantity) VALUES 
('The Pragmatic Programmer', 'Andrew Hunt', 45.99, 12),
('Clean Code', 'Robert C. Martin', 37.50, 8),
('Designing Data-Intensive Applications', 'Martin Kleppmann', 50.00, 5);

-- Simulate an order for Alice (CustomerID: 1) buying 1 copy of "Clean Code"
INSERT INTO Orders (CustomerID, TotalAmount) VALUES (1, 37.50);
-- Assuming OrderID generated is 1
INSERT INTO OrderItems (OrderID, BookID, Quantity, Subtotal) VALUES (1, 2, 1, 37.50);

-- Step 5: Useful queries

-- View all available books
SELECT Title, Author, Price, StockQuantity 
FROM Books;

-- Find order details with customer names using an INNER JOIN
SELECT 
    o.OrderID,
    CONCAT(c.FirstName, ' ', c.LastName) AS CustomerName,
    o.TotalAmount,
    o.OrderDate
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID;
