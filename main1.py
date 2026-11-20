import random
while True:
    user_action = input("Choose an option (Rock,Paper,Scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nyou chose {user_action}, computer chose {computer_action}\n")
    if user_action == computer_action:
        print(f"Both players selected {user_action}. Its a tie!")
    elif user_action == "rock":
            if computer_action == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose")
    elif user_action == "paper":
            if computer_action == "rock":
                print("Paper covers rock! You win!")
            else:
                print("scissors cut paper! You lose")
    elif user_action == "scissors":
            if computer_action == "paper":
                    print("scissors cut paper! You win!")
            else:
                    print("Rock smashes scissors! You lose")
    play_again = input("play again? (y/n): ")
    if play_again != "y":
          break
            