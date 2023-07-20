

"""name = input("Enter your name ")
age = input("Enter your age: ")
age = float(input("Enter your age: "))
age = int(input("Enter your age: "))
age = int(age)
age = age + 1
print(f"Hello {name}")
print(f"You are {age} years old")
"""

"""Practice 1 - mad libs"""

"""
adjective1 = input("Enter an adjective; ")
noun = input("Enter a noun; ")
adjective2 = input("Enter an adjective; ")
verb = input("Enter a verb; ")
adjective3 = input("Enter an adjective; ")


print(f"Today I went to a {adjective1} zoo in Ibadan, Nigeria.")
print(f"In an exhibit I saw {noun}")
print(f"{noun} was {adjective2} and {verb}ing")
print(f"I was {adjective3}")
"""

"""Practice 2 - area calculation"""

"""length = float(input("Enter the length of a rectangle: "))
width = float(input("Enter the width of a rectangle: "))
height = float(input("Enter the height of a rectangle: "))

area = length * width
volume = length * width * height

print(f"The area is: {area} cm")
print(f"The volume is: {volume}cm^3")"""

"""Practice 3 - shopping cart"""

"""item = input("What items would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like to buy?: "))

total = price * quantity

print(f"You have bought {quantity} {item}s")
print(f"Your total is: £{round( total, 2)} thanks for shopping with us")"""

"""Arithemetic Operations"""

#friends = 3

#friends = friends +1 (addition long cut)
#friends  += 1 (addition short cut)
#friends = friends - 2 (subtraction long cut)
#friends -= 2 (subtraction short cut)
#friends = friends * 3 (multiplication long cut)
#friends *= 3 (multiplication short cut)
#friends = friends / 2 (division long cut)
#friends /= 2 (division short cut)
#friends = friends ** 2 (exponential long cut)
#friends **= 2 (exponential short cut)
#remainder = friends % 2 (modulous operator)

#print(friends)

"""Built-in Functions"""

"""x = 3.14
y = 4
z = 5

#result = round(x)
#result = abs(y)
#result = pow(y, 3)
#result = max(x, y, z)
#result = min(x, y, z)

print(result)"""

"""Math Function, you have to import math"""
"""
import math

x = 9.7

print(math.pi)
print(math.e)
print(math.sqrt(x))
result = pow(4, 3) - This is power function, used to raise to the power of something.
result = math.ceil(x)
result = math.floor(x)

print(result)"""

"""Practice 1 - Find the circumference of a circle"""
#With maths task, always remember to import math

"""import math

radius = float(input("Enter the radius of any circle: "))

circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)}cm")"""


"""Practice 2 - Calculate the radius of a circle"""

#With maths task, always remember to import maths

"""import math

radius = float(input("Enter the radius of a circle; "))

area = math.pi * pow(radius, 2)

print(f"The radius is: {round(area, 2)}cm^2 ")"""

"""Practice 3 - Calculate the hypotenuse of a right angle triangle"""

import math

"""a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C = {c}")"""

#If statements
#if = Do some code only IF some condition is True. It is a basic form of condition making.
#       Else do something else
#       Elfi

"""age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You've not be born yet")
else:
    print("You must be 18+ to sign up!")"""

# Pay attention to order of if statements

"""age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old for this!")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You've not be born yet")
else:
    print("You must be 18+ to sign up!")"""

"""Practice 1 - Y/N"""

"""response = input("Would you like food? (Y/N): ") 
# input("Would you like food"?: )
#if response == YES

if response == "Y":
    print("Have some food!")
else: 
    print("No food for a lazy man!")"""

"""Practice 2"""

"""name = input("Enter your name: ")

if name == "":
    print(f"Bitch, go type in your dirty name")
else:
    print(f"Hello my dear sweetheart {name}")"""

"""Practice 3"""

"""for_sale = False

if for_sale:
    print("This item is available for sale")
else:
    print("This item is not for sale")

#Another practice
online = False

if online:
    print("The user is online")
else:
    print("The user is not online")"""

#Python calculator program - I'm happy

"""operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"Put in the right operator, bloody bomboclaat!")"""

#Python Weight converter program

"""weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? Type in K for Kgs or L for Lbs: ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"Your weight is: {weight} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"Your weight is: {weight} {unit}")
else:
    print(f" {unit} is invalid, enter the right unit to get your exact weight, Bitch!")"""

#Temperature conversion program

"""unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}°F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celcius is: {temp}°C")
else:
    print(f"{unit} is an invalid unit of measurement")"""

#LOGICAL OPERATORS - they are used on conditional statements

#           and = checks two or more conditions is TRUE
#           or = checks if at least one condition is TRUE
#           not = True if condition is False, and vice versa

#temp = 15

"""#AND
if temp > 0 and temp < 30:
    print("The temperature is good")
else:
    print("The temperature is bad")"""

#OR
"""if temp <= 0 or temp >= 30:
    print("The temperature is bad")
else:
    print("The temperature is good")"""

"""sunny = True
#NOT
if not sunny:
    print("It is sunny outside")
else:
    print("It is cloudy outside")"""

#STRING METHODS IN PYTHON

#name = input("Enter your full name: ")
#phone_number = input("Enter your phone number: ")

#result = len(name)
#result = name.find("o")
#result = name.rfind("q")
#name.capitalize()
#result = name.upper()
#result = name.lower()
#result = name.isdigit()
#result = name.isalpha()
#result = phone_number.count("-")
#result = phone_number.replace(" ", "")
#To get all the str methods type the following - print(help(str))

#print(result)

#Excersise 1
#Validate user input exercise
#1. username is no more than 12 characters
#2. username must not contain spaces
#3. username must not contain digits

"""username = input("Enter your username: ")

if len(username) > 12:
    print("Your username should be less than 12 characters")
elif username.find(" "):
    print("Your username should not contain spaces")
elif username.isdigit():
    print("Your username should not contain digits or numbers")
else:
    print(f"Welcome {username}")"""

"""#STRING INDEXING
#Indexing = accessing elements of a sequence using [] (indexing operator)
#           [start : end : step]
#           step [::]
#           the starting index is inclusive and ending index is exclusive

credit_number = "1234-5678-9012-3456"

#print(credit_number[14])
#print(credit_number[:4])
#print(credit_number[14:])
#print(credit_number[5:9])
#print(credit_number[-1])
#print(credit_number[::3]) #this will print every (3) third character within the string

#Exercise
#Create a program to get the last 4 digits of a credit card number
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

#Reverse the credit card numbers
#to reverse a string, set the ::step to -1
credit_number = credit_number[::-1]
print(credit_number)"""

"""PYTHON EMAIL SLICER"""
"""email = input("Enter your email: ")

index = email.index("@")

username = email[:index]
#domain = email[index:]
domain = email[index + 1:] #index reps the @ symbol, so adding +1 to it gives us the next character to be printed 
# to the console.
#Another shortcut way to write the index line, even though i don't like that below;
username = email[:email.index("@")]
domain = email[email.index("@") + 1:]

print(f"Your username is {username} and domain is {domain}")"""

"""#Format specifiers in Python
#format specifiers = {value:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator, used for thousand sepasrator 000,000

#price1,price2, price3 are values
price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is ${price1: .2f}")
print(f"Price 2 is ${price2: .2f}")
print(f"Price 3 is ${price3: .2f}")

#To allocate spaces use :10(here 10 is the number of spaces I want)
print(f"Price 1 is ${price1:<10}")
print(f"Price 2 is ${price2:<10}") #left aligned
print(f"Price 3 is ${price3:10}")"""


#While loop
#while loop = execute some code WHILE some condition remains true

#name = input("Enter your name: ")

#Normal approach no while loop
"""if name == "":
    print("You did not enter your name")
else:
    print(f"Hello {name}")"""

#While loop 1
"""name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")
print(f"Hello {name}")"""

#Infinite loop with no exit strategy
"""name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    #name = input("Enter your name: ")
print(f"Hello {name}")
"""

#While loop 2
"""age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))

print(f"You are {age} years old")"""

#While loop 3 using logical conditions

"""num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 - 10: "))

print(f"Your number is {num}")"""

#While loop 4 using logical conditions
"""food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter a food you like (q to quit): ")

print("bye")"""

#Compound interest calculator using while loop
#P = Principle
#R = Rate
#T = Time

"""principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero")

while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest rate can't be less than or equal to zero")

while time <= 0:
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("Time can't be less than or equal to zero")

# I have written the print below to test the while loop function works and meets all the set parameters.
#print(principle)
#print(rate)
#print(time)

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year(s): ${total: .2f}")
"""
#Method 2
"""
principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle cannot be less than or equal to zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate cannot be less than or equal to zero")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time cannot be less than zero")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year(s): £{total:.2f}")"""

#Loops
#for loops = execute a block of code a fixed number of times.
#           You can iterate over a range, string, sequence, etc.

"""for x in range(1, 11):
    print(x)
    
for x in reversed(range(1, 11)):
    print(x)

for x in range(1, 11, 2): #2 here represents - counting in two places, python will count every two numbers (1,3,5,7,9)
    print(x)

print("HAPPY NEW YEAR!")"""

"""credit_card = "1234-5678-9012-3456"

for x in credit_card:
    print(x)"""

#Using the continue keyword to skip, in this example 13 is skipped. Also in python,the last number is excluded,
# in this example, it stops at 20 and 21 is excluded

"""for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)"""
#using break
"""for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)"""

#Nested loop
#nested loop = A loop found within the code of another loop (outer, inner)
#               outer loop:
#                   inner loop:

"""for x in range(3): #this will repeat the inner loop (y) 3 times
    for y in range(1, 10): #this has to be y because the outer loop (x), already uses x, they cant be the same value.
        print(y, end="") #end="" - this ends each line of your print result
    print()"""

"""rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbols = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbols, end="")
    print()"""

#Countdown timer
#there is a sleep function
#import the time module

import time
"""
my_time = int(input("Enter the time in seconds: "))

#noraml way
for x in range(0, my_time):
    print(x)
    time.sleep(3)

print("Your time is up Bitch!")"""

#Count backwards, enclose range with reverse function or use a step. This ex, is using a step, -1 is the step
"""for x in range(my_time, 0, -1):
    print(x)
    time.sleep(3)

print("Your time is up Bitch!")"""

#Count backwards using reversed function
"""for x in reversed(range(0, my_time)):
    print(x)
    time.sleep(3)

print("Your time is up Bitch!")"""

#Let's display a digital clock
"""for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    #print(f"00:00:{seconds:02}") #here using format specifier to add zero padding = :02, ) pad the digits and display 2 digits
    time.sleep(3)

print("Your time is up Bitch!")"""

#Task - Credit card validator program in Python

# 1. Remove any '-' or ' '
# 2. Add all digits in the odd places from right to left
# 3. Double every second digit from right to left
#               (If result is a two-digit number, add the two-digit number together to get a single digit).
# 4. Sum the totals of steps 2 & 3
# 5. If sum is divisible by 10, the credit card # is valid

"""sum_odd_digits = 0
sum_even_digits = 0
total = 0

# Step1
card_number = input("Enter your credit card number: ")
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")
card_number = card_number[::-1] #this is to do reverse, another method
print(card_number)

# Step 2
for x in card_number[::2]:
    sum_odd_digits += int(x)

# Step 3
for x in card_number[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += (1 + (x % 10))
    else:
        sum_even_digits += x

# Step 4
total = sum_odd_digits + sum_even_digits

# Step 5
if total % 10 == 0:
    print("VALID")
else:
    print("INVALID")"""

# Python lists, sets and tuples
# Collection = single "variable" used to store multiple variables
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. Faster

"""fruits = ["apple", "pineapple", "orange", "banana", "coconut"]
print(dir(fruits)) #use this to display all the attributes and methods of a LIST, use the dir function
print(len(fruits)) #use this to get the length(in my own words, the number of items in your list)
print(help(fruits)) #use this to help you get the different methods you can use.
print("apple" in fruits) #use this as a boolean to confirm if an item is in the list, it returns as true/false.

# Methods in a list
#Append
fruits.append("melon") #the append() method is used to add an element to the end of a list. It is a list method that modifies the list by appending the specified element as a new item.
fruits.remove("apple")
fruits.insert(0, "lemon") #list the index and then the item
fruits.sort()
fruits.reverse() #to reverse in alphabetical order, sort first then reverse
fruits.clear()
fruits.index("apple") #this tells you the index position of an item in the list, remember to print. print(fruits.index("apple))
fruits.count()
fruits [0] = "pineapple" #use this to add an item to the list

#Methods in a Set
fruits = {"apple", "pineapple", "orange", "banana", "coconut"}
print(dir(fruits)) #use this to display all the attributes and methods of a SET, use the dir function
print(help(fruits)) #use this to help you get the different methods you can use.Use this for an indepth description from dir
fruits.add("")
fruits.remove("")
fruits.pop() #this will remove the first element randomly
fruits.clear()
fruits [0] = "pineapple" #use this to add an item to the set

#Methods in a Tuple
fruits = ("apple", "pineapple", "orange", "banana", "coconut", "coconut")
print(dir(fruits)) #use this to display all the attributes and methods of a TUPLE, use the dir function (Majorly index and count)
print(help(fruits)) #use this to help you get the different methods you can use.Use this for an indepth description from dir
print("apple" in fruits) #use this as a boolean to confirm if an item is in the list, it returns as true/false.
print(fruits.index("apple"))
fruits [0] = "pineapple" #use this to add an item to the tuple
fruits.count("coconut")"""

# Shopping cart Program
"""foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q": #Another way to write this - if food == "q" or food == "Q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: £"))
        foods.append(food)
        prices.append(price)

print("------ YOUR CART ------")

for food in foods:
    print(food) # to list horizontally, do this - end =""

for price in prices:
    total += price

print()
print(f"Your total is: £{total}, thanks for your patronage")"""

# Python 2D (2-dimensions) collections
"""fruits =        ["apple", "orange", "banana", "coconut"]
vegetables =    ["celery", "carrots", "potatoes"]
meats =         ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats] #this is a collection of fruits, vegetables, meats. Notice no ""

print(groceries[2]) #this will print out the index of each individual list
# for example print(groceries[0]) will print fruits, print(groceries[1]) = vegetables, print(groceries[2]) = meats

print(groceries[1][3]) #this will print out the index of the index of each individual list. You can also say, it will print out row 0; column 0. This is what I mean,
# print(groceries[0][0]) = fruits, apple, print(groceries[1][0]) = celery, print(groceries[2][0]) = chicken.
"""
"""#   You can also write your collection this way.
groceries = [["apple", "orange", "banana", "coconut"],
              ["celery", "carrots", "potatoes"],
              ["chicken", "fish", "turkey"]]

for collection in groceries:
    for food in collection: #using nested lopps prints everything in the collection
        print(food, end=" ")
    print() #printing an empty line takes your text to next line."""

"""#       Exercise - Create a key pad
num_pad = ((1, 2, 3),
           (4, 5, 6),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()"""

#    Python quiz game
"""
questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B") #CDAAB
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------")
    print(question)

    for option in options[question_num]:
        print()
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("        RESULTS       ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score/len(questions)*100)
print(f"Your score is: {score}%")"""
"""
#   Concession stand program

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

cart = []
total = 0

print("-----------MENU----------")
for key, value in menu.items():
    print(f"{key:10}: £{value:.2f}")
print("--------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("-----------YOUR ORDER-----------")
for food in cart:
    total += menu.get(food)
    print(food)

print()
print(f"Your total is: £{total:.2f}")"""

"""#   Just testing out random.randint(), used a conditional flow - if, else, elif
import random

play = input("Enter any random number (q to quit): ")

if play.lower() == "q":
    # Quit the game
    #print("Game over Bitch!")
    break
else:
    game = random.randint(1,20)
    print(game)"""
"""
#   Testing this out using loops and if statements
import random

while True:
    play = input("Enter any random number (q to quit): ")
    
    if play.lower() == "q":
        # Player quits the game
        break
    else:
        game = random.randint(1,6)
        print(game)
        
"""

"""
#   Testing this out using a loop with nested if statements
import random

while True:
    play = input("Enter any random numer (q to quit): ")

    if play.lower() == "q":
        # Quit the game
        break
    else:
        game = random.randint(1,12)
        print(game)

        if int(play) == game:
            print("You've won the game!!!!!")
        else:
            print("Try again")
            
"""

#   Generate random numbers in python

import random

"""low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

#number = random.randint(low, high)
#number = random.random() #this will give a floating number btw 0 & 1
#option = random.choice(options) #this will pick a random choice from your list, set or tuple
random.shuffle(cards) #this shuffle the numbers in a set, list, tuple

print(cards)"""
"""
#   Guess game
low = 1
high = 100
guesses = 0
number = random.randint(low, high)

while True:
    guess = int(input(f"Enter a number between ({low} - {high}): "))
    guesses += 1

    if guess < number:
        print(f"{guess} is too low")
    elif guess > number:
        print(f"{guess} is too high")
    else:
        print(f"{guess} is correct!!!!!")
        break

print(f"This round took you {guesses} guesses")"""

"""#   Rock paper scissors
import random

options = ("rock", "paper", "scissors")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You loose! Play again")

    play_again = input("You want to play again? (y/n): ").lower() #another way to do this
    if not play_again == "y":
        running = False
    #if not input("Play again? (y/n): ").lower() == "y": #if the user input does not equal y-yes, set running to false.
        #running = False

print("Thanks for playing!")
"""

"""
#    List Comprehension
#list comprehension = a way to create a new list with less syntax. Can mimic certain lambda functions, easier to read
#list = [expression for item in iterable]
#list lambda = [expression for item in iterable if conditional]
#list = [expression (if/else) for item in iterable]

squares = []                #create an empty list
for i in range(1, 11):      #create a for loop
    squares.append(i * i)   #define what each loop iteration should do
print(squares)

squares = [i * i for i in range(1, 11)]
print(squares)


students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
passed_students = list(filter(lambda x: x >= 60, students))
print(passed_students)

passed_students = [i for i in students if i >= 60]
print(passed_students)

passed_students = [i if i >= 60 else "FAILED" for i in students]
print(passed_students)"""


#      DICTIONARY COMPREHENSION
#dictionary comprehension = create dictionaries ousing an expression
#                           can replace for loops and certain lambda functions

# ---------------------FORMULA-------------------------------------------------------------------
#dictionary = {key: expression for (key, value) in iterable.items())
#dictionary = {key: expression for (key, value) in iterable.items() if conditional}
#dictionary = {key: (if/else) for (key, value) in iterable.items()}
#dictionary = {key: function(value) for (key, value) in iterable.items()}
# ------------------------------------------------------------------------------------------------

"""cities_in_F = {"New York": 32,
               "Boston": 75,
               "Los Angeles": 100,
               "Chicago": 50
               }

cities_in_C = {key: round((value-32) * (5/9)) for (key, value) in cities_in_F.items()}
print(cities_in_C)"""

# -----------------------------------------------------------------------------------------------

"""weather = {"New York": "snowing", "Boston": "sunny", "Los Angeles": "sunny", "Chicago": "cloudy"}

sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}

print(sunny_weather)"""

# -----------------------------------------------------------------------------------------------

"""cities = {"New York": 32, "Boston": 75, "Los Angeles": 10, "Chicago": 50}
desc_cities = {key: ("WARM"if value >= 40 else "COLD" ) for (key, value) in cities.items()}
print(desc_cities)
"""
# -------------------------------------------------------------------------------------------------

"""def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return  "WARM"
    else:
        return "COLD"


cities = {"New York": 32, "Boston": 75, "Los Angeles": 10, "Chicago": 50}
desc_cities = {key: check_temp(value) for (key, value) in cities.items()}
print(desc_cities )
"""

#POOP - Python Object Oriented Programming
#Atrributes = is/has. Ex; name, age, height
#Methods = actions; what an object can do. Ex; eat, sleep, make Youtube videos
#If writing a large program, use a new file for class and then import.
#Class name should start in capital letters

"""class Car:
#__init__(self) method helps us create/construct objects
    def __init__(self, make,model, year, colour):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour

#Create a method for the car object
    def drive(self):
        print("This "+self.model+" is driving")
        #print("This car is driving")

    def stop(self):
        print("This "+self.model+" is stopped")
        # print("This car is driving"


#Create/construct car object
car_1 = Car("Ford", "Focus", 2021, "grey")
car_2 = Car("Porsche", "Cayenne", 2023, "matte black")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.colour)

#Use the method
car_1.drive()
car_2.stop()"""

#Python class variables
"""class Car:

    wheels = 4  #class variable - set within a class outside of the constructor.
                # You can set a default balue for all instances of this class, for all unique objects created and you
                #can change the values later too.

    # __init__(self) method helps us create/construct objects
    def __init__(self, make, model, year, colour):
        self.make = make        #instance variable - declared inside of the constructor and can be given unique values
        self.model = model      #instance variable
        self.year = year        #instance variable
        self.colour = colour    #instance variable


car_1 = Car("Ford", "Focus", 2021, "grey")
car_2 = Car("Porsche", "Cayenne", 2023, "matte black")

car_1.wheels = 2



print(car_1.wheels)
print(car_2.wheels)"""

#Python Inheritance
"""class Animal:       #this is the parent class

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):       #this is the child class
    #Give each child class their own unique attribute and method.
    def run(self):      #this is a run method
        print("This rabbit is running")
class Fish(Animal):         #this is the child class
    def swim(self):
        print("This fish is swimming")
class Hawk(Animal):         #this is the child class
    def fly(self):
        print("This hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

# print(rabbit.alive)
# fish.eat()
# hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()"""

#       Python Multilevel Inheritance
#multi-level inheritance = when a  derived (child) class inherits another derived (child) class - hierarchy of classes
#       Lets use a family tree of living organisms
"""class Organism:

    alive = True

class Animal(Organism):

    def eat(self):
        print("This animal is eating")

class Dog(Animal):

    def bark(self):
        print("This dog is barking")

dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()"""

#       Multiple Inheritance Python
#multiple inheritance = when a child class is derived from more than one parent class

"""class Prey:

    def flee(self):
        print("This animal flees")

class Predator:

    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

#Create objects from these classes
rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()"""

#       Python method overriding
#method overriding is the ability of an object-oriented programming language to allow a subclass also known as a child class,
#to provide a specific implementation of a method that is already provided by one of its parents. In this case we are going to
#override the eat method.
"""class Animal:

    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating a carrot")

rabbit = Rabbit()
rabbit.eat()
"""

#       Python Method Chaining
#   method chaining = calling multiple methods sequentially. Each call performs an action on the same object and returns self.

"""class Car:
    #the functions are methods for the class Car
    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brake")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self

# Create an instance (object) of the Car class
car = Car()

# Method chaining to perform actions on the car object
car.turn_off().brake()

# Use the backslash when calling multiple methods in sequence (method chaining)
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()"""

#       Python Super Function
#   supper() = Function used to give access to the methods of a parent class. It returns a temporary object of a parent
#              class when used.
"""
# Define a Rectangle class with length and width attributes
class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

# Define a Square class that inherits from the Rectangle class(parent class)
class Square(Rectangle):
    def __init__(self, length, width):
        # It uses `super()` to call the constructor of the parent class to initialize the length and width attributes
        super().__init__(length, width)

    # Define a method to calculate the area of the square
    def area(self):
        return self.length * self.width

class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        # Additionally, it has a height attribute specific to the Cube class. The height attribute stays, because it is not in the rectangle class
        self.height = height

    # Define a method to calculate the volume of the cube
    def volume(self):
        return self.length * self.width * self.height
    
# Create objects of the Square and Cube classes
square = Square(3, 3)
cube = Cube(3, 3, 3)

# Calculate and print the area of the square and the volume of the cube
print(square.area())
print(cube.volume())
"""

#       Python Abstract Classes
#   Prevents a user from celebrating an object of that class + compels a user to override abstract methods in a child class

#   abstract class = a class which contains one or more abstract methods.
#   abstract method = a method that has a declaration but does not have an implementation.
#   abc = abstract base class
"""
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("This motorcycle is stopped")

#vehicle = Vehicle() #the abstact class
car = Car()
motorcycle = Motorcycle()

#vehicle.go() #TypeError: Can't instantiate abstract class Vehicle with abstract methods go, stop
car.go()
motorcycle.go()"""

#Python Objects as Arguments
"""
class Car:

    colour = None

class Okada:

    colour = None
def change_colour(car, colour):

    car.colour = colour

car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Okada()

change_colour(car_1, "red")
change_colour(car_2, "white")
change_colour(car_3, "black")
change_colour(bike_1, "yellow")

print(car_1.colour)
print(car_2.colour)
print(car_3.colour)
print(bike_1.colour)"""

#Python Duck Typing

# duck typing = concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/attributes are present
#               “If it walks like a duck, and it quacks like a duck, then it must be a duck.”

"""class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is qwuacking")

class Chicken:

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")

class Person():

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)
"""

#   walrus operator :=
# new to Python 3.8
# assignment expression a.k.a walrus operator
# assigns values to variables as part of a larger expression

# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)
# print(foods) #This will print out the food as a list
#This will print each food on a line
# for food in foods:
#     print(foods)

# foods = list()
# while food := input("What food do you like?: ") != "quit":
#     foods.append(food)
# print(foods) #This will print out the food as a list
#This will print each food on a line
# for food in foods:
#     print(foods)


#  Higher Order Function =  a function that either:
#                           1. accepts a function as an argument
#                               or
#                           2. returns a function
#                           (In python, functions are also treated as objects)

# ----- 1. accepts a function as an argument -----
"""def loud(text):
   return text.upper()

def quiet(text):
   return text.lower()

def hello(func):
   text = func("Hello")
   print(text)


hello(loud)
hello(quiet)
# ------------ 2. returns a function -------------
def divisor(x):
   def dividend(y):
       return y / x
   return dividend


divide = divisor(2)
print(divide(10))"""

#Python Lambda Function
#lambda function = a function written in one line using the lambda keyword. It accepts any number of arguments,
#                   but only has one expression (think of it as a shortcut). It is useful for a short period of time, throw-away

#lambda parameters: expression

#normal way to write functions
"""def double(x):
    return x * 2

print(double(5))"""

"""double = lambda x: x * 2
print(double(7))

multiply = lambda x, y: x * y
print(multiply(9, 5))

add = lambda x, y, z: x + y + z
print(add(1, 2, 3))

full_name = lambda first_name, last_name: first_name + " " + last_name
print(full_name("James", "Bond"))

age_check = lambda age: True if age >= 18 else False
print(age_check(38))"""

#       Python Sort Method
# sort() method   = used with lists. It is a built-in method for list. It can accept keyword arguments(key, reverse)
# sort() function = used with iterables

"""students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr.Krabs"]

students.sort()
students.sort(reverse=True)

for i in students:
    print(i)"""

#Sorting with tuple
"""students = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr.Krabs")
sorted_students = sorted(students)
sorted_students = sorted(students, reverse=True)

for i in sorted_students:
    print(i)"""

#Sorting with list of tuples
"""students = [("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick","D", 36),
            ("Spongebob","B", 20),
            ("Mr.Krabs","C", 78)]

grade = lambda grades: grades[1]
# students.sort(key=age)                     # sorts current list
for i in students:
    print(i) 
    """
#Sorting with tuples of tuples
"""students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick","D", 36),
            ("Spongebob","B", 20),
            ("Mr.Krabs","C", 78))
sorted_students = sorted(students, key=grade)  # sorts and creates a new list

for i in sorted_students:
    print(i) """

#           Python Map
#  map function () = applies a functon to each item in an iterable (list, tuple, etc)
#map function accepts two arguments (iterable, function)

#list of tuples

"""store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]

#convert store price to euros, its currently in dollars
to_euros = lambda data: (data[0], data[1]*0.82)

store_euros = list(map(to_euros, store))

for i in store_euros:
    print(i)

#convert store price to dollars, this time divide by 0.82
to_dollars = lambda data: (data[0], round(data[1] / 0.82, 2)) # use the round function to round to 2 decimal points
store_dollars = list(map(to_dollars, store))

for i in store_dollars:
    print(i)"""


#           Python Filter
# filter() =    creates a collection of elements from an iterable,
#               for which a function returns true
#
#               filter(function, iterable)
"""
friends = [("Rachel",19),
           ("Monica",18),
           ("Phoebe",17),
           ("Joey",16),
           ("Chandler",21),
           ("Ross",20)]

age = lambda data:data[1] >= 18

drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)"""

#       Python Reduce
# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#            performs function on first two elements and repeats process until 1 value remains
#
# reduce(function, iterable)

"""import functools

letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x, y,:x + y,letters) #here x+y reps H+E, so it keeps adding all the words in "letters"
print(word)

# factorial = [5,4,3,2,1]
# result = functools.reduce(lambda x, y,:x * y,factorial) #here x*y reps 5*4, so it keeps adding all the numbers in "factorial"
# print(result)"""

#           Python Zip
# zip(*iterables) =  aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                    creates a zip object with paired elements stored in tuples for each element

"""usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")
login_dates = ["1/1/2021","1/2/2021","1/3/2021"]

# --------------------------------------
users = list(zip(usernames,passwords))

for i in users:
    print(i)

# --------------------------------------
users = dict(zip(usernames,passwords))

for key,value in users.items():
    print(key+" : "+value)

# --------------------------------------
users = zip(usernames,passwords,login_dates)

for i in users:
    print(i)
"""

#           Python Time Module
#import time
# ***************************************************************************
#print(time.ctime(0))    # convert a time expressed in seconds since epoch to a readable string
#                                        epoch = when your computer thinks time began (reference point)
#print(time.time())      # return current seconds since epoch
#print(time.ctime(time.time())) # will get current time

# ***************************************************************************
# time.strftime(format, time_object) = formats a time_object to a string
# time_object = time.localtime() # local time
# time_object = time.gmtime()  # UTC time
# local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
# print(local_time)

# ***************************************************************************
# time.strptime(string_string, format) = parses a string representing time/date and returns a struct_time object
# time_string = "20 April, 2020"
# time_object = time.strptime(time_string,"%d %B, %Y")
# print(time_object)

# ***************************************************************************
# time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and returns a string
# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.asctime(time_tuple)
# print(time_string)

# ***************************************************************************
# time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and return seconds since epoch
# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.mktime(time_tuple)
# print(time_string)
