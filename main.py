import random
print("---------Welcome---------")
print("-----------To-------")
print("-----Rock Paper Scissors-------")
print("Select any of the options from 0 - 2:")
print("0.Rock \n1.Paper \n2.Scissors")

while True:
    user_action = int(input("Enter a choice: "))
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {possible_actions[user_action]}, computer chose {computer_action}.\n")

    if possible_actions[user_action] == computer_action:
        print(f"Both players selected {possible_actions[user_action]}. It's a tie!")
    elif possible_actions[user_action] == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif possible_actions[user_action] == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif possible_actions[user_action] == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break