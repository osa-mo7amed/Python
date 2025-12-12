#This code creates a 2D array based on user-defined dimensions and then prints the array in a structured format.
u = int(input("raws: "))
k = int(input("colums: "))
print()

array = [[0 for j in range(u)] for i in range(k)]

for i in range(u):
    for j in range(k):
        array[i][j] = input(f"Enter {i+1}x{j+1}: ")

for i in range(u):
    for j in range(k):
        print(array[i][j], end = " ")
    print()