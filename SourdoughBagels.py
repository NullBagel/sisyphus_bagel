import random

def settings():    
    while True:
        print(f"Current difficulty set to {difficulty}.")
        print("Select difficulty settings or press X to exit:")
        print("1. Easy (Guesses: 15 | Digits: 2 | Numbers only)")
        print("2. Standard (Guesses: 10 | Digits: 3 | Numbers only)")
        print("3. Hard (Guesses: 7 | Digits: 3 | Numbers & letters)")
        difficulty = input()
        
        if difficulty in ["1", "2", "3", "X"]:
            print(f"You have chosen {difficulty}.")
            print("Settings will be adjusted accordingly.")
            break
        
        else:
            print("Invalid selection. Please select again.")  

    if difficulty == "1":
        max_guess = 15
        max_digits = 2
        mode = "Numbers"
    elif difficulty == "2":
        max_guess = 10
        max_digits = 3
        mode = "Numbers"
    elif difficulty == "3":
        max_guess = 7
        max_digits = 3
        mode = "Numbers & Letters"
    elif difficulty == "X":
        return difficulty, max_guess, max_digits, mode

    return difficulty, max_guess, max_digits, mode

def char_check(user_input, max_digits, mode):
    
    if mode == "Numbers":
        while len(user_input) != max_digits or not user_input.isdigit():
            user_input = input(f"Please input {max_digits} numbers.")
        return user_input
    
    elif mode == "Numbers & Letters":
        while len(user_input) != max_digits or not user_input.isalnum():
            user_input = input(f"Please input {max_digits} numbers and/or letters")
        return user_input

def get_bagel(max_digits, mode):
    numbers_list = "0123456789"
    numbers_letters_list = numbers_list + "abcdefghijklmnopqrstuvwxyz"

    if mode == "Numbers":
        return "".join(random.choices(numbers_list, k=max_digits))
        
    elif mode == "Numbers & Letters":
        return "".join(random.choices(numbers_letters_list, k=max_digits))

def get_clues(user_input, bagel_number):
    clues = []
    
    if user_input == bagel_number:
        return True

    for i in range(len(user_input)):        
        if user_input[i] == bagel_number[i]:
            clues.append("Fermi")
        elif user_input[i] in bagel_number:
            clues.append("Pico")

    if len(clues) == 0:
        clues.append("Bagels")
    else:
        clues.sort()

    return clues

def play_again():
    while True:
        print("Play again? Y/N")
        replay_choice = input().upper()
        if replay_choice in ("Y", "N"):
            break
        else:
            print("Please only input Y or N")

    return replay_choice
    
def bagel_game_core(max_guess, max_digits, mode):
    while True:
        bagel_number = get_bagel(max_digits, mode)
        
        for i in range(max_guess):
            user_input = input("Please input a number:")
            user_input = char_check(user_input, max_digits, mode) #check if entry fits within the defined number of digits
            clues = get_clues(user_input, bagel_number)
            
            if clues is True:
                print("You win!")
                break
            else:
                print(f"Guess #{i + 1}")
                print(clues)
        else:
            print("Out of guesses :(")
        replay_choice = play_again()
        
        if replay_choice == "N":
            break

def menu_explanation():
    explanation_input = ""
    while explanation_input.lower() != "x":
        print("""
=============================================================
Sourdough Bagels is number guessing game where you will attempt to guess a random number picked by the computer.
Depending on your inputs, you will be given clues based on how close you are to the secret number.

| CLUES  | WHAT IT MEANS
---------------------------------------------------------
| Pico   | One digit is correct but in the wrong position
| Fermi  | One digit is correct and in the right position
| Bagels | No digit is correct
---------------------------------------------------------

For example, if the secret number is 248 and your guess was 843, the clues will be 'Fermi', 'Pico'.
=============================================================
If you are done, PRESS X TO RETURN TO MAIN MENU.
*pressing anything else will repeat the explanation above.*
        """)
        explanation_input = input()

def menu_quit():
    print("Quiting game...")
    print("Thank you for playing!")

max_guess = 10
max_digits = 3
mode = "Numbers"
difficulty = "2"

print("""🥯 Sourdough Bagels 🥯
The Bagels game but with an added kick!
By MangoBagel 🥭, Created: 24/02/2026""")

print("""Hello! 👋
Thank you for playing my game! Just like the namesake, Sourdough Bagels is the more flavourful version of the traditional Bagels game.
""")

while True:
    print("""🥯🥯🥯 MAIN MENU 🥯🥯🥯
    1. Start bagelling 
    2. Explanation
    3. Settings
    4. Quit Game""")
    menu_choice = input("What would you like to do?")
    
    if menu_choice == "1":
        bagel_game_core(max_guess, max_digits, mode)
        
    elif menu_choice == "2":
        menu_explanation()

    elif menu_choice == "3":
        difficulty = settings()
        max_guess = difficulty[1]
        max_digits = difficulty[2]
        mode = difficulty[3]
        
    elif menu_choice == "4":
        menu_quit()
        break
        
    else:
        print("Please select from the 4 choices. Key in the number corresponding to the action you want.")
