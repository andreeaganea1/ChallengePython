print("\tWelcome to the Favorite Teachers Program.\n")

first = input("Who is your favorite teacher? ").title()
second = input("Who is your second favorite teacher? ").title()
third = input("Who is your third favorite teacher? ").title()
fourth = input("Who is your fourth favorite teacher? ").title()

lista = [first, second, third, fourth]

print(f"Your favorite teachers ranked are: {lista}")
print(f"Your favorite teachers in alphabetic order are: {lista.sort()}")
print(f"Your favorite teachers in reverse alphabetic order are: {lista.sort(reverse = True)}")
