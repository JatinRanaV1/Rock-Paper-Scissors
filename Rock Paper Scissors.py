from random import randint

rps = ["Rock", "Paper", "Scissors"]

computer = rps[randint(0,2)]

player = False

while player == False:
    print("Rock, Paper, Scissors?...or type 'Exit' to exit")
    player = input("Input: ")
    if player == computer:
        print("Computer: ",computer)
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("Computer: ",computer)
            print("You lose!")
        else:
            print("Computer: ",computer)
            print("You win!")
    elif player == "Paper":
        if computer == "Scissors":
            print("Computer: ",computer)
            print("You lose!")
        else:
            print("Computer: ",computer)
            print("You win!")
    elif player == "Scissors":
        if computer == "Rock":
            print("Computer: ",computer)
            print("You lose!")
        else:
            print("Computer: ", computer)
            print("You win!")
    elif player == "Exit":
        exit()
    else:
        print("That's not a valid play. Check your spelling!")
    player = False
    computer = rps[randint(0,2)]