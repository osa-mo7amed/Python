#This code shows how to use Exception 
print("\t\tLog in\n")

input("Enter your username: ").strip().lower()
while True:
    try:
        int(input("Enter pin(****): "))
    except ValueError:
        pass
    else:
        break
print()
    
#Another way 
print("\t\tLog in\n")

input("Enter your username: ").strip().lower()
while True:
    try:
        int(input("Enter pin(****): "))
        break
    except ValueError:
        pass

print()

#Another way using functions and return not break
def main():
    print("\t\tLog in\n")
    
    input("Enter your username: ").strip().lower()
    
    U = pin("Enter pin(****): ")
    
def pin(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid pin!")
            
main()