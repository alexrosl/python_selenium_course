import unittest
from tests.home.login_test import LoginTests
from tests.courses.register_courses_csv_test import RegisterCoursesCSVTests

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesCSVTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)
