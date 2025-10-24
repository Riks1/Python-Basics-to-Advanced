# Importing the random module to allow the computer to make random choices
import random

# Infinite loop so the game continues until the user types "quit"
while True:
    # Ask the user to input their move
    user_move = input("Enter Rock, Paper, or Scissors (or type 'quit' to stop): ").capitalize()
    
    # If the user types 'quit', the game will stop
    if user_move == "Quit":
        print("Game ended. Thanks for playing!")
        break

    # Generate a random number between 0 and 2 (0 = Rock, 1 = Scissors, 2 = Paper)
    number = random.randint(0, 2)

    # Convert the random number to a move (for computer)
    if number == 0:
        computer_move = "Rock"
    elif number == 1:
        computer_move = "Scissors"
    else:
        computer_move = "Paper"
    
    # Display the computer's move
    print(f"Computer chose: {computer_move}")

    # Compare user's move and computer's move to decide the winner
    if computer_move == user_move:
        # Both chose the same move
        print("It's a Draw!")
    elif (computer_move == "Rock" and user_move == "Scissors") or \
         (computer_move == "Scissors" and user_move == "Paper") or \
         (computer_move == "Paper" and user_move == "Rock"):
        # All cases where the computer wins
        print("Computer Wins!!")
    elif (user_move == "Rock" or user_move == "Paper" or user_move == "Scissors"):
        # If it's not a draw or computer win, the user wins
        print("You Win!! 🎉")
    else:
        # If the user enters something invalid
        print("Invalid input! Please enter Rock, Paper, or Scissors.")
    
    # Print a blank line for better readability
    print()
