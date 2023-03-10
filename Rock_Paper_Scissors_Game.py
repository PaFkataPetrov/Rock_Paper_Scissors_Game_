import random
import colorama
colorama.init()

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_move = ""

while player_move != "end":
    print(colorama.Style.RESET_ALL)
    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        print("Invalid Input. Try again: ")
        raise SystemExit

    computer_random_choose = random.randint(1, 3)

    computer_move = ""

    if computer_random_choose == 1:
        computer_move = rock
    elif computer_random_choose == 2:
        computer_move = paper
    else:
        computer_move = scissors
    print(colorama.Fore.YELLOW, f"The computer chose {computer_move}")

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        print(colorama.Fore.GREEN, "You win!")
    elif player_move == computer_move:
        print(colorama.Fore.BLUE, "Draw!")
    else:
        print(colorama.Fore.RED, "You lose!")
