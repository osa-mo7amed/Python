#This program is answer to: Even or Odd Checker
#Write a function that takes a number and prints whether it is even or odd.
#Use a loop to test it on numbers from 1 to 20.
num = int(input("Enter a number: "))

if (num%2 == 0):
    print("The num is even!")

elif (num%2 != 0):
    print("The number is odd!")
     
else:
    print("Invalid input!")
    
#This program is answer to:Multiplication Table
#Write a function that prints the multiplication table (1–10) for any number entered by the user.
#Example: if user enters 5, output 5 x 1 = 5 … 5 x 10 = 50.
n = int(input("Enter a number: "))

for i in range(10):
    print((i+1), " x", n, " = ", n * (i+1))
    i = i+1
    
#This program is answer to: Sum of Natural Numbers
#Ask the user for m.
#Write a function that uses a loop to calculate the sum 1 + 2 + 3 + ... + m.
#Print the result.
def sum_natural(m):
    total = 0
    for i in range(1, m + 1):
        total += i
    return total

m = int(input("Enter a positive number: "))
print(f"The sum of natural numbers from 1 to {m} is {sum_natural(m)}")
