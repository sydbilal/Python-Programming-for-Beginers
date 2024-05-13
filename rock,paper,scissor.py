import random

while True:
    choices = ["Rock", "Paper", "Scissors"]

    user_choice = input("Choose Rock, Paper, or Scissors (or 'q' to quit): ").capitalize()

    if user_choice == 'Q':
        break

    if user_choice not in choices:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        continue

    computer_choice = random.choice(choices)

    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")
