def generate_random_choice():
    y=object()
    x=id(y)
    print(x)
    random_choice = x % 3
    return random_choice

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif ((player_choice == 0 and computer_choice == 2) or (player_choice == 1 and computer_choice == 0) or (player_choice == 2 and computer_choice == 1)):
        return "You win!"
    else:
        return "You lose!"

def choice(choice):
    choices = ["Rock", "Paper", "Scissors"]
    return choices[choice]

def playgame():
    print("Welcome to Rock, Paper, Scissors!")

    player_choice = input("Enter your choice (Rock, Paper, Scissors): ").strip().lower()
    if player_choice == "rock":
        player_choice = 0
    elif player_choice == "paper":
        player_choice = 1
    elif player_choice == "scissors":
        player_choice = 2
    else:
        print("Invalid choice! Exiting game.")
        return

    # user_input = input("Enter a string or number to generate randomness for the computer's choice: ")
    computer_choice = generate_random_choice()

    print(f"You chose: {choice(player_choice)}")
    print(f"Computer chose: {choice(computer_choice)}")

    result = determine_winner(player_choice, computer_choice)
    print(result)
    again=input("do you want to play again?\n(yes/no)\n")
    if again == "yes":
        playgame()
    else:
        return
    

playgame()