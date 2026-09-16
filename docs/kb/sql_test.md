<!-- kb-agent:source-sha256=0adf2fa2ea28d5c7430ad3e126ffe974c9eade005572ef8c9748767661cdb6f9 -->
# sql_test.sql

This SQL script initializes and seeds a relational database named `BookstoreDB`. It defines the schema for a basic bookstore management system, establishes table relationships and constraints, inserts sample data, and provides diagnostic queries.

---

## Database Initialization

The script performs the following setup steps:
1. **Database Creation**: Creates the database `BookstoreDB` if it does not already exist.
2. **Context Selection**: Switches the active session context to `BookstoreDB`.
3. **Teardown**: Drops existing tables in the correct reverse-dependency order to avoid foreign key constraint violations:
   - `OrderItems`
   - `Orders`
   - `Books`
   - `Customers`

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
Stores the inventory of books available in the bookstore.

| Column Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `BookID` | `INT` | `AUTO_INCREMENT`, `PRIMARY KEY` | Unique identifier for each book. |
| `Title` | `VARCHAR(150)` | `NOT NULL` | Title of the book. |
| `Author` | `VARCHAR(100)` | `NOT NULL` | Author of the book. |
| `Price` | `DECIMAL(10, 2)` | `NOT NULL`, `CHECK (Price >= 0)` | Price of the book (must be non-negative). |
| `StockQuantity` | `INT` | `NOT NULL`, `DEFAULT 0` | Available stock. |

### 3. `Orders` Table
Tracks customer orders.

| Column Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `OrderID` | `INT` | `AUTO_INCREMENT`, `PRIMARY KEY` | Unique identifier for each order. |
| `CustomerID` | `INT` | `NOT NULL` | Foreign key referencing `Customers(CustomerID)`. |
| `OrderDate` | `DATETIME` | `DEFAULT CURRENT_TIMESTAMP` | Timestamp when the order was placed. |
| `TotalAmount` | `DECIMAL(10, 2)` | `NOT NULL` | Total cost of the order. |

* **Foreign Key Constraint**: `CustomerID` references `Customers(CustomerID)` with `ON DELETE CASCADE`. If a customer is deleted, their associated orders are automatically removed.

### 4. `OrderItems` Table
A junction table representing line items within an order.

| Column Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `OrderItemID` | `INT` | `AUTO_INCREMENT`, `PRIMARY KEY` | Unique identifier for each line item. |
| `OrderID` | `INT` | `NOT NULL` | Foreign key referencing `Orders(OrderID)`. |
| `BookID` | `INT` | `NOT NULL` | Foreign key referencing `Books(BookID)`. |
| `Quantity` | `INT` | `NOT NULL`, `CHECK (Quantity > 0)` | Number of copies ordered (must be greater than 0). |
| `Subtotal` | `DECIMAL(10, 2)` | `NOT NULL` | Cost for this line item (Quantity * Price). |

* **Foreign Key Constraints**:
  - `OrderID` references `Orders(OrderID)` with `ON DELETE CASCADE`. If an order is deleted, its line items are automatically removed.
  - `BookID` references `Books(BookID)`.

---

## Seed Data

The script populates the tables with the following initial dataset:

### Customers
* Alice Johnson (`alice.j@example.com`)
* Bob Smith (`bob.smith@example.com`)
* Charlie Brown (`charlie.b@example.com`)

### Books
* *The Pragmatic Programmer* by Andrew Hunt ($45.99, Stock: 12)
* *Clean Code* by Robert C. Martin ($37.50, Stock: 8)
* *AI Application Programmer* by Mayur ($50.00, Stock: 8)
* *Designing Data-Intensive Applications* by Martin Kleppmann ($50.00, Stock: 5)

### Orders & Order Items
Simulates a single transaction where Alice (`CustomerID: 1`) purchases 1 copy of *Clean Code* (`BookID: 2`):
* **Order**: `OrderID: 1`, `CustomerID: 1`, `TotalAmount: 37.50`
* **OrderItem**: `OrderItemID: 1`, `OrderID: 1`, `BookID: 2`, `Quantity: 1`, `Subtotal: 37.50`

---

## Diagnostic Queries

The script includes two built-in queries to verify data state:

### 1. View Available Books
Retrieves the catalog of books with their author, price, and stock levels.
```sql
SELECT Title, Author, Price, StockQuantity 
FROM Books;
```

### 2. View Order Details with Customer Names
Performs an `INNER JOIN` between `Orders` and `Customers` to generate a summary of orders, concatenating the customer's first and last name.
```sql
SELECT 
    o.OrderID,
    CONCAT(c.FirstName, ' ', c.LastName) AS CustomerName,
    o.TotalAmount,
    o.OrderDate
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID;
```
