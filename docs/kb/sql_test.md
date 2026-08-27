# sql_test.sql

This SQL script initializes and configures the database schema for a bookstore application (`BookstoreDB`). It handles database creation, table teardown and setup, constraint definitions, sample data insertion, and basic reporting queries.

---

## Database Initialization and Cleanup

The script performs the following setup steps:
1. **Database Creation**: Creates the database `BookstoreDB` if it does not already exist and sets it as the active database context.
2. **Teardown**: Drops existing tables in reverse dependency order to avoid foreign key constraint violations:
   * `OrderItems`
   * `Orders`
   * `Books`
   * `Customers`

---

## Schema Definition

The schema consists of four tables with defined relationships, primary keys, auto-incrementing identifiers, and data integrity constraints.

### 1. `Customers` Table
Stores customer profile information.

| Column Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `CustomerID` | `INT` | `PRIMARY KEY`, `AUTO_INCREMENT` | Unique identifier for each customer. |
| `FirstName` | `VARCHAR(50)` | `NOT NULL` | Customer's first name. |
| `LastName` | `VARCHAR(50)` | `NOT NULL` | Customer's last name. |
| `Email` | `VARCHAR(100)` | `UNIQUE`, `NOT NULL` | Unique email address. |
| `JoinedDate` | `DATE` | `DEFAULT (CURRENT_DATE)` | Date the customer joined. Defaults to the current date. |

### 2. `Books` Table
Stores inventory details for books.

| Column Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `BookID` | `INT` | `PRIMARY KEY`, `AUTO_INCREMENT` | Unique identifier for each book. |
| `Title` | `VARCHAR(150)` | `NOT NULL` | Book title. |
| `Author` | `VARCHAR(100)` | `NOT NULL` | Book author. |
| `Price` | `DECIMAL(10, 2)` | `NOT NULL`, `CHECK (Price >= 0)` | Book price. Must be non-negative. |
| `StockQuantity` | `INT` | `NOT NULL`, `DEFAULT 0` | Available stock. Defaults to 0. |

### 3. `Orders` Table
Tracks customer orders.

| Column Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `OrderID` | `INT` | `PRIMARY KEY`, `AUTO_INCREMENT` | Unique identifier for each order. |
| `CustomerID` | `INT` | `NOT NULL`, `FOREIGN KEY` | References `Customers(CustomerID)`. |
| `OrderDate` | `DATETIME` | `DEFAULT CURRENT_TIMESTAMP` | Timestamp of the order. Defaults to the current date and time. |
| `TotalAmount` | `DECIMAL(10, 2)` | `NOT NULL` | Total cost of the order. |

* **Foreign Key Constraint**: `CustomerID` references `Customers(CustomerID)` with `ON DELETE CASCADE`. If a customer is deleted, their associated orders are automatically removed.

### 4. `OrderItems` Table
Stores line-item details for each order, linking orders to books.

| Column Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `OrderItemID` | `INT` | `PRIMARY KEY`, `AUTO_INCREMENT` | Unique identifier for each line item. |
| `OrderID` | `INT` | `NOT NULL`, `FOREIGN KEY` | References `Orders(OrderID)`. |
| `BookID` | `INT` | `NOT NULL`, `FOREIGN KEY` | References `Books(BookID)`. |
| `Quantity` | `INT` | `NOT NULL`, `CHECK (Quantity > 0)` | Number of copies ordered. Must be greater than 0. |
| `Subtotal` | `DECIMAL(10, 2)` | `NOT NULL` | Subtotal for the line item. |

* **Foreign Key Constraints**:
  * `OrderID` references `Orders(OrderID)` with `ON DELETE CASCADE`. If an order is deleted, its line items are automatically removed.
  * `BookID` references `Books(BookID)`. This prevents deleting a book if it is referenced by an existing order item.

---

## Sample Data

The script populates the tables with initial sample data to simulate a real-world scenario:

1. **Customers**: Inserts three records:
   * Alice Johnson (`alice.j@example.com`)
   * Bob Smith (`bob.smith@example.com`)
   * Charlie Brown (`charlie.b@example.com`)
2. **Books**: Inserts three records:
   * *The Pragmatic Programmer* by Andrew Hunt ($45.99, Stock: 12)
   * *Clean Code* by Robert C. Martin ($37.50, Stock: 8)
   * *Designing Data-Intensive Applications* by Martin Kleppmann ($50.00, Stock: 5)
3. **Orders & Order Items**: Simulates a single order where Alice Johnson (`CustomerID: 1`) purchases 1 copy of *Clean Code* (`BookID: 2`) for a total of $37.50.

---

## Verification Queries

The script includes two queries to verify the schema and data:

### 1. View Available Books
Retrieves the title, author, price, and stock quantity of all books in the inventory.
```sql
SELECT Title, Author, Price, StockQuantity 
FROM Books;
```

### 2. Retrieve Order Details with Customer Names
Performs an `INNER JOIN` between `Orders` and `Customers` to retrieve order details, concatenating the customer's first and last name into a single `CustomerName` field.
```sql
SELECT 
    o.OrderID,
    CONCAT(c.FirstName, ' ', c.LastName) AS CustomerName,
    o.TotalAmount,
    o.OrderDate
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID;
```
