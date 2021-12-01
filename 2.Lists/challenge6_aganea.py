print("¡Welcome to the Grade Sorter App!\n")

nota1 = int(input("What is your first grade?(0-100) "))
nota2 = int(input("What is your second grade?(0-100) "))
nota3 = int(input("What is your third grade?(0-100) "))
nota4 = int(input("What is your fourth grade?(0-100) "))

notas = [nota1 , nota2, nota3, nota4]
print(f"\nYour grades are {notas}")
notas.sort()
print(f"Your grades from the highest to the lowest are: {notas}")

print(f"\nThe lowest two grades will now be dropped.")
print(f"Removed grade: {notas.pop(0)}")
print(f"Removed grade: {notas.pop(0)}")

print(f"\nYour remaining grades are: {notas}")

print(f"\nNice work! Your highest grade is a {notas[1]}")