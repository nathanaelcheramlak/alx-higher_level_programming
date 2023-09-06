#!/usr/bin/python3
""""Module for class Rectangle"""


class Rectangle:
    """Defines Rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Method that initializes instances

        Args:
            width: width of a Rectangle.
            height: height of a Rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Method that returns width of Rectangle.

        Returns:
            width of a Rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Method that sets width of Rectangle

        Args:
            value: width

        Raises:
            TypeError: if width is not intiger
            ValueError: if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Method that returns height of Rectangle.

        Returns:
            height of a Rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Method that sets height of Rectangle

        Args:
            value: height

        Raises:
            TypeError: if height is not intiger
            ValueError: if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Method that returns the area of Rectangle.

        Returns:
            area of Rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """Method that returns perimeter of Rectangle

        Returns:
            perimeter of Rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """Method that returns str # of Rectangle.

        Returns:
            string format of Rectangle
        """
        rectangle = ""

        if self.width == 0 and self.height:
            return rectangle

        for i in range(self.height):
            rectangle += (str(self.print_symbol) * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """Method that returns the string representation of instances.

        Returns:
            string representation of the Object.
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """Method that prints messege when the instance is deleted"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
