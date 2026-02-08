reached = False

while not reached:
    print("Keep Driving...")
    
    userInput = input("Have you reached your destination? (yes/no): ")
    if userInput.lower() == "yes":
        reached = True
        print("Congratulations! You've reached your destination.")