# Samantha Bergdahl

def rpsGame(user, computer):

    if (user == "Rock" or user == "Scissors" or user == "Paper"):
        if (user == computer):
            return "Tie"

        elif ((user == "Rock") and (computer == "Scissors")):
            return "You won"

        elif ((user == "Paper") and (computer == "Rock")):
            return "You won"

        elif ((user == "Scissors") and (computer == "Paper")):
            return "You won"

        else:
            return "Computer won"
    else:
        return "That was not one of the options :("
