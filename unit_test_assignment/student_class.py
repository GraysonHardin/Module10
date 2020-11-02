"""
Program: student_class.py
Author: Grayson Hardin
Last date modified: 11/2/2020

This program takes a first and last name, major and gpa. It will simply print said values to the console. However, it has extensive testing behind to test whether or not the names are correct, if the gpa is a valid input, and more.
"""


class Student:
    def __init__(self, lname, fname, major, gpa=0.0):
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

        # Majority of the logic is from 18-20. This will process and evaluate whether the said variables are correct. If so, then they will continue on and print. If not, they will return the error.
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not isinstance(gpa, float) or gpa < 0 or gpa > 4 or not (name_characters.issuperset(fname) and name_characters.issuperset(lname) and name_characters.issuperset(major)):
            raise ValueError

    def __str__(self):  # This is the formatting code
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)


def main():  # Outputs to the console
    grayson_student = Student(lname='Hardin', fname='Grayson', major='CIS', gpa=4.0)
    print(grayson_student)


if __name__ == '__main__':
    main()

