def main(): 
    x = float(input("Enter the value of x : "))
    
    switch = input("Enter your operation(square or root): ").strip().lower()
    
    if switch == "square":
        print("The x squared is", square(x))
    
    elif switch == "root":
        print("The x root is", root(x))

    else: 
        print("Invalid operation!")

def square(n):
    return n * n
    # I can also use math.pow(n, m)

def root(n):
    return n ** 0.5 #The ** mean n to the power of 0.5
    # I can also use math.sqrt(n, m)
main() 