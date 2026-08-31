# sql_test.sql

This SQL script initializes and configures the relational database schema for a bookstore application (`BookstoreDB`). It handles database creation, table teardown and setup (with constraints and foreign key relationships), seeds sample data, and provides verification queries.

---

## Database Initialization & Teardown

The script performs the following setup steps:
1. **Database Creation**: Creates the database `BookstoreDB` if it does not already exist and sets it as the active database context.
2. **Table Teardown**: Drops existing tables in reverse order of their dependency hierarchy to avoid foreign key constraint violations:
   1. `OrderItems` (Depends on `Orders` and `Books`)
   2. `Orders` (Depends on `Customers`)
   3. `Books`
   4. `Customers`

---

## Database Schema

The schema consists of four tables: `Customers`, `Books`, `Orders`, and `OrderItems`.

### 1. `Customers` Table
Stores customer profile information.

| Column Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `CustomerID` | `INT` | `AUTO_INCREMENT`, `PRIMARY KEY` | Unique identifier for each customer. |
| `FirstName` | `VARCHAR(50)` | `NOT NULL` | Customer's first name. |
| `LastName` | `VARCHAR(50)` | `NOT NULL` | Customer's last name. |
| `Email` | `VARCHAR(100)` | `UNIQUE`, `NOT NULL` | Unique email address. |
| `JoinedDate` | `DATE` | `DEFAULT (CURRENT_DATE)` | Date the customer joined. Defaults to the current date. |

### 2. `Books` Table
Stores inventory details for books.

| Column Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `BookID` | `INT` | `AUTO_INCREMENT`, `PRIMARY KEY` | Unique identifier for each book. |
| `Title` | `VARCHAR(150)` | `NOT NULL` | Title of the book. |
| `Author` | `VARCHAR(100)` | `NOT NULL` | Author of the book. |
| `Price` | `DECIMAL(10, 2)` | `NOT NULL`, `CHECK (Price >= 0)` | Price of the book. Must be non-negative. |
| `StockQuantity`| `INT` | `NOT NULL`, `DEFAULT 0` | Available stock. Defaults to 0. |

### 3. `Orders` Table
Tracks customer orders.

| Column Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `OrderID` | `INT` | `AUTO_INCREMENT`, `PRIMARY KEY` | Unique identifier for each order. |
| `CustomerID` | `INT` | `NOT NULL`, `FOREIGN KEY` | References `Customers(CustomerID)` with `ON DELETE CASCADE`. |
| `OrderDate` | `DATETIME` | `DEFAULT CURRENT_TIMESTAMP` | Timestamp of the order. Defaults to current system time. |
| `TotalAmount` | `DECIMAL(10, 2)`| `NOT NULL` | Total cost of the order. |

### 4. `OrderItems` Table
A junction table representing individual line items within an order.

| Column Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `OrderItemID` | `INT` | `AUTO_INCREMENT`, `PRIMARY KEY` | Unique identifier for each line item. |
| `OrderID` | `INT` | `NOT NULL`, `FOREIGN KEY` | References `Orders(OrderID)` with `ON DELETE CASCADE`. |
| `BookID` | `INT` | `NOT NULL`, `FOREIGN KEY` | References `Books(BookID)`. |
| `Quantity` | `INT` | `NOT NULL`, `CHECK (Quantity > 0)` | Number of copies ordered. Must be greater than 0. |
| `Subtotal` | `DECIMAL(10, 2)`| `NOT NULL` | Total cost for this line item. |

---

## Seed Data

The script populates the database with initial sample records:

* **Customers**:
  * Alice Johnson (`alice.j@example.com`)
  * Bob Smith (`bob.smith@example.com`)
  * Charlie Brown (`charlie.b@example.com`)
* **Books**:
  * *The Pragmatic Programmer* by Andrew Hunt ($45.99, Stock: 12)
  * *Clean Code* by Robert C. Martin ($37.50, Stock: 8)
  * *AI Application Programmer* by Mayur ($50.00, Stock: 8)
  * *Designing Data-Intensive Applications* by Martin Kleppmann ($50.00, Stock: 5)
* **Orders & Order Items**:
  * Simulates an order for Alice (`CustomerID: 1`) purchasing 1 copy of *Clean Code* (`BookID: 2`) for a total of $37.50.

---

## Verification Queries

The script includes two built-in queries to verify data integrity and schema relationships:

### 1. View Available Books
Retrieves basic catalog information for all books in stock.
```sql
SELECT Title, Author, Price, StockQuantity 
FROM Books;
```

### 2. Retrieve Order Details
Performs an `INNER JOIN` between `Orders` and `Customers` to generate a summary of orders, concatenating the customer's first and last names.
```sql
SELECT 
    o.OrderID,
    CONCAT(c.FirstName, ' ', c.LastName) AS CustomerName,
    o.TotalAmount,
    o.OrderDate
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID;
```
