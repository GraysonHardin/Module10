"""
Program: customer_class.py
Author: Grayson Hardin
Last date modified: 11/1/2020

This takes in a list of names, customer id and various contact info. The program also shows examples of a proper input and an improper input.
"""


class Customer:
    # List of variables
    def __init__(self, customer_id, last_name, first_name, phone_number, address):
        self.customer_id = customer_id
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number
        self.address = address

    def __repr__(self):  # Added repr
        return 'Customer ID: ' + repr(self.customer_id) + repr(self.last_name) + repr(self.first_name) + repr(self.phone_number) + repr(self.address)

    def __str__(self):  # Added str
        return 'Customer ID: ' + str(self.customer_id) + str(self.last_name) + str(self.first_name) + str(self.phone_number) + str(self.address)

    def display(self):  # Creates the format and allows the user to print to the console
        base_string = repr(f'Customer ID: {self.customer_id} {self.last_name} {self.first_name} {self.address} {self.phone_number}')
        results = isinstance(self.customer_id, int)

        if results is True:  # Logic
            return base_string

        else:
            raise AttributeError("'Customer' object has no attribute 'cid'")


customer1 = Customer(8007315631, 'Ruiz', 'Matthew', '123 Main Street Urban, Iowa', '515-111-333')  # This is an example of a proper customer output
customer2 = Customer('hello', 'Bob', 'Henry', '803 North E Street Ankeny, Iowa', '515 973 301') # This is an example of a false customer output that will return a error.

print(customer1.__repr__())
print(customer2.display())
