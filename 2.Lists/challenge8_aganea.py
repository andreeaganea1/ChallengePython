import datetime
time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hours = str(time.day)
minute = str(time.minute)

print("Welcome to the Grocery List App.")
print(f"Current day and time: {month}/{day} {hours}:{minute}")
lista = ["Meat", "Cheese"]
print(f"You currently have {lista[0]} and {lista[1]} in your list.\n")

lista.append(str(input("Type of food to add to the grocery list: ")).title())
lista.append(str(input("Type of food to add to the grocery list: ")).title())
lista.append(str(input("Type of food to add to the grocery list: ")).title())

print(f"Here is your grocery list: {lista}")
lista.sort()
print(f"Here is your list sorted: {lista}\n")

print("Simulating grocery shopping...\n")

print(f"Current grocery list: {len(lista)} items.")
print(lista)
cosa = str(input("What item did you just buy? ")).title()
print(f"Removing {cosa} from list...\n")
lista.remove(cosa)

print(f"Current grocery list: {len(lista)} items.")
print(lista)
cosa = str(input("What item did you just buy? ")).title()
print(f"Removing {cosa} from list...\n")
lista.remove(cosa)

print(f"Current grocery list: {len(lista)} items.")
print(lista)
cosa = str(input("What item did you just buy? ")).title()
print(f"Removing {cosa} from list...\n")
lista.remove(cosa)

print(f"Current grocery list: {len(lista)} items.\n")
print(lista)
print(f"\nSorry the store is out of: {lista.pop(1)}")
lista.append(str(input("What item would you like instead?: ")).title())

print(f"Here is what remains in your grocery list: {lista}")