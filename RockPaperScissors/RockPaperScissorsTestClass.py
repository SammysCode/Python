import unittest
import RockPaperScissors

# Samantha Bergdahl


class TestRPSGame (unittest.TestCase):

    def test_For_Rock_And_Rock(self):
        # Arrange
        user = "Rock"
        computer = "Rock"
        expectedValue = "Tie"

        # Act
        result = RockPaperScissors.rpsGame(user, computer)

        # Assert
        self.assertEqual(expectedValue, result)

    def test_For_Paper_And_Paper(self):
        # Arrange
        user = "Paper"
        computer = "Paper"
        expectedValue = "Tie"

        # Act
        result = RockPaperScissors.rpsGame(user, computer)

        # Assert
        self.assertEqual(expectedValue, result)

    def test_For_Scissor_And_Scissor(self):
        # Arrange
        user = "Scissors"
        computer = "Scissors"
        expectedValue = "Tie"

        # Act
        result = RockPaperScissors.rpsGame(user, computer)

        # Assert
        self.assertEqual(expectedValue, result)

    def test_For_Paper_And_Rock(self):
        # Arrange
        user = "Paper"
        computer = "Rock"
        expectedValue = "You won"

        # Act
        result = RockPaperScissors.rpsGame(user, computer)

        # Assert
        self.assertEqual(expectedValue, result)

    def test_For_Paper_And_Scissor(self):
        # Arrange
        user = "Paper"
        computer = "Scissors"
        expectedValue = "Computer won"

        # Act
        result = RockPaperScissors.rpsGame(user, computer)

        # Assert
        self.assertEqual(expectedValue, result)

    def test_For_Rock_And_Scissor(self):
        # Arrange
        user = "Rock"
        computer = "Scissors"
        expectedValue = "You won"

        # Act
        result = RockPaperScissors.rpsGame(user, computer)

        # Assert
        self.assertEqual(expectedValue, result)

    def test_For_Rock_And_Paper(self):
        # Arrange
        user = "Rock"
        computer = "Paper"
        expectedValue = "Computer won"

        # Act
        result = RockPaperScissors.rpsGame(user, computer)

        # Assert
        self.assertEqual(expectedValue, result)

    def test_For_Scissor_And_Paper(self):
        # Arrange
        user = "Scissors"
        computer = "Paper"
        expectedValue = "You won"

        # Act
        result = RockPaperScissors.rpsGame(user, computer)

        # Assert
        self.assertEqual(expectedValue, result)

    def test_For_Scissor_And_Rock(self):
        # Arrange
        user = "Scissors"
        computer = "Rock"
        expectedValue = "Computer won"

        # Act
        result = RockPaperScissors.rpsGame(user, computer)

        # Assert
        self.assertEqual(expectedValue, result)

    def test_For_If_User_Typed_Else_Than_The_Options_Result_NotOneOfTheOptions(self):
        # Arrange
        user = ""
        computer = "Rock"
        expectedValue = "That was not one of the options :("
        # Act
        result = RockPaperScissors.rpsGame(user, computer)

        # Assert
        self.assertEqual(expectedValue, result)


if __name__ == "__main__":
    unittest.main()
