import random

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

while True:
    user_choice = input("Choose rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice, try again.")
        continue

    computer_choice = random.choice(choices)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    print("Score -> You:", user_score, " Computer:", computer_score)

    play_again = input("Play again? (y/n): ").lower()
    if play_again != "y":
        break

print("Thanks for playing!");