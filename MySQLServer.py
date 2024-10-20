from mysql.connector import connect, Error

# Database connection details
try:
    with connect(
        host="localhost",
        user="root",
        password=""
    ) as connection:
        print("Connected to MySQL")
        
        # Create the database if it doesn't exist
        create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
            print("Database 'alx_book_store' created successfully!")

        # Select the database to use
        use_db_query = "USE alx_book_store"
        with connection.cursor() as cursor:
            cursor.execute(use_db_query)

        # Create the tables
        create_tables_query = """
        CREATE TABLE IF NOT EXISTS Authors(
            author_id INT AUTO_INCREMENT PRIMARY KEY,
            author_name VARCHAR(215) NOT NULL
        );
        
        CREATE TABLE IF NOT EXISTS Books(
            book_id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(130) NOT NULL,
            author_id INT,
            price DOUBLE NOT NULL,
            publication_date DATE,
            FOREIGN KEY(author_id) REFERENCES Authors(author_id) ON DELETE CASCADE
        );
        
        CREATE TABLE IF NOT EXISTS Customers(
            customer_id INT AUTO_INCREMENT PRIMARY KEY,
            customer_name VARCHAR(215),
            email VARCHAR(215),
            address TEXT
        );
        
        CREATE TABLE IF NOT EXISTS Orders(
            order_id INT AUTO_INCREMENT PRIMARY KEY,
            customer_id INT,
            order_date DATE NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE
        );
        
        CREATE TABLE IF NOT EXISTS Order_Details(
            orderdetailid INT AUTO_INCREMENT PRIMARY KEY,
            order_id INT,
            book_id INT,
            quantity DOUBLE NOT NULL,
            FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE,
            FOREIGN KEY (book_id) REFERENCES Books(book_id) ON DELETE CASCADE
        );
        """
        
        # Execute table creation queries
        with connection.cursor() as cursor:
            for query in create_tables_query.split(";"):
                if query.strip():  # Avoid executing empty strings
                    cursor.execute(query)
            print("Tables created or already exist.")

except Error as e:
    print(f"Error: {e}")

# Connection will be automatically closed when 'with' block ends.
