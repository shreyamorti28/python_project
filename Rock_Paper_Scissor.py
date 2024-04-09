import random
def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please try again.")


def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'paper' and computer_choice == 'rock') or \
            (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"


def main():
    print("Welcome to Rock, Paper, Scissors!")

    total_rounds = 3  # Change this to adjust the number of rounds
    user_score = 0
    computer_score = 0

    for round_num in range(1, total_rounds + 1):
        print(f"Round {round_num}:")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if 'win' in result:
            if 'You' in result:  # Increment user score if the user wins
                user_score += 1
            else:  # Increment computer score if the computer wins
                computer_score += 1

        print(f"Your score: {user_score}, Computer's score: {computer_score}")

    print("Game over!")
    print(f"Final scores - Your score: {user_score}, Computer's score: {computer_score}")


if __name__ == "__main__":
    main()
