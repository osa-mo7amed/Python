#This program is writing a array 3*3
# Initialize the 3x3 array first
array = [[0 for j in range(3)] for i in range(3)]

# Input values into array
for i in range(3):
    for j in range(3):
        array[i][j] = input(f"Enter {i+1}x{j+1}: ")

# Print the entire array
for i in range(3):
    for j in range(3):
        print(array[i][j], end=" ")
    print()  # New line after each row