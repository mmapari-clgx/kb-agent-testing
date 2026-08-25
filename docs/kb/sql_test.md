# `sql_test.sql`

This SQL script is designed to set up a test database environment for a bookstore application. It handles the creation of the database, defines the schema for customers, books, and orders, and populates the tables with sample data for testing and development purposes. It also includes example queries for common data retrieval operations.

## Execution Flow

The script executes in a series of sequential steps:

1.  **Database Creation:** It first creates a database named `BookstoreDB` if one does not already exist, and then selects it for use with the `USE BookstoreDB;` command.
2.  **Table Cleanup:** To ensure a clean slate on every run, the script drops the `OrderItems`, `Orders`, `Books`, and `Customers` tables if they exist. The tables are dropped in reverse order of their dependency to avoid foreign key constraint errors.
3.  **Schema Definition:** It creates the four primary tables (`Customers`, `Books`, `Orders`, `OrderItems`) with their respective columns, data types, constraints, and relationships.
4.  **Data Seeding:** Sample data is inserted into the `Customers`, `Books`, `Orders`, and `OrderItems` tables to simulate a live environment.
5.  **Example Queries:** The script concludes with a set of `SELECT` statements that serve as examples for querying the database.

## Schema Definition

The script defines the following tables:

### `Customers`

Stores information about individual customers.

| Column | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `CustomerID` | `INT` | `AUTO_INCREMENT`, `PRIMARY KEY` | Unique identifier for each customer. |
| `FirstName` | `VARCHAR(50)` | `NOT NULL` | The customer's first name. |
| `LastName` | `VARCHAR(50)` | `NOT NULL` | The customer's last name. |
| `Email` | `VARCHAR(100)` | `UNIQUE`, `NOT NULL` | The customer's unique email address. |
| `JoinedDate` | `DATE` | `DEFAULT (CURRENT_DATE)` | The date the customer registered, defaults to the current date. |

### `Books`

Stores information about the books available for sale.

| Column | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `BookID` | `INT` | `AUTO_INCREMENT`, `PRIMARY KEY` | Unique identifier for each book. |
| `Title` | `VARCHAR(150)` | `NOT NULL` | The title of the book. |
| `Author` | `VARCHAR(100)` | `NOT NULL` | The author of the book. |
| `Price` | `DECIMAL(10, 2)` | `NOT NULL`, `CHECK (Price >= 0)` | The price of the book. Must be non-negative. |
| `StockQuantity` | `INT` | `NOT NULL`, `DEFAULT 0` | The quantity of the book currently in stock. |

### `Orders`

Stores header information for customer orders.

| Column | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `OrderID` | `INT` | `AUTO_INCREMENT`, `PRIMARY KEY` | Unique identifier for each order. |
| `CustomerID` | `INT` | `NOT NULL`, `FOREIGN KEY` | References `Customers(CustomerID)`. If a customer is deleted, their orders are also deleted (`ON DELETE CASCADE`). |
| `OrderDate` | `DATETIME` | `DEFAULT CURRENT_TIMESTAMP` | The timestamp when the order was placed. |
| `TotalAmount` | `DECIMAL(10, 2)` | `NOT NULL` | The total cost of the order. |

### `OrderItems`

Stores line item details for each order.

| Column | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `OrderItemID` | `INT` | `AUTO_INCREMENT`, `PRIMARY KEY` | Unique identifier for each line item in an order. |
| `OrderID` | `INT` | `NOT NULL`, `FOREIGN KEY` | References `Orders(OrderID)`. If an order is deleted, its line items are also deleted (`ON DELETE CASCADE`). |
| `BookID` | `INT` | `NOT NULL`, `FOREIGN KEY` | References `Books(BookID)`. |
| `Quantity` | `INT` | `NOT NULL`, `CHECK (Quantity > 0)` | The number of units of a specific book in the order. Must be greater than zero. |
| `Subtotal` | `DECIMAL(10, 2)` | `NOT NULL` | The total price for this line item (`Price` * `Quantity`). |

## Sample Data

The script inserts the following initial data:

*   **Customers:** Three sample customers ('Alice Johnson', 'Bob Smith', 'Charlie Brown').
*   **Books:** Three sample books ('The Pragmatic Programmer', 'Clean Code', 'Designing Data-Intensive Applications').
*   **Orders & OrderItems:** A single order is created for customer 'Alice Johnson' (`CustomerID: 1`) for one copy of 'Clean Code' (`BookID: 2`).

## Example Queries

The file includes two example queries to demonstrate data retrieval:

1.  **View All Available Books:**
    ```sql
    SELECT Title, Author, Price, StockQuantity FROM Books;
    ```
    This query retrieves the title, author, price, and stock quantity for every book in the `Books` table.

2.  **Find Order Details with Customer Names:**
    ```sql
    SELECT
        o.OrderID,
        CONCAT(c.FirstName, ' ', c.LastName) AS CustomerName,
        o.TotalAmount,
        o.OrderDate
    FROM Orders o
    JOIN Customers c ON o.CustomerID = c.CustomerID;
    ```
    This query uses an `INNER JOIN` to combine data from the `Orders` and `Customers` tables, showing the order ID, the customer's full name, the total amount, and the date for each order.
