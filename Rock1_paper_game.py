import random

options = ("rock", "paper", "scissors")
playing = True  #creating a variable

while playing:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice(rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It is a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You Win!")
    else:
     print("You Loose!")

    """if not input("Play again? (y/n):").lower() == "y":
        running = False"""

    """play_again = input("Play Again? (y/n): ").lower()
    if play_again == "n":
        playing = False"""

    print("Thanks For playing!")