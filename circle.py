import math

class Circle:
    """
    A class used to represent a Circle.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius: float):
        """
        Initialize a Circle object with a given radius.

        Parameters:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def perimeter(self) -> float:
        """
        Calculate the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.radius

    def area(self) -> float:
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.radius ** 2)
