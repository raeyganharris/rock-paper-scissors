import random

def main():
    play_again = "y"
    while play_again == "y": #While the user wants to play again
        result = "Tie"
        while result == "Tie": #While result is a tie
            number = random.randint(1, 3)
            computer_choice = get_computer_choice(number)
            user_choice = input("Enter Rock, Paper or Scissors: ").lower()
            print("The computer chose", computer_choice.capitalize())
            result = get_winner(user_choice, computer_choice)
            print(result)

		play_again = input("Do you want to play again? (y/n): ").lower()

#Assign string to number
def get_computer_choice(number):
    if number == 1:
        return "rock"
    elif number == 2:
        return "paper"
    else:
        return "scissors"

#Decide who wins
def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif user_choice == "rock" and computer_choice == "scissors":
        return "You win!"
    elif user_choice == "scissors" and computer_choice == "paper":
        return "You win!"
    elif user_choice == "paper" and computer_choice == "rock":
        return "You win!"
    else:
        return "The computer wins!"

main()
