import unittest
import calculations

class calculationsTest (unittest.TestCase):

    def test_CalculateSumOfIntegers_val1_and_val2_AssignValueToResult(self):
        #Arrange
        val1 = int(4)
        val2 = int(6)
        expectedResult = int(10)

        #Act
        result = calculations.addition(val1, val2)
        
        #Assert
        self.assertEqual (expectedResult, result)

    def test_CalculateReminderOfIntegers_val1_and_val2_AssignValueToResult(self):
       #Arrage
        val1 = int(3)
        val2 = int(3)
        expectedResult = int(0)

        #Act
        result = calculations.subtraction(val1, val2)

        #Assert
        self.assertEqual (expectedResult, result)

    def test_CalculateMultiplicationOfIntegers_val1_and_val2_AssignValueToResult(self):
       #Arrage
        val1 = int(3)
        val2 = int(3)
        expectedResult = int(9)

        #Act
        result = calculations.multiplication(val1, val2)

        #Assert
        self.assertEqual (expectedResult, result)

    def test_CalculateDivisionOfIntegers_val1_and_val2_AssignValueToResult(self):
       #Arrage
        val1 = int(3)
        val2 = int(3)
        expectedResult = int(1)

        #Act
        result = calculations.division(val1, val2)

        #Assert
        self.assertEqual (expectedResult, result)

if __name__ == '__main__':
    unittest.main()
