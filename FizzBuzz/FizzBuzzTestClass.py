import unittest
import FizzBuzzEngine


class FizzBuzzTestClass (unittest.TestCase):

    def test_Send_1_To_FizzBuzzEngine_Return_1(self):
        # Arrange
        value = int(1)
        expectedValue = int(1)

        # Act
        result = FizzBuzzEngine.FizzBuzz(value)

        # Assert
        self.assertEqual(expectedValue, result)

    def test_Send_2_To_FizzBuzzEngine_Return_2(self):
        # Arrange
        value = int(2)
        expectedValue = int(2)

        # Act
        result = FizzBuzzEngine.FizzBuzz(value)

        # Assert
        self.assertEqual(expectedValue, result)

    def test_Send_3_To_FizzBuzzEngine_Return_Fizz(self):
        # Arrange
        value = int(3)
        expectedValue = "Fizz"

        # Act
        result = FizzBuzzEngine.FizzBuzz(value)

        # Assert
        self.assertEqual(expectedValue, result)

    def test_Send_4_To_FizzBuzzEngine_Return_4(self):
        # Arrange
        value = int(4)
        expectedValue = int(4)

        # Act
        result = FizzBuzzEngine.FizzBuzz(value)

        # Assert
        self.assertEqual(expectedValue, result)

    def test_Send_5_To_FizzBuzzEngine_Return_Buzz(self):
        # Arrange
        value = int(5)
        expectedValue = "Buzz"

        # Act
        result = FizzBuzzEngine.FizzBuzz(value)

        # Assert
        self.assertEqual(expectedValue, result)

    def test_Send_6_To_FizzBuzzEngine_Return_Fizz(self):
        # Arrange
        value = int(6)
        expectedValue = "Fizz"

        # Act
        result = FizzBuzzEngine.FizzBuzz(value)

        # Assert
        self.assertEqual(expectedValue, result)

    def test_Send_7_To_FizzBuzzEngine_Return_7(self):
        # Arrange
        value = int(7)
        expectedValue = int(7)

        # Act
        result = FizzBuzzEngine.FizzBuzz(value)

        # Assert
        self.assertEqual(expectedValue, result)

    def test_Send_9_To_FizzBuzzEngine_Return_Fizz(self):
        # Arrange
        value = int(9)
        expectedValue = "Fizz"

        # Act
        result = FizzBuzzEngine.FizzBuzz(value)

        # Assert
        self.assertEqual(expectedValue, result)

    def test_Send_10_To_FizzBuzzEngine_Return_Buzz(self):
        # Arrange
        value = int(10)
        expectedValue = "Buzz"

        # Act
        result = FizzBuzzEngine.FizzBuzz(value)

        # Assert
        self.assertEqual(expectedValue, result)

    def test_Send_11_To_FizzBuzzEngine_Return_11(self):
        # Arrange
        value = int(11)
        expectedValue = int(11)

        # Act
        result = FizzBuzzEngine.FizzBuzz(value)

        # Assert
        self.assertEqual(expectedValue, result)

    def test_Send_12_To_FizzBuzzEngine_Return_Fizz(self):
        # Arrange
        value = int(12)
        expectedValue = "Fizz"

        # Act
        result = FizzBuzzEngine.FizzBuzz(value)

        # Assert
        self.assertEqual(expectedValue, result)

    def test_Send_15_To_FizzBuzzEngine_Return_FizzBuzz(self):
        # Arrange
        value = int(15)
        expectedValue = "FizzBuzz"

        # Act
        result = FizzBuzzEngine.FizzBuzz(value)

        # Assert
        self.assertEqual(expectedValue, result)

    def test_Send_30_To_FizzBuzzEngine_Return_FizzBuzz(self):
        # Arrange
        value = int(30)
        expectedValue = "FizzBuzz"

        # Act
        result = FizzBuzzEngine.FizzBuzz(value)

        # Assert
        self.assertEqual(expectedValue, result)

    def test_Send_99_To_FizzBuzzEngine_Return_Fizz(self):
        # Arrange
        value = int(99)
        expectedValue = "Fizz"

        # Act
        result = FizzBuzzEngine.FizzBuzz(value)

        # Assert
        self.assertEqual(expectedValue, result)

    def test_Send_100_To_FizzBuzzEngine_Return_Buzz(self):
        # Arrange
        value = int(100)
        expectedValue = "Buzz"

        # Act
        result = FizzBuzzEngine.FizzBuzz(value)

        # Assert
        self.assertEqual(expectedValue, result)


if __name__ == '__main__':
    unittest.main()
