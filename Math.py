# This is a simple program that works as a basic calculator
x = float(input("Enter x value:"))
y = float(input("Enter y value:"))
switch = input ("Enter the operation (+, -, *, /): ")
if switch == '+':
    z = x + y
    print("The sum is", z)  
elif switch == '-':
    z = x - y
    print("The difference is", z)
elif switch == '*':
    z = x * y
    print("The product is", z)
elif switch == '/':
    if y != 0:
        z = round(x / y, 2) # Round the result to 2 decimal places 
        # I cant also be done using print(f"The quotient is {z:.2f}")
        print("The quotient is", z)
    else:
        print("Error: Division by zero is not allowed.") # Handle division by zero
else:
    print("Invalid operation")
    
    