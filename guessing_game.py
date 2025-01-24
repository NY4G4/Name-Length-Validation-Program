secret_number = int(input("Enter a number between 1 and 10: ")) #the secret number that the user has to guess
while secret_number > 10:
        print("The number that you have entered is not within the specified range! Please enter a number between 1 and 10: ")
        secret_number = int(input("Enter a number between 1 and 10: "))
        
guess_count = 0 
guess_limit = 3 #The maximum number of guesses a user can make

while guess_count < guess_limit:
    guess = int(input("Enter a number between 1 and 10: "))
    guess_count += 1
    if guess > 10:
        print("The number that you have entered is not within the specified range! Please enter a number between 1 and 10:")
    elif guess == secret_number:
        print("Congratulations! You have guessed the correct number!")
        break
else:
     print(f"Sorry! You have exceeded the number of guesses allowed! The correct number was {secret_number}")
