import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(player,computer):
    if  computer == player:
        return "It's a Tie!"

    elif (player == "rock" and computer== "scissors") or\
         (player == "paper"and computer ==  "rock") or\
         (player == "scissors" and computer == "paper"):
         return "You Win!"
    
    else:
        return "Computer Wins!" 


def main():
    print("------------ Welcome to Rock, Paper, Scissors Game------------")

    round_to_win = int(input("How many rounds do you want to play?: "))
    computer_score = 0
    player_score = 0

    while computer_score < round_to_win and  player_score < round_to_win:

        player_choice = input("Enter your choice 'rock, paper, or scissors' or 'quit' to exit: ").lower().strip()

        if player_choice == 'quit':
            break

        elif player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer Choice: {computer_choice}")

        winner = determine_winner(computer_choice, player_choice)
        print(winner)

        if "You Win!" in winner:
            player_score += 1
        elif  "Computer Wins!" in winner:
            computer_score=+ 1
        else:
            continue
        
        print(f"Score:  YOU {player_score} - {computer_score}  COMPUTER\n")



if __name__ == "__main__":
    main()
