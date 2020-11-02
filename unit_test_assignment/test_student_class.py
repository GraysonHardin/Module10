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

    def test_object_created_all_attributes(self):
        grayson_student = Student(lname='Hardin', fname='Grayson', major='CIS', gpa=4.0)
        expected_last_name = 'Hardin'
        expected_first_name = 'Grayson'
        expected_major = 'CIS'
        expected_gpa = 4.0

        self.assertEqual(grayson_student.last_name, expected_last_name)
        self.assertEqual(grayson_student.first_name, expected_first_name)
        self.assertEqual(grayson_student.major, expected_major)
        self.assertEqual(grayson_student.gpa, expected_gpa)

    def test_student_str(self):
        expected = f'Hardin, Grayson has major CIS with gpa: 4.0'
        self.assertEqual(self.student.__str__(), expected)

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            Student(lname='123', fname='Grayson', major='CIS', gpa=4.0)

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            Student(lname='Hardin', fname='123', major='CIS', gpa=4.0)

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            Student(lname='Hardin', fname='Grayson', major='123', gpa=4.0)




if __name__ == '__main__':
    unittest.main()
