# #using print function
# print("Hello World!")

# #using input function
# name = input("Enter your name: ")
# print("Hello " + name)

# color = input("What is your favorite color? ")
# print(f"My favorite color is {color}")

# number = input("Enter a number: ")
# #using int to change string to integer
# number = int(number)
# print(number + 5)

#Single line variable assignment with position
name, animal, food = "Kayla", "dog", "seafood" #all must be defined - so 3 variables must have 3 things assigned
print(name, animal, food) #can print all on one line this way 
print(name) #can print individual variables this way
print(animal)
print(food)

#in keyword #in a string it counts each index, but in a list it counts each word between commas basically
name = "Kayla"
if "y" in name:
    print("There is a y here")
    
name_list = ["Kayla", "Claire", "Deni"]
if "Claire" in name_list:
    print("She's Here!")
else:
    print("Nope")


