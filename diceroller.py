import random

while True:
    choice = input("Roll the dice? (y/n): ").lower()
    if choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"You rolled: {die1} and {die2}")
    elif choice == 'n':
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice! Please type 'y' or 'n'.")
