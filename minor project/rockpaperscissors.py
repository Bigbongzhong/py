class RPS:
    def genrandomChoice(self, user_input):
        hash_value = hash(user_input)
        random_choice = abs(hash_value) % 3
        return random_choice

    def winner(self, pChoice, cChoice):
        if pChoice == cChoice:
            return "It is a tie"
        elif ((pChoice == 0 and cChoice == 2) or 
                (pChoice == 1 and cChoice == 0) or 
                (pChoice == 2 and cChoice == 1)):
            return "You won the game"
        else:
            return "You lost the game"

    def user_choice(self, choice):
        ch = ["Rock", "Paper", "Scissors"]
        return ch[choice]

    def play(self):
        print("Welcome to Rock-Paper-Scissors!")

        while True:
            pChoice = input("Enter your choice (Rock, Paper, Scissors): ").strip().lower()
            if pChoice == "rock":
                pChoice = 0
            elif pChoice == "paper":
                pChoice = 1
            elif pChoice == "scissors":
                pChoice = 2
            else:
                print("Invalid choice! Try again.")
                continue  

            user_input = input("Enter a string or number to generate randomness for the computer's choice: ")
            computer_choice = self.genrandomChoice(user_input)

            print(f"You chose: {self.user_choice(pChoice)}")
            print(f"Computer chose: {self.user_choice(computer_choice)}")

            print(self.winner(pChoice, computer_choice))

            again = input("Do you want to play again? (yes/no): ").strip().lower()
            if again != "yes":
                print("Thanks for playing!")
                break

RPS().play()
