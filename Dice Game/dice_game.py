import random

def roll_dice():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    
    print(f"you've rolled a {die1} and a {die2}. Total: {die1 + die2} ")


def main():
    while True:
        choice = input("Do you want to roll a die? (y,n): ").strip().lower()

        if choice == 'y':
            roll_dice()
        elif choice == 'n':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter y or n.")


if __name__ == "__main__":
    main()