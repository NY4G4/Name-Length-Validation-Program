command = "" # stores the commands entered by the user
car_started = False # describes the state of the car (whether it is started or not)

while True:
    command = input("> ").lower()
    if command == "start":
        if car_started: # checks if the car has already started
            print("The car has already started!")
        else:
            car_started = True # starts the car
            print("The car is starting...")
            print("The car has started.")
    elif command == "stop":
        if not car_started: # checks if the car has already stopped
            print("The car has already stopped!")
        else:
            car_started = False # stops the car
            print("The car is stopping...")
            print("The car has stopped.")
    elif command == "help":
        print("""
start - starts the car
stop - stops the car
quit - exits the simulator
        """)
    elif command == "quit":
        break
    else:
        print("I don't understand the command you entered. Please enter 'help' for a list of valid commands.")


