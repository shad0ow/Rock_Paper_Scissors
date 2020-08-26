from random import randint

list = ["Scissors", "Paper", "Rock"]
computer = list[randint(0,2)]
print(computer)
guess = 0

while (guess != computer):
    guess = input("Guess : ")
    if (guess == computer):
        print("Tie !")

    elif (guess == "Scissors"):
        if (computer == "Paper"):
            print("You won ! Computer picked", computer.lower())
            break
        else:
            print("You lost ! Computer picked", computer.lower())
            break
    elif (guess == "Rock"):
        if (computer == "Paper"):
            print("You lost ! Computer picked", computer.lower())
            break
        else:
            print("You won ! Computer picked", computer.lower())
            break
    elif (guess == "Paper"):
        if (computer == "Scissors"):
            print("You lost ! Computer picked", computer.lower())
            break
        else:
            print("You won ! Computer picked", computer.lower())
            break
