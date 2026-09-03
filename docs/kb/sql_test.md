<!-- kb-agent:source-sha256=0adf2fa2ea28d5c7430ad3e126ffe974c9eade005572ef8c9748767661cdb6f9 -->
# sql_test.sql

This SQL script initializes and configures the database schema for a relational bookstore database named `BookstoreDB`. It handles database creation, table setup with relational constraints, seed data insertion, and basic reporting queries.

---

## Database Initialization

The script performs the following setup steps:
1. **Database Creation**: Creates the database `BookstoreDB` if it does not already exist and sets it as the active database context.
2. **Cleanup**: Drops existing tables in the reverse order of their dependency hierarchy (`OrderItems` $\rightarrow$ `Orders` $\rightarrow$ `Books` $\rightarrow$ `Customers`) to prevent foreign key constraint violations during re-runs.

---

## Schema Definition

The database consists of four tables: `Customers`, `Books`, `Orders`, and `OrderItems`.

### 1. `Customers` Table
Stores customer profile information.

| Column Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `CustomerID` | `INT` | `AUTO_INCREMENT`, `PRIMARY KEY` | Unique identifier for each customer. |
| `FirstName` | `VARCHAR(50)` | `NOT NULL` | Customer's first name. |
| `LastName` | `VARCHAR(50)` | `NOT NULL` | Customer's last name. |
| `Email` | `VARCHAR(100)` | `UNIQUE`, `NOT NULL` | Unique email address. |
| `JoinedDate` | `DATE` | `DEFAULT (CURRENT_DATE)` | Date the customer joined. |

### 2. `Books` Table
Stores inventory details for books.

| Column Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `BookID` | `INT` | `AUTO_INCREMENT`, `PRIMARY KEY` | Unique identifier for each book. |
| `Title` | `VARCHAR(150)` | `NOT NULL` | Title of the book. |
| `Author` | `VARCHAR(100)` | `NOT NULL` | Author of the book. |
| `Price` | `DECIMAL(10, 2)` | `NOT NULL`, `CHECK (Price >= 0)` | Retail price (must be non-negative). |
| `StockQuantity`| `INT` | `NOT NULL`, `DEFAULT 0` | Available stock. |

### 3. `Orders` Table
Tracks customer orders.

| Column Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `OrderID` | `INT` | `AUTO_INCREMENT`, `PRIMARY KEY` | Unique identifier for each order. |
| `CustomerID` | `INT` | `NOT NULL` | Foreign key referencing `Customers(CustomerID)`. |
| `OrderDate` | `DATETIME` | `DEFAULT CURRENT_TIMESTAMP` | Timestamp of the order. |
| `TotalAmount` | `DECIMAL(10, 2)`| `NOT NULL` | Total monetary value of the order. |

* **Foreign Key Constraint**: `CustomerID` references `Customers(CustomerID)` with `ON DELETE CASCADE`. If a customer is deleted, their associated orders are automatically removed.

### 4. `OrderItems` Table
A junction table representing line items within an order.

| Column Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `OrderItemID` | `INT` | `AUTO_INCREMENT`, `PRIMARY KEY` | Unique identifier for each line item. |
| `OrderID` | `INT` | `NOT NULL` | Foreign key referencing `Orders(OrderID)`. |
| `BookID` | `INT` | `NOT NULL` | Foreign key referencing `Books(BookID)`. |
| `Quantity` | `INT` | `NOT NULL`, `CHECK (Quantity > 0)` | Number of copies ordered (must be greater than 0). |
| `Subtotal` | `DECIMAL(10, 2)`| `NOT NULL` | Total cost for this line item. |

* **Foreign Key Constraints**:
  * `OrderID` references `Orders(OrderID)` with `ON DELETE CASCADE`.
  * `BookID` references `Books(BookID)`.

---

## Seed Data

The script populates the tables with initial sample data:

* **Customers**: Inserts 3 records:
  * Alice Johnson (`alice.j@example.com`)
  * Bob Smith (`bob.smith@example.com`)
  * Charlie Brown (`charlie.b@example.com`)
* **Books**: Inserts 4 records:
  * *The Pragmatic Programmer* by Andrew Hunt ($45.99, Stock: 12)
  * *Clean Code* by Robert C. Martin ($37.50, Stock: 8)
  * *AI Application Programmer* by Mayur ($50.00, Stock: 8)
  * *Designing Data-Intensive Applications* by Martin Kleppmann ($50.00, Stock: 5)
* **Orders & OrderItems**: Simulates a single purchase where Alice Johnson (CustomerID: 1) buys 1 copy of *Clean Code* (BookID: 2) for a total of $37.50.

---

## Verification Queries

The script includes two queries to verify schema creation and data integrity:

1. **View Available Books**:
   Retrieves the title, author, price, and stock quantity for all books in the inventory.
   ```sql
   SELECT Title, Author, Price, StockQuantity 
   FROM Books;
   ```

2. **Retrieve Order Details**:
   Performs an `INNER JOIN` between `Orders` and `Customers` to display order IDs, concatenated customer full names, order totals, and order dates.
   ```sql
   SELECT 
       o.OrderID,
       CONCAT(c.FirstName, ' ', c.LastName) AS CustomerName,
       o.TotalAmount,
       o.OrderDate
   FROM Orders o
   JOIN Customers c ON o.CustomerID = c.CustomerID;
   ```
