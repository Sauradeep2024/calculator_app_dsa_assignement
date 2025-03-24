# Import the unittest module for writing unit tests
import unittest

# Import the Circle class from the circle.py module
from circle import Circle

# Import math to get accurate values of π
import math

# Define a test case class that inherits from unittest.TestCase
class TestCircleMethods(unittest.TestCase):

    def test_perimeter(self):
        """
        Test the perimeter method of the Circle class.
        For radius = 1, the expected perimeter = 2 * π * 1
        """
        circle = Circle(1)  # Create a circle with radius 1
        expected = 2 * math.pi  # Expected perimeter
        # Check if the actual perimeter is almost equal to expected (up to 5 decimal places)
        self.assertAlmostEqual(circle.perimeter(), expected, places=5)

    def test_area(self):
        """
        Test the area method of the Circle class.
        For radius = 2, the expected area = π * 2^2 = π * 4
        """
        circle = Circle(2)  # Create a circle with radius 2
        expected = math.pi * 4  # Expected area
        # Check if the actual area is almost equal to expected (up to 5 decimal places)
        self.assertAlmostEqual(circle.area(), expected, places=5)

# This block runs the tests when the file is executed directly
if __name__ == '__main__':
    unittest.main()
