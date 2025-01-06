import os

# (Optional) Function for clearing the terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear') 

# Call the clear() function to clear the terminal
clear()

# Print "Hello World" to the terminal
print("Hello World!\n")
