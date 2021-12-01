print("\tWelcome to the Right Triangle Solver App.\n")
firstleg = float(input("What is the lenght of the first leg? "))
secondleg = float(input("What is the lenght of the second leg? "))

hypotenuse = (firstleg ** 2 + secondleg ** 2) ** 0.5
area = (firstleg * secondleg) / 2

print(f"The hypotenuse of the triangle is {round (hypotenuse , 2)} cm")
print(f"The area of the triangle is {round(area , 2)} m²")