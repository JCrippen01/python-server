import sqlite3
import json
from models import Customer

CUSTOMERS = [
    {
        "id": 1,
        "name": "Dion Stoade",
        "address": "6866 4th Court",
        "email": "dstoade0@cornell.edu",
        "isKaren": True
    },
    {
        "id": 2,
        "name": "Windy Thorneloe",
        "address": "59924 Beilfuss Center",
        "email": "wthorneloe1@usa.gov",
        "isKaren": True
    },
    {
        "id": 3,
        "name": "Hillie Phillpotts",
        "address": "21 Straubel Point",
        "email": "hphillpotts2@rakuten.co.jp",
        "isKaren": True
    },
    {
        "id": 4,
        "name": "Jobye Danielou",
        "address": "7 Pleasure Terrace",
        "email": "jdanielou3@apple.com",
        "isKaren": True
    },
    {
        "id": 5,
        "name": "Gabbie Schult",
        "address": "46273 Oak Trail",
        "email": "gschult4@tinyurl.com",
        "isKaren": True
    },
    {
        "id": 6,
        "name": "Vasily Youdell",
        "address": "0993 Gulseth Avenue",
        "email": "vyoudell5@globo.com",
        "isKaren": True
    },
    {
        "id": 7,
        "name": "Debra Blackhurst",
        "address": "57305 Crowley Alley",
        "email": "dblackhurst6@last.fm",
        "isKaren": True
    },
    {
        "id": 8,
        "name": "Helenelizabeth Passfield",
        "address": "02 Reinke Plaza",
        "email": "hpassfield7@netvibes.com",
        "isKaren": True
    },
    {
        "id": 9,
        "name": "Franchot Slator",
        "address": "4930 Oneill Drive",
        "email": "fslator8@51.la",
        "isKaren": True
    },
    {
        "id": 10,
        "name": "Renaud Erbe",
        "address": "30 Westridge Pass",
        "email": "rerbe9@psu.edu",
        "isKaren": True
    }
]

def get_all_customers():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM customer c
        """)

        # Initialize an empty list to hold all animal representations
        customers = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            customer = Customer(
                row['id'], row['name'], row['address'], row['email'], row['password'])

            customers.append(customer.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(customers)


def get_single_customer(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM customer c
        WHERE c.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an customer instance from the current row
        customer = Customer(data['id'], data['name'],
                            data['address'], data['email'], data['password'])

        return json.dumps(customer.__dict__)

def create_customer(customer):
    '''Apends the customers List: Next, in the customers/request.py module,
     put the following function in to take the new dictionary
     representation sent my the client and append it to the customerS
     list.'''
    # Get the id value of the last customer in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the customer dictionary
    customer["id"] = new_id

    # Add the customer dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer

def delete_customer(id):
    # Initial -1 value for customer index, in case one isn't found
    customer_index = -1

    # Iterate the customerS list, but use enumerate() so that you
    # can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Store the current index.
            customer_index = index

    # If the customer was found, use pop(int) to remove it from list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    # Iterate the customerS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Update the value.
            CUSTOMERS[index] = new_customer
            break
