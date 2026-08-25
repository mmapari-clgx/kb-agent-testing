# `sql_test.sql`

This SQL script is designed to set up a test database environment for a bookstore application. It handles the creation of the database, defines the schema for customers, books, and orders, and populates the tables with sample data for testing and development purposes. It also includes example queries for common data retrieval tasks.

## Script Behavior

The script executes in a series of sequential steps:

1.  **Database Creation:** It first creates a database named `BookstoreDB` if one does not already exist. It then sets `BookstoreDB` as the active database for subsequent commands using `USE BookstoreDB;`.
2.  **Table Cleanup:** To ensure a clean, idempotent run, the script drops the `OrderItems`, `Orders`, `Books`, and `Customers` tables if they already exist. The drop order is important to respect foreign key constraints.
3.  **Schema Definition:** It creates the four main tables for the bookstore application: `Customers`, `Books`, `Orders`, and `OrderItems`. It defines columns, data types, primary keys, foreign keys, and other constraints.
4.  **Data Seeding:** The script inserts sample records into the `Customers`, `Books`, `Orders`, and `OrderItems` tables to provide a baseline dataset.
5.  **Example Queries:** The script concludes with two `SELECT` statements that serve as examples for querying the populated database.

## Schema Definition

The script creates the following tables:

### `Customers`

Stores information about individual customers.

| Column | Type | Constraints | Description |
| --- | --- | --- | --- |
| `CustomerID` | `INT` | `AUTO_INCREMENT`, `PRIMARY KEY` | Unique identifier for each customer. |
| `FirstName` | `VARCHAR(50)` | `NOT NULL` | The customer's first name. |
| `LastName` | `VARCHAR(50)` | `NOT NULL` | The customer's last name. |
| `Email` | `VARCHAR(100)` | `UNIQUE`, `NOT NULL` | The customer's unique email address. |
| `JoinedDate` | `DATE` | `DEFAULT (CURRENT_DATE)` | The date the customer registered. Defaults to the current date. |

### `Books`

Stores information about the books available for sale.

| Column | Type | Constraints | Description |
| --- | --- | --- | --- |
| `BookID` | `INT` | `AUTO_INCREMENT`, `PRIMARY KEY` | Unique identifier for each book. |
| `Title` | `VARCHAR(150)` | `NOT NULL` | The title of the book. |
| `Author` | `VARCHAR(100)` | `NOT NULL` | The author of the book. |
| `Price` | `DECIMAL(10, 2)` | `NOT NULL`, `CHECK (Price >= 0)` | The price of the book. Must be non-negative. |
| `StockQuantity` | `INT` | `NOT NULL`, `DEFAULT 0` | The quantity of the book currently in stock. |

### `Orders`

Stores header information for customer orders.

| Column | Type | Constraints | Description |
| --- | --- | --- | --- |
| `OrderID` | `INT` | `AUTO_INCREMENT`, `PRIMARY KEY` | Unique identifier for each order. |
| `CustomerID` | `INT` | `NOT NULL` | Foreign key referencing `Customers.CustomerID`. |
| `OrderDate` | `DATETIME` | `DEFAULT CURRENT_TIMESTAMP` | The timestamp when the order was placed. |
| `TotalAmount` | `DECIMAL(10, 2)` | `NOT NULL` | The total cost of the order. |

**Foreign Keys:**
*   `FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE`: If a customer is deleted, all of their associated orders will also be deleted.

### `OrderItems`

Stores line item details for each order, linking orders to books.

| Column | Type | Constraints | Description |
| --- | --- | --- | --- |
| `OrderItemID` | `INT` | `AUTO_INCREMENT`, `PRIMARY KEY` | Unique identifier for each line item. |
| `OrderID` | `INT` | `NOT NULL` | Foreign key referencing `Orders.OrderID`. |
| `BookID` | `INT` | `NOT NULL` | Foreign key referencing `Books.BookID`. |
| `Quantity` | `INT` | `NOT NULL`, `CHECK (Quantity > 0)` | The number of units of a specific book in the order. Must be greater than zero. |
| `Subtotal` | `DECIMAL(10, 2)` | `NOT NULL` | The total price for this line item (`Price` * `Quantity`). |

**Foreign Keys:**
*   `FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE`: If an order is deleted, all of its associated line items will also be deleted.
*   `FOREIGN KEY (BookID) REFERENCES Books(BookID)`: Links the line item to a specific book.

## Example Queries

The script includes the following sample queries:

*   **View all available books:**
    ```sql
    SELECT Title, Author, Price, StockQuantity FROM Books;
    ```
    This query retrieves the title, author, price, and stock quantity for every book in the `Books` table.

*   **Find order details with customer names:**
    ```sql
    SELECT
        o.OrderID,
        CONCAT(c.FirstName, ' ', c.LastName) AS CustomerName,
        o.TotalAmount,
        o.OrderDate
    FROM Orders o
    JOIN Customers c ON o.CustomerID = c.CustomerID;
    ```
    This query performs an `INNER JOIN` between the `Orders` and `Customers` tables to produce a result set that includes the order ID, the customer's full name, the total amount, and the date of the order.
