print("\tWelcome to the basketball roster programm.\n")
roster = []

pointguard = input("Who is your point guard? ").title()
shootingguard = input("Who is your shooting guard? ").title()
smallforward = input("Who is your small forward? ").title()
powerforward = input("Who is your power forward? ").title()
center = input("Who is your center? ").title()

roster.append(pointguard)
roster.append(shootingguard)
roster.append(smallforward)
roster.append(powerforward)
roster.append(center)

print("\n\tYour starting five for the upcoming basketball season.\n")
print(f"\t\tPoint guard:\t\t{roster[0]}")
print(f"\t\tShooting guard:\t\t{roster[1]}")
print(f"\t\tSmall forward:\t\t{roster[2]}")
print(f"\t\tPower forward:\t\t{roster[3]}")
print(f"\t\tCenter:\t\t\t{roster[4]}\n")

injured_player = []
print(f"\nOh no, {smallforward} is injured.")
roster.remove(smallforward)
injured_player.insert(2, roster)
print(f"Your roster only has {len(roster)} players.")
added_player = input(f"Who will take {smallforward}'s spot? ").title()
roster.insert(2, added_player)

print("\n\tYour starting five for the upcoming basketball season.\n")
print(f"\t\tPoint guard:\t\t{roster[0]}")
print(f"\t\tShooting guard:\t\t{roster[1]}")
print(f"\t\tSmall forward:\t\t{roster[2]}")
print(f"\t\tPower forward:\t\t{roster[3]}")
print(f"\t\tCenter:\t\t\t{roster[4]}\n")

print(f"\nGood Luck {roster[2]}!")
print(f"Your roster has now {len(roster)}.")