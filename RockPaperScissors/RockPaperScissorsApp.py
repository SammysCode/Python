import RockPaperScissors
import random

# Samantha Bergdahl


def main():

    user = input("Choose Rock, Paper or Scissors: ")

    rps = ("Rock", "Paper", "Scissors")
    computer = (random.choice(rps))

    result = RockPaperScissors.rpsGame(user, computer)
    print("Computer chose: " + computer)
    print("You chose: " + user)
    print(result)


if __name__ == "__main__":
    main()
