"""
Program: invoice_class.py
Author: Grayson Hardin
Last date modified: 11/1/2020

This program takes a list of items and prints a invoice of the item and price.
"""


import locale


class Invoice:
    # List of variables
    def __init__(self, invoice_id, customer_id, last_name, first_name, phone_number, address, items_with_price={}):
        self.invoice_id = invoice_id
        self.customer_id = customer_id
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number
        self.address = address
        self.items_with_price = items_with_price

    def __repr__(self):  # Added repr
        return 'Invoice ID: ' + repr(self.invoice_id) + ' The Customer ID is: ' + repr(self.customer_id) + repr(self.last_name) + repr(self.first_name) + repr(self.phone_number) + repr(self.address)

    def __str__(self):  # Added str
        return 'Invoice ID: ' + str(self.invoice_id) + ', The Customer ID is: ' + str(self.customer_id) + str(self.last_name) + str(self.first_name) + str(self.phone_number) + str(self.address)

    def add_item(self, item, price):  # Dictionary
        self.items_with_price.update({
            item: price
        })

    def create_invoice(self):  # Initiate the invoice
        locale.setlocale(locale.LC_ALL, '')
        base_string = repr(f'Invoice ID: {self.invoice_id} The customer ID is: {self.customer_id} {self.last_name} {self.first_name} {self.phone_number} {self.address}')
        print(base_string)

        for item, price in self.items_with_price.items():
            print(item, ":", locale.currency(price, grouping=True))
        total_before_tax = sum(self.items_with_price.values())
        price_with_tax = (total_before_tax * .06) + total_before_tax  # Calculates tax
        print('The total amount due is:', locale.currency(price_with_tax, grouping=True))

# Example one
invoice1 = Invoice(8007315631, 183, 'Ruiz', 'Matthew', '123 Main Street Urban, Iowa', '515-111-333')
invoice1.add_item(item="Apple cord", price=3)
invoice1.add_item(item="Corsair Headset", price=5)
invoice1.add_item(item="Ford Mustang", price=2)

# Examples two
invoice1.create_invoice()
invoice2 = Invoice(281414, 183, 'Ruiz', 'Matthew', '123 Main Street Urban, Iowa', '515-111-333', {'Ford 150': 60000})
invoice2.add_item(item="Computer", price=10)
invoice2.add_item(item="keyboard", price=30)
invoice2.create_invoice()
