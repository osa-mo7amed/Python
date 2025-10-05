#This code adds two 3x3 arrays element-wise and prints the resulting array.
array1 = [[0 for j in range(3)] for i in range(3)]
array2 = [[0 for j in range(3)] for i in range(3)]

for i in range(3):
    for j in range(3):
        array1[i][j] = int(input(f"Enter {i+1}x{j+1}: "))

print()

for i in range(3):
    for j in range(3):
        array2[i][j] = int(input(f"Enter {i+1}x{j+1}: "))

print("The result: ")

for i in range(3):
    for j in range(3):
        print(array1[i][j]+array2[i][j], end = " ")
    print()
