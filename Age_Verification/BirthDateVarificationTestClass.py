import unittest
import BirthDateVarification

# Samantha Bergdahl


class Test_What_Age_Is_User (unittest.TestCase):

    def test_If_User_Is_Under_18(self):
        # Arrange
        value = int(10)
        exceptedValue = "You are a child"

        # Act
        result = BirthDateVarification.whatAge(value)

        # Assert
        self.assertEqual(exceptedValue, result)

    def test_If_User_Is_Over_18_And_Under_70(self):
        # Arrange
        value = int(50)
        exceptedValue = "You are an adult"

        # Act
        result = BirthDateVarification.whatAge(value)

        # Assert
        self.assertEqual(exceptedValue, result)

    def test_If_User_Is_Over_70(self):
        # Arrange
        value = int(80)
        exceptedValue = "You are a pensioner"

        # Act
        result = BirthDateVarification.whatAge(value)

        # Assert
        self.assertEqual(exceptedValue, result)


if __name__ == "__main__":
    unittest.main()
