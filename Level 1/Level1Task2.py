def convert_temp(temp, unit):
    if unit == "C":
        return round((temp * 9/5) + 32, 2)
    elif unit == "F":
        return round((temp - 32) * 5/9, 2)
    else:
        return "Invalid unit"

# the user to enter a temperature value and the unit of measurement
temp = float(input("Enter temperature: "))
unit = input("Enter unit (C or F): ")
if unit == "C":
    print(f"{temp}°{unit} is equal to {convert_temp(temp, unit)}°F")
elif unit == "F":
    print(f"{temp}°{unit} is equal to {convert_temp(temp, unit)}°C")
else:
    print("Invalid unit")