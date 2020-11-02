class Student:
    def __init__(self, lname, fname, major, gpa=0.0):
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not isinstance(gpa, float) or gpa < 0 or gpa > 4 or not (name_characters.issuperset(fname) and name_characters.issuperset(lname) and name_characters.issuperset(major)):
            raise ValueError

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)


def main():
    grayson_student = Student(lname='Hardin', fname='Grayson', major='CIS', gpa=4.0)
    print(grayson_student)


if __name__ == '__main__':
    main()

