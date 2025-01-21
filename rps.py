# Rock-Paper-Scissors game
import random # Importing the random library 

# Creating variables for the player and computer
# Single quotes can also be used to create strings
'''
    player_choice = "rock" 
    computer_choice = 'paper'
'''

# A function is a block of code that only runs when it is called
# Indentation is important in Python. 
# If the lines of code are idented the same way, then they are part of the same function/block of code
def get_choices():
    # The input() function is used to get user input
    player_choice = input("Enter your choice: Rock, Paper, Scissors \n")

    options = ["rock", "paper", "scissors"] # List of options the computer can choose from
    computer_choice = random.choice(options) # The random.choice() method is used to select a random item from the options list 

    # Dictionaries are used to store data values in key:value pairs
    # Uses curly brackets
    # The key is the name of the variable and the value is the value of the variable
    # The values in a dictionary can also be variables. 
    choices = {"Player": player_choice, "Computer": computer_choice} # Dictionary with two key-value pairs

    return choices # Returns the player and computer choices

# The get_choices() function is called and the return value is stored in the choices variable
# choices = get_choices() # Returns the player and computer choices

# Prints the player and computer choices on the console.
# The output will be: ('rock', 'paper') which is a tuple because the get_choices() function has two variables
# print(choices)  

# Libraries, Lists & Methods
# Libraries are collections of functions and methods that allow you to perform many actions without writing your own code
# Import statements are used to import libraries and are usually at the top of the file
# A list is used to store multiple items in a single variable
# Lists are created using square brackets and each item is separated by a comma

# FUNCTION ARGUMENTS
# Functions can receive data called arguments inside the parentheses
def check_win(player, computer):
    # print("You chose:" + player + "Computer chose" + computer) # Prints the player and computer choice
    print(f"You chose: {player}, Computer chose: {computer}") # f-strings are used to format strings in Python

    # The lower() method is used to convert a string to lowercase
    # This is done to make the game case-insensitive
    player = player.lower()
    computer = computer.lower()

    if player == computer: # If the player and computer choices are the same
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:  
            return "Paper covers rock! You lose."  
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose."
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose."

choices = get_choices()
result = check_win(choices["Player"], choices["Computer"]) # Calls the check_win() function with the player and computer choices as arguments

print(result) # Prints the result of the game

'''
    elif player == "rock" and computer == "scissors":
        return "Rock smashes scissors! You win!" 
    elif player == "rock" and computer == "paper":
        return "Paper covers rock! You lose."
'''

# win = check_win("rock", "paper") # Calls the check_win() function with the player and computer choices as arguments   
    # return [player, computer] # Returns a list with the player and computer choices

# IF STATEMENTS
# If statements are used to make decisions in code using conditions by checking if an expression is True or False
# If the expression is True, the code block under the if statement will be executed. If it is False, the code block will be skipped

# ASSIGNMENT : Giving a variable a value using the = operator
# COMPARISON : Comparing two values using the >, <, >=, <= operators
# CONCATENATION : Combining strings using the + operator
# EQUALITY : Checking if two values are equal using the == operator
# INEQUALITY : Checking if two values are not equal using the != operator

# ELSE & ELIF STATEMENTS
# Else statements are used to execute code if the 'if statement' is False
# Elif statements are used to check multiple expressions for True and execute a block of code as soon as one of the conditions is True
'''
    age = 20
    if age >= 18:
        print("You are an adult!")
    elif age > 12:
        print("You are a teenager!")
    elif age > 1:
        print("You are a child!")
    else:
        print("You are an infant!")
'''
# REFACTORING & NESTED IF STATEMENTS
# Refactoring is the process of restructuring existing computer code without changing its external behavior/functionality to make it simpler and more understandable.
# Nested if statements are if statements that are inside another if statement which 

# ACCESSING DICTIONARY VALUES
# Dictionary values can be accessed using the key inside square brackets
'''
    choices = {"Player": "rock", "Computer": "paper"}

    p_choice = choices["Player"] 
    c_choice = choices["Computer"] 

    print(p_choice)
    print(c_choice)
'''