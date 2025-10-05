#This code shows how to use Exception and prcatising functions and fundamentals
def main():
    print("\t\tCreate an account\n")
    
    Un = input("Enter your username: ").strip().lower() 
    
    while True:
        if len(Un) < 5:
            print("Username must be at least 5 characters")
            Un = input("Enter your username: ").strip().lower()
        else:
            break
    
    U = pin("Enter pin(****): ")
    
    while True:
        if len(str(U)) != 4:
            print("Pin must be 4 digits")
            U = pin("Enter pin(****): ")
        else:
            break

    print("Account created successfully")
    print(f"Your username is {Un} and your pin is {U}")
    print("Please remember your username and pin")
    print("You will need them to log in")
    print()
    
    print("Now you can log in")
    
    print("\t\tLog in\n")
    
    Un1 = input("Enter your username: ").strip().lower()
    while True:
        if Un1 != Un:
            print("Access denied")
            Un1 = input("Enter your username: ").strip().lower()
        else:
            print("Access granted")
            break
        
    U1 = pin("Enter pin(****): ")
   
    while True:
        if U1 != U:
            print("Access denied")
            U1 = pin("Enter pin(****): ")
        else:
            break
    

def pin(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid pin use numbers only!")
            
main()