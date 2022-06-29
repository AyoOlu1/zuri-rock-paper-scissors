import random
print("---------Welcome---------")
print("-----------To-------")
print("-----Rock Paper Scissors-------\n")
print("Select any of the options (r, p or s):\n")
print("r ----> Rock \np ----> Paper \ns ----> Scissors")

while True:
    options = { "r": ["rock"], "p":["paper"], "s":["scissors"] }
    computer = [random.choice(i) for i in options.values()] # select all values in the dictionary and put them in a list
    computer_action = random.choice(computer)   # select a random computer choice from the list in line 6
    user = (input("Enter a choice: "))
    
    # if the user selects the right option, run this code, else print the "else" statement

    if user in options.keys(): 
        print("Player: {}".format(("\n".join(options[user])) + "  Computer: " + computer_action + " "))
        
        if "\n".join(options[user]) == computer_action:
                print("Both players selected" + "\n".join(options[user])+ ". It's a tie!")
                print("Select another option")

        elif "\n".join(options[user]) == "rock":
            if computer_action == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif "\n".join(options[user]) == "paper":
            if computer_action == "rock":
                print("Paper covers rock! You win!")
                break
            else:
                print("Scissors cuts paper! You lose.")
        elif "\n".join(options[user]) == "scissors":
            if computer_action == "paper":
                print("Scissors cuts paper! You win!")
                break
            else:
                print("Rock smashes scissors! You lose.")

    else: 
        {
            print("select the right option!")
        }
   


