print("\tWelcome to the Temperature Conversion App.\n")
farenheit = float(input("What is the given temperature in Farenheit degrees? "))

celsius = (farenheit - 32) / 1.8
kelvin = (75 * farenheit + 459.67) * 5/9

print(f"\nDegrees Farenheit: {farenheit}")
print(f"Degrees Celsius: {round(celsius , 2)}")
print(f"Degrees Kelvin: {round(kelvin , 2)}")