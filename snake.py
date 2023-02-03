from random import *

choices = ["snake", "water", "gun"]

while True:
    print("1.Play")
    print("2.EXIT")
    ch = input("Enter Your Choice : ")
    if ch == "1":
        print(choices)
        user_input = input("Enter Your Choice : ").lower()
        computer_choice = choices[randrange(0, 3)]
        # Condition
        if user_input == computer_choice:
            print(f"Computer choose :-{computer_choice}:,Match Draw")
        elif user_input == "snake" and computer_choice == "water":
            print(f"Computer choose :-{computer_choice}:,You Won")
        elif user_input == "water" and computer_choice == "gun":
            print(f"Computer choose :-{computer_choice}:,You Won")
        elif user_input == "gun" and computer_choice == "snake":
            print(f"Computer choose :-{computer_choice}:,You Won")
        else:
            print(f"Computer choose :-{computer_choice}:You loose computer won")
    elif ch == "2":
        break
    else:
        print("Invalid Syntax")