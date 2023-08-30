num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /, %): ")

# Perform the operation based on the operator

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
elif operator == "%":
    result = num1 % num2
else:
    print("Invalid operator")
    exit()


# Display the result
print(f"{num1:.2f} {operator} {num2:.2f} = {result:.2f}")