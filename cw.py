#
import random


# ### Problem 1:
# Write some Python code that has three variables called ```greeting```, ```my_name```, and ```my_age```.
# Initialize each of the 3 variables with an appropriate value, then print out the example below using the 3 variables
# and two different approaches for formatting Strings.

greeting = "Hello"
my_name = "Rachel"
my_age = "24"

#
# 1) Using concatenation and the ```+``` and 2) Using an ```f-string```. Sample output:
concat = greeting + " " + my_name + "!!! I hear that you are " + my_age + " today!"
print (concat)

stringMethod = f'{greeting} {my_name}!!! I hear that you are {my_age} today!'
print (stringMethod)

#YOUR_GREETING_VARIABLE YOUR_NAME_VARIABLE!!! I hear that you are YOUR_MY_AGE_VARIABLE today!

#
# ### Problem 2:
# Write some Python code that asks the user for a secret password.
# Create a loop that quits with the user's quit word. If the user doesn't enter that word, ask them to guess again.

password = input("Enter a secret password.")
password2= "x"
while password != password2:
    password2 = input("Guess the secret password.")

# ### Problem 3:
# Write some Python code using ```f-strings``` that prints 0 to 50 three times in a row (vertically).
# ```
# 1 1 1
# 2 2 2
# 3 3 3
# 4 4 4
# 5 5 5
# .
# .
# .
# ```

x=0
for x in range(1,51,1):
    print(x,x,x)


# ### Problem 4:
# Write some Python code that create a random number and stores it in a variable.
# Ask the user to guess the random number. Keep letting the user guess until they get it right, then quit.

user_guess = 0
secret_num = random.randint(1,5)
while user_guess != secret_num:
    user_guess = int(input("Guess a number from 1-5:"))
    if user_guess != secret_num:
        print('Incorrect! Try again.')

    else:
        print(f'Correct! The magic number was {secret_num}')



# ### Challenge
# Write some Python code to ask the user to create a number for the computer to guess between 1 - 10000.
# Write the code so that the computer guesses random numbers between 1 - 10000 and will keep guessing until
# the computer guesses the number correctly. Once the computer guesses the random number, alert the user with an
# alert box that displays how many guesses it took to guess the random number.
