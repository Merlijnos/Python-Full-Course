import random
while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None
    # print(computer)
    while player not in choices:
        player = input("rock, paper or scissors? ").lower()

    if player == computer:
        print("computer chose " + computer)
        print("player chose " + player)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("computer chose " + computer)
            print("player chose " + player)
            print("You lose!")
        if computer == "scissors":
            print("computer chose " + computer)
            print("player chose " + player)
            print("You win!")
    elif player == "scissors":
        if computer == "rock":
            print("computer chose " + computer)
            print("player chose " + player)
            print("You lose!")
        if computer == "paper":
            print("computer chose " + computer)
            print("player chose " + player)
            print("You win!")
    elif player == "paper":
        if computer == "scissors":
            print("computer chose " + computer)
            print("player chose " + player)
            print("You lose!")
        if computer == "rock":
            print("computer chose " + computer)
            print("player chose " + player)
            print("You win!")

    play_again = input("Play again? (yes/no) ").lower()
    
    if play_again != "yes":
        break
    
print("Bye!")