# Showcase Your Dance Moves - Task 1: Code Correction
# Incorrect code below:
# weather = "sunny"
# if weather == "sunny":
# print("Wear sunglasses!")
# else:
# print("Take an umbrella!")

# Corrected code below:
weather = "sunny"
if weather == "sunny":
    print("Wear sunglasses!")
# Added an elif 
elif weather == "cold":
    print("Bring a coat!")
else:
    print("Take an umbrella!")
    
# Showcase Your Dance Moves - Task 2: Your Mood Today 
mood = input('How are you feeling today? Please enter "happy" or "sad" ')
if mood == "happy":
    print("That's great to hear!")
else:
    print("I hope your day gets better!")
    

# Python Naming Convention Practice - Task 1: Code Correction
# Incorrect code below:   
# Pi_value = 3.14
# userAge = 25
# user_location = "New York"
# MAXLIMIT = 1000

# Corrected code below:
pi_value = 3.14
user_age = 25
USER_LOCATION = "New York" #Assuming this is a constant 
MAX_LIMIT = 1000 #Assuming this is a constant 


# Arithmetic Operations in Daily Life - Task 1: Grocery Store Math
bread = 4
peanut_butter = 6
jelly = 5.50

cost_of_groceries = bread + peanut_butter + jelly

print(f'The total cost of the groceries is ${cost_of_groceries}!')


# Arithmetic Operations in Daily Life - Task 2: Bank Interest
amount = 10000
interest_rate = 7
interest_amount = interest_rate * 10

end_of_year_amount = amount + interest_amount 

print(f'The amount at the end of the year would be ${end_of_year_amount}!')