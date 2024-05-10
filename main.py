from random import randrange

def main():


    user_wins = 0
    computer_wins = 0
    rps_array = ["Rock", "Paper", "Scissors"]

    while True:
        user_input = input("Type Rock/Paper/Scissors or Q to quit ")
        if user_input == "q" or user_input == "Q":
            break

        if user_input not in ["Rock", "Paper" , "Scissors"]:
            continue
        
        computer_random = randrange(3)
        computer_choice = rps_array[computer_random]

        print("The computer choose " + computer_choice)

        if user_input == "Scissors" and computer_choice == "Paper":
            user_wins += 1
            print("You won")
        elif user_input == "Paper" and computer_choice == "Rock":
            user_wins += 1
            print("You won")
        elif user_input == "Rock" and computer_choice == "Scissors":
            user_wins += 1
            print("You won")
        else:
            computer_wins += 1
            print("The computer won")

    print("you won " + str(user_wins) + " times")
    print("The computer won " + str(computer_wins) + " times")
    exit



main()