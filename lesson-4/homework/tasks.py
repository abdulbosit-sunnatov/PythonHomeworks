def uncommon_elements(list1, list2):
    uncommon = [x for x in list1 if x not in list2] + [x for x in list2 if x not in list1]
    return uncommon

print(uncommon_elements([1, 1, 2], [2, 3, 4]))        
print(uncommon_elements([1, 2, 3], [4, 5, 6]))        
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5])) 


def print_squares(n):
    for i in range(1, n):
        print(i ** 2)

print_squares(5)


def insert_underscores(txt):
    result = []
    vowels = "aeiouAEIOU"
    count = 0

    for i, char in enumerate(txt):
        result.append(char)
        if (i + 1) % 3 == 0 or (char in vowels and (i + 1) % 3 != 0):
            if i + 1 < len(txt): 
                result.append('_')
    
    return ''.join(result)

print(insert_underscores("hello"))           
print(insert_underscores("assalom"))           
print(insert_underscores("abcabcdabcdeabcdefabcdefg")) 



import random

def guessing_game():
    while True:
        number = random.randint(1, 100)
        attempts = 10

        while attempts > 0:
            guess = int(input("Guess a number between 1 and 100: "))

            if guess > number:
                print("Too high!")
            elif guess < number:
                print("Too low!")
            else:
                print("You guessed it right!")
                break

            attempts -= 1
            print(f"Attempts left: {attempts}")

        if attempts == 0:
            print("You lost. Want to play again?")
            play_again = input("Type 'Y', 'YES', 'y', 'yes', 'ok' to play again: ")
            if play_again.lower() not in ['y', 'yes', 'ok']:
                break

guessing_game()


def check_password():
    password = input("Enter your password: ")

    if len(password) < 8:
        print("Password is too short.")
    elif not any(char.isupper() for char in password):
        print("Password must contain an uppercase letter.")
    else:
        print("Password is strong.")

check_password()


def prime_numbers():
    for num in range(2, 101):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=' ')
prime_numbers()

import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    player_score = computer_score = 0

    while player_score < 5 and computer_score < 5:
        computer_choice = random.choice(choices)
        player_choice = input("Choose rock, paper, or scissors: ").lower()

        if player_choice not in choices:
            print("Invalid choice! Try again.")
            continue

        print(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            player_score += 1
            print("You win this round!")
        else:
            computer_score += 1
            print("Computer wins this round!")

        print(f"Scores -> You: {player_score} | Computer: {computer_score}")

    if player_score == 5:
        print("Congratulations! You win the match!")
    else:
        print("Computer wins the match. Better luck next time!")

rock_paper_scissors()


