import random

def get_choice():
    choice = input("Choose rock, paper, or scissors: ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        choice = input("Choose rock, paper, or scissors: ").lower()
    return choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif ((user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")):
        return "You win!"
    else:
        return "You lose!"

def disp(user_choice, computer_choice, result):
    # Display the user's choice, computer's choice, and the result
    print(f"\nYour choice: {user_choice.capitalize()}")
    print(f"Computer's choice: {computer_choice.capitalize()}")
    print(f"Result: {result}")

def play():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_choice()
        computer_choice = get_computer_choice()

        result = determine(user_choice, computer_choice)
        disp(user_choice, computer_choice, result)

        # Update
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        # Display 
        print(f"\nScores - You: {user_score} | Computer: {computer_score}")

        print()
        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        print()
        
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    print("Let's play Rock,Paper,Scissors Game")
    play()
