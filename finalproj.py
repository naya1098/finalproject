import time
import random
import gametwo  # Module I wrote
import pandas as pd

# Store the user's name
user_name = input("Please enter your name: ")

# Call gametwo
gametwo.display_rules()

# Global variables
money = 100
choices = []

# Welcome the user and lay out some more rules
def welcome():
    """
    This function displays the welcome message to the user and introduces the game and the $100 budget constraint.
    """
    print('Welcome to the build your cat simulator ' + user_name + '!')
    print('Keep in mind you only have $100 to customize your cat!')
    print('So use them wisely!! :3 ')
    print('----------------------------')
    print(' ')

# First question that requires user input: asks user their preference on cat hair length
def question_one():
    """
    This makes the user to choose between a long-haired cat for $50 or a short-haired cat for $30.
    Then deducts the chosen amount from the global 'money' variable.
    """
    global money
    while True:
        try:
            ans = input(' Q1: Would you rather pay $50 for a long hair cat (1) or $30 for a short haired (2) ? Type 1 or 2 to pick: ')
            if ans.lower() not in ('1', '2'):
                raise ValueError("Please enter '1' or '2'. ")  # Redirect user to input either 1 or 2
            break
        except ValueError as e:
            print(e)

    if ans.lower() == '1':
        print(f"Now you have a beautiful fluffy cat!")
        print(' ')
        money -= 50  # Decreases fund by 50
        choices.append(('Long hair', 50))
    elif ans.lower() == '2':
        print(f"You now have a beautiful short haired cat!")
        print(' ')
        money -= 30  # Decreases fund by 30
        choices.append(('Short hair', 30))

def question_two():
    """
    This function asks the user to choose between brown eyes for $20 or green eyes for $40 for their cat.
    Then asks the user to confirm their choice before deducting the amount from the global 'money' variable.
    If the user keeps answering "yes" when they want to change their mind the question will keep looping until user inputs "no".
    """
    global money
    while True:
        try:
            ans = input(f'Q2: Do you prefer brown eyes for $20 (1) or green eyes for $40 (2)? (1/2): ')
            print(' ')
            if ans.lower() not in ('1', '2'):
                raise ValueError("Please enter '1' or '2'. ")  # Redirect user to input either 1 or 2

            confirm = input('Would you like to change your mind? (yes/no): ')
            print(' ')
            if confirm.lower() == 'no':
                print("Okay, now moving on to the next question.")
                break
            elif confirm.lower() != 'yes':
                raise ValueError("Please enter 'yes' or 'no'.")
                
        except ValueError as e:
            print(e)
        print(' ')

    if ans.lower() == '1':
        print("You have spent $20!")
        print(' ')
        money -= 20  # Decreases fund by 20
        choices.append(('Brown eyes', 20))
    elif ans.lower() == '2':
        print("You have spent $40!")
        print(' ')
        money -= 40  # Decreases fund by 40
        choices.append(('Green eyes', 40))

def question_three():
    """
    Question 3 makes the user to choose the sex of the cat for a fixed price of $10.
    Either way it deducts $10 from the global 'money' variable based on the user's choice.
    """
    global money
    while True:
        try:
            ans = input(' Q3: Would you rather female ($10) or male ($10)? (f/m)?: ')
            if ans.lower() not in ('f', 'm'):
                raise ValueError("Please enter 'f' or 'm'. ")  # Redirect user to input either f or m
            break
        except ValueError as e:
            print(e)

    if ans.lower() == 'f':
        print(f"Now you have a beautiful female cat!")
        print(' ')
        money -= 10  # Decreases fund by 10
        choices.append(('Female', 10))
    elif ans.lower() == 'm':
        print(f"You now have a handsome male cat!")
        print(' ')
        money -= 10  # Decreases fund by 10
        choices.append(('Male', 10))

def question_four_randomizer():
    """
    The last question in the game offers the user a chance to adopt a second cat from a randomized selection.
    The 'my_cat' global variable updates if the user decides to adopt.
    """
    global my_cat
    global money

    cat_options = [
        ("a playful Siamese", "very vocal and enjoys climbing"),
        ("a Maine Coon", "friendly and great with families"),
        ("a Russian Blue", "shy but very affectionate once familiar")
    ]

    breed, personality = random.choice(cat_options)

    while True:
        try:
            ans = input(f'Would you like to adopt {breed} that is {personality}? (y/n):')
            print(' ')
            if ans.lower() not in ('y', 'n'):
                raise ValueError("Please enter 'y' or 'n'. ")  # Redirect user to input either y or n
            if ans.lower() == 'y':
                my_cat = {'breed': breed, 'personality': personality}
                choices.append((breed, 0))  # No cost for the second cat
                print("Congratulations on your new cats!")
            else:
                print("Well, that's too bad! We will find a different home for him!")
            break
        except ValueError as e:
            print(e)
        print(' ')

#in this function,I complete the advanced topic portion of the project - I added in a dataframe using pandas/pd to anaylze the data collected during the game according to the users choices. 
def finalscreen():
    """
    Finally, this function displays the final screen with a thank you message and rolls the credits after a brief pause.
    """
    print('Hello, user :) This concludes the game. Thank you for playing!')
    time.sleep(2)
    
    print('Please, allow for a brief rolling of the credits!')
    time.sleep(2)
    
    print('Credits:')
    print(' ')
    print('Creative Director &amp; Developer: Inaya Siddiqi')

    # Display the results
    df = pd.DataFrame(choices, columns=['Choice', 'Cost'])
    print(df)
    print(f'\nTotal money spent: ${100 - money}')
    print(f'Money left: ${money}')

welcome()
time.sleep(2)
question_one()
time.sleep(2)
print(' ')
print('You have', money, 'dollars left in the bank')
print(' ')
time.sleep(3)
question_two()
time.sleep(2)
print(' ')
print('You have', money, 'dollars left in the bank')
time.sleep(2)
question_three()
time.sleep(2)
print(' ')
print('You have', money, 'dollars left in the bank')
time.sleep(2)
print('__________________________________________ ')
print('Its your lucky day we are having a buy one get one free sale, in addition to your new cat, you also get ANOTHER randomized second cat!!!')
question_four_randomizer()
time.sleep(2)
finalscreen()

# Test cases (commented out)

# def test_question_one_long_hair():
#     global money
#     money = 100  # Reset money to initial value before the test
#     user_input = '1'  # Simulating user choosing the long hair cat which costs $50
#     question_one()  # Function to be tested
#     assert money == 50, "Test Failed: Money should be 50 after choosing long hair cat."
#     print("Test Passed: Correct amount deducted for long hair cat.")

# def test_question_one_short_hair():
#     global money
#     money = 100  # Reset money to initial value before the test
#     user_input = '2'  # Simulating user choosing the short hair cat which costs $30
#     question_one()  # Function to be tested
#     assert money == 70, "Test Failed: Money should be 70 after choosing short hair cat."
#     print("Test Passed: Correct amount deducted for short hair cat.")

# def test_question_two_brown_eyes():
#     global money
#     money = 100  # Reset money to initial value before the test
#     user_input = '1'  # Simulating user choosing brown eyes which cost $20
#     question_two()  # Function to be tested
#     assert money == 80, "Test Failed: Money should be 80 after choosing brown eyes."
#     print("Test Passed: Correct amount deducted for brown eyes.")
