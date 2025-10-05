#This program shows how lists works and the best way to put  
Students = ["Osama", "Mohammed", "Ali", "Abdaslam", "Alfahal"]
Age = [21, 20, 22, 20, 19]
i = 0

for student in Students:
    print(student, Age[i])
    i = i + 1
    
print()

#Another way using range and len
for i in range(len(Students)):
    print(i+1, Students[i], Age[i])

print()

#Another way using dictionary
students = {
    "Osama": 21,
    "Mohammed": 20, 
    "Ali": 22,
    "Abdaslam": 20,
    "Alfahal": 19
}
for student in students:
    print(student, students[student], sep=", ") #Another way using sep parameter in print function
