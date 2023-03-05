import unittest
import TriangleProblem

# Samantha Bergdahl


class TestTriangleProblem (unittest.TestCase):

    def test_If_Triangle_Is_Equilateral(self):
        # Arrange
        side1 = int(1)
        side2 = int(1)
        side3 = int(1)
        expectedValue = "The triangle is equilateral"

        # Act
        result = TriangleProblem.triangleSides(side1, side2, side3)

        # Assert
        self.assertEqual(expectedValue, result)

    def test_If_Triangle_First_Side_Different(self):
        # Arrange
        side1 = int(2)
        side2 = int(1)
        side3 = int(1)
        expectedValue = "The triangle is isosceles"

        # Act
        result = TriangleProblem.triangleSides(side1, side2, side3)

        # Assert
        self.assertEqual(expectedValue, result)

    def test_If_Triangle_Second_Side_Different(self):
        # Arrange
        side1 = int(1)
        side2 = int(2)
        side3 = int(1)
        expectedValue = "The triangle is isosceles"

        # Act
        result = TriangleProblem.triangleSides(side1, side2, side3)

        # Assert
        self.assertEqual(expectedValue, result)

    def test_If_Triangle_Third_Side_Different(self):
        # Arrange
        side1 = int(1)
        side2 = int(1)
        side3 = int(3)
        expectedValue = "The triangle is isosceles"

        # Act
        result = TriangleProblem.triangleSides(side1, side2, side3)

        # Assert
        self.assertEqual(expectedValue, result)

    def test_If_Triangle_All_Sides_Different(self):
        # Arrange
        side1 = int(1)
        side2 = int(2)
        side3 = int(3)
        expectedValue = "The triangle is irregular"

        # Act
        result = TriangleProblem.triangleSides(side1, side2, side3)

        # Assert
        self.assertEqual(expectedValue, result)


if __name__ == "__main__":
    unittest.main()
