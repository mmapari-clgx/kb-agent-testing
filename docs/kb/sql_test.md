# sql_test.sql

This SQL script initializes and seeds a relational database schema for a bookstore application (`BookstoreDB`). It sets up the database, defines tables with constraints and foreign key relationships, inserts sample data, and provides verification queries.

---

## Database Initialization

The script performs the following setup steps:
1. **Database Creation**: Creates the database `BookstoreDB` if it does not already exist.
2. **Context Selection**: Switches the active session context to `BookstoreDB`.
3. **Cleanup**: Drops existing tables in reverse dependency order to prevent foreign key constraint violations during re-runs:
   - `OrderItems`
   - `Orders`
   - `Books`
   - `Customers`

---

## Schema Definition

The schema consists of four tables: `Customers`, `Books`, `Orders`, and `OrderItems`.

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
| `Price` | `DECIMAL(10, 2)`| `NOT NULL`, `CHECK (Price >= 0)` | Retail price (must be non-negative). |
| `StockQuantity`| `INT` | `NOT NULL`, `DEFAULT 0` | Number of copies in stock. |

### 3. `Orders` Table
Tracks customer orders.

| Column Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `OrderID` | `INT` | `AUTO_INCREMENT`, `PRIMARY KEY` | Unique identifier for each order. |
| `CustomerID` | `INT` | `NOT NULL`, `FOREIGN KEY` | References `Customers(CustomerID)` with `ON DELETE CASCADE`. |
| `OrderDate` | `DATETIME` | `DEFAULT CURRENT_TIMESTAMP` | Timestamp when the order was placed. |
| `TotalAmount` | `DECIMAL(10, 2)`| `NOT NULL` | Total cost of the order. |

### 4. `OrderItems` Table
A junction table representing line items within an order.

| Column Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `OrderItemID` | `INT` | `AUTO_INCREMENT`, `PRIMARY KEY` | Unique identifier for each line item. |
| `OrderID` | `INT` | `NOT NULL`, `FOREIGN KEY` | References `Orders(OrderID)` with `ON DELETE CASCADE`. |
| `BookID` | `INT` | `NOT NULL`, `FOREIGN KEY` | References `Books(BookID)`. |
| `Quantity` | `INT` | `NOT NULL`, `CHECK (Quantity > 0)` | Number of copies ordered (must be greater than 0). |
| `Subtotal` | `DECIMAL(10, 2)`| `NOT NULL` | Cost for this specific line item. |

---

## Seed Data

The script populates the tables with initial sample data:

* **Customers**:
  - Alice Johnson (`alice.j@example.com`)
  - Bob Smith (`bob.smith@example.com`)
  - Charlie Brown (`charlie.b@example.com`)
* **Books**:
  - *The Pragmatic Programmer* by Andrew Hunt ($45.99, Stock: 12)
  - *Clean Code* by Robert C. Martin ($37.50, Stock: 8)
  - *Designing Data-Intensive Applications* by Martin Kleppmann ($50.00, Stock: 5)
* **Orders & Order Items**:
  - Simulates an order placed by Alice (`CustomerID: 1`) purchasing 1 copy of *Clean Code* (`BookID: 2`) for a total of $37.50.

---

## Verification Queries

The script includes two queries to verify the schema and data:

1. **View Available Books**:
   Retrieves the title, author, price, and stock quantity for all records in the `Books` table.
   ```sql
   SELECT Title, Author, Price, StockQuantity 
   FROM Books;
   ```

2. **Retrieve Order Details**:
   Performs an `INNER JOIN` between `Orders` and `Customers` to return order IDs, concatenated customer full names, total amounts, and order dates.
   ```sql
   SELECT 
       o.OrderID,
       CONCAT(c.FirstName, ' ', c.LastName) AS CustomerName,
       o.TotalAmount,
       o.OrderDate
   FROM Orders o
   JOIN Customers c ON o.CustomerID = c.CustomerID;
   ```
