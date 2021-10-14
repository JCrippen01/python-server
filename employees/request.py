EMPLOYEES = [
    {
      "id": 1,
      "name": "Jessica Younker",
      "email": "jessica@younker.com",
      "employee": True
    },
    {
      "id": 2,
      "name": "Jordan Nelson",
      "email": "jordan@nelson.com",
      "employee": True
    },
    {
      "id": 3,
      "name": "Zoe LeBlanc",
      "email": "zoe@leblanc.com",
      "employee": True
    },
    {
      "name": "Meg Ducharme",
      "email": "meg@ducharme.com",
      "id": 4,
      "employee": True
    },
    {
      "name": "Hannah Hall",
      "email": "hannah@hall.com",
      "id": 5,
      "employee": True
    },
    {
      "name": "Emily Lemmon",
      "email": "emily@lemmon.com",
      "id": 6,
      "employee": True
    },
    {
      "name": "Jordan Castelloe",
      "email": "jordan@castelloe.com",
      "id": 7,
      "employee": True
    },
    {
      "name": "Leah Gwin",
      "email": "leah@gwin.com",
      "id": 8,
      "employee": True
    },
    {
      "name": "Caitlin Stein",
      "email": "caitlin@stein.com",
      "id": 9,
      "employee": True
    },
    {
      "name": "Greg Korte",
      "email": "greg@korte.com",
      "id": 10,
      "employee": True
    },
    {
      "name": "Charisse Lambert",
      "email": "charisse@lambert.com",
      "id": 11,
      "employee": True
    },
    {
      "name": "Madi Peper",
      "email": "madi@peper.com",
      "id": 12,
      "employee": True
    },
    {
      "name": "Jenna Solis",
      "email": "jenna@solis.com",
      "id": 14,
      "employee": True
    },
    {
      "id": 15,
      "name": "Ryan Tanay",
      "email": "ryan@tanay.com",
      "employee": False
    },
    {
      "id": 16,
      "name": "Emma Beaton",
      "email": "emma@beaton.com",
      "employee": False
    },
    {
      "id": 17,
      "name": "Dani Adkins",
      "email": "dani.adkins.com",
      "employee": False
    },
    {
      "id": 18,
      "name": "Adam Oswalt",
      "email": "adam@oswalt.com",
      "employee": False
    },
    {
      "id": 19,
      "name": "Fletcher Bangs",
      "email": "flangs@bangs.com",
      "employee": False
    },
    {
      "id": 20,
      "name": "Angela Lee",
      "email": "lee@lee.com",
      "employee": False
    },
    {
      "id": 21,
      "name": "mike mike",
      "email": "m@m.com",
      "employee": False,
    }
]

EMPLOYEELOCATIONS = [
    {
      "id": 1,
      "userId": 1,
      "locationId": 1
    },
    {
      "id": 2,
      "userId": 2,
      "locationId": 2
    },
    {
      "id": 15,
      "userId": 2,
      "locationId": 1
    },
    {
      "id": 3,
      "userId": 3,
      "locationId": 1
    },
    {
      "id": 4,
      "userId": 4,
      "locationId": 2
    },
    {
      "id": 5,
      "userId": 5,
      "locationId": 2
    },
    {
      "id": 6,
      "userId": 6,
      "locationId": 2
    },
    {
      "id": 7,
      "userId": 7,
      "locationId": 1
    },
    {
      "id": 8,
      "userId": 8,
      "locationId": 1
    },
    {
      "id": 9,
      "userId": 9,
      "locationId": 2
    },
    {
      "id": 10,
      "userId": 10,
      "locationId": 1
    },
    {
      "id": 11,
      "userId": 11,
      "locationId": 1
    },
    {
      "id": 12,
      "userId": 12,
      "locationId": 2
    },
    {
      "id": 14,
      "userId": 14,
      "locationId": 2
    }
]

def get_all_employees():
    '''something'''
    return EMPLOYEES

# Function with a single parameter

def get_single_employee(id):
    '''something'''
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the employeeS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

def create_employee(employee):
    '''Apends the Animals List: Next, in the employees/request.py module,
     put the following function in to take the new dictionary
     representation sent my the client and append it to the EMPLOYEES
     list.'''
    # Get the id value of the last employee in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the employee dictionary
    employee["id"] = new_id

    # Add the employee dictionary to the list
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee