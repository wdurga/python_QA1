import random

user_point = 0
computer_point = 0

while True:
    user_input = None
    possible_choices = ["rock", "paper", "scissors"]
    computer_input = random.choice(possible_choices)


    while user_input not in possible_choices:
        user_input = input("Enter your choice (rock, paper, scissors) : ")

    print(f"User chose {user_input}")
    print(f"Computer chose {computer_input}")

    if user_input == computer_input:
        print(f"It's a Tie.")
        print()
    elif user_input == "rock":
        if computer_input == "scissors":
            print("User wins.")
            user_point +=1
            print()
        else:
            print("User loose.")
            computer_point +=1
            print()

    elif user_input == "paper":
        if computer_input == "rock":
            print("User wins.")
            user_point +=1
            print()
        else:
            print("User loose.")
            computer_point +=1
            print()

    elif user_input == "scissors":
        if computer_input == "paper":
            print("User wins.")
            user_point +=1
            print()
        else:
            print("Computer wins. ")
            computer_point +=1
            print()

    play_again = input("Do you want to play again? (y/n) : ")
    print()
    if play_again.lower() != "y":
        break
print(f"Total Points of User: {user_point}")
print(f"Total Points of Computer: {computer_point}")
print()
print("GAME OVER !!")
print("Thank You for playing !! ")