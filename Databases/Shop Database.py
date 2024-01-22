import sqlite3

# Connect to the SQLite database (this will create the database if it doesn't exist)
conn = sqlite3.connect('shop.db')
cursor = conn.cursor()

# Create the 'customer' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS customer (
        customer_id INTEGER PRIMARY KEY,
        customer_name TEXT,
        address TEXT
    );
''')

# Create the 'product' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS product (
        product_number INTEGER PRIMARY KEY,
        product_name TEXT,
        price INTEGER
    );
''')

# Create the 'order' table
# Note: 'order' is a reserved keyword in SQL, so it's better to use a different name for the table (e.g., 'order_table')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS order_table (
        order_number INTEGER PRIMARY KEY,
        customer_id INTEGER,
        product_number INTEGER,
        quantity INTEGER,
        FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
        FOREIGN KEY (product_number) REFERENCES product(product_number)
    );
''')

# Input data into the 'customer' table
num_customers = int(input("Enter the number of customers to add: "))
for _ in range(num_customers):
    customer_id = input("Enter customer ID: ")
    customer_name = input("Enter customer name: ")
    address = input("Enter customer address: ")

    cursor.execute("INSERT INTO customer (customer_id, customer_name, address) VALUES (?, ?, ?)",
                   (customer_id, customer_name, address))

# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Database and tables created successfully.")
