import unittest
from unit_test_assignment.student_class import Student


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = Student(lname='Hardin', fname='Grayson', major='CIS', gpa=4.0)

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        grayson_student = Student(lname='Hardin', fname='Grayson', major='CIS')
        expected_last_name = 'Hardin'
        expected_first_name = 'Grayson'
        expected_major = 'CIS'

        self.assertEqual(grayson_student.last_name, expected_last_name)
        self.assertEqual(grayson_student.first_name, expected_first_name)
        self.assertEqual(grayson_student.major, expected_major)




if __name__ == '__main__':
    unittest.main()