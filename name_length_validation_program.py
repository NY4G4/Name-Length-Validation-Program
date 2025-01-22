name = input('What is your name? ') #Asks the user to enter his/her name
if len(name) < 3: #Checks if the name is at least 3 characters long
    print("Your name must be at least 3 characters long!")
elif len(name) > 50: #Checks whether the length of the name has exceeeded 50 characters
    print("The length of your name should not exceed 50 characters!")
else:
    print("Thank you for entering your name.")
