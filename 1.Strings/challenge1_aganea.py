print("\tWelcome to letter counter app!")
name = input("Whats your name? ").title()
print(f"Hello {name}! \nI will count the number of times that a specific letter occurs in your message.")

message = input("Please enter a message: ").lower()
letter = input("Wich letter would you like to count the occurences of? ").lower()

number = 0

for x in range (len(message)):
    if message[x] == letter:
        number += 1
print(f"{name} your phrase has {number}{letter}'s in it.")