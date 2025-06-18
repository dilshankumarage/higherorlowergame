from signal import valid_signals
from art import logo,vs
import random
from game_data import data

def format_data(account):
    """Take the account data and returns the printable format"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"Compare {account_name}, {account_desc} from {account_country}"

#use if to check user correct or wrong
def check_answer(user_guess,a_followers,b_followers):
    """Take a user's guess and return if the guess is right"""
    if a_followers>b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

#print the 1st logo
print(logo)
score = 0
game_continue = True
account_b = random.choice(data)
#assign random accounts a and b
while game_continue:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    #Question getting printed
    print(f"Compare A {format_data(account_a)}")
    #vs_image
    print(vs)

    print(f"Against B {format_data(account_b)}")

    #user input a or b
    guess = input("Please reply as 'A' OR 'B'").lower()
    # clear the screen
    print("\n"*20)
    print(logo)

    #compare which account has more followers
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    #if user correct plus 1 point, if wrong game over
    #if correct, correct account become A and a random get to be B
    if is_correct:
        score += 1
        print(f"You are correct, your score is {score}")
    else:
        print(f"Sorry you are wrong, your score is {score}")
        game_continue = False

