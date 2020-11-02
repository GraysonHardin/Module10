"""
Program: employee.py
Author: Grayson Hardin
Last date modified: 11/1/2020

Program has a class (Employee) that has standard employee information. Depending on hourly /  yearly pay, it will return a different output. To change output. simply modify line 45.
"""

import locale
import datetime


class Employee:
    # List of variables
    def __init__(self, last_name, first_name, address, phone_number, salaried, salary, start_date):
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.phone_number = phone_number
        self.salaried = salaried
        self.salary = salary
        self.start_date = start_date

    def __repr__(self):  # Added repr
        return 'Last name: ' + repr(self.last_name) + ', First name ' + repr(self.first_name) + ', Address ' + repr(self.address) + ', Phone Number ' + repr(self.phone_number)

    def __str__(self):  # Added str
        return 'Last name: ' + str(self.last_name) + ', first name ' + str(self.first_name) + ', address ' + str(self.address) + ', phone number ' + str(self.phone_number)


    def display(self):
        locale.setlocale(locale.LC_ALL, '')
        base_string = 'Last name: ' + repr(self.last_name) + ', first name ' + repr(self.first_name) + ', address ' + repr(self.address) + ', phone number ' + repr(self.phone_number)
        formatted_datetime = datetime.date.strftime(self.start_date, "%m-%d-%Y")
        formatted_currency = locale.currency(self.salary, grouping=True)

        if self.salaried is True:  # Calculates whether or not to print hourly / yearly
            return base_string + ' Salaried employee: ' + formatted_currency + '/year' + ' Start date: ' + formatted_datetime

        formatted_hourly = base_string + ' Hourly employee: ' + formatted_currency + '/hour' + ' Start date: ' + formatted_datetime
        return formatted_hourly


emp_salary = Employee('Grayson', 'Hardin', '123 Main Street Cedar Rapids Iowa', '515-111-333,', True, 40000, datetime.datetime(2019, 6, 28))
print(emp_salary.display())








