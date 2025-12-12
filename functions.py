# This program draws a face based on the user's mood input usinf functions
def forehead():
    print("*************")
    print("*           *")

def eyes1():
    print("*   >   <   *")
    print("*   0   0   *")
    print("*           *")

def eyes2():
    print("*   _   _   *")
    print("*   0   0   *")
    print("*           *")

def nose():
    print("*     ^     *")

def mouth1():
    print("*    ___    *")
    print("*   '   '   *")
    print("*************")

def mouth2():
    print("*    ---    *")
    print("*           *")
    print("*************")

switch = ("which mood are you in? (serious or angery): ")
mood = input(switch).strip().lower()

if mood == "angery":
    forehead()
    eyes1()
    nose()
    mouth1()

elif mood == "serious":
    forehead()
    eyes2()
    nose()
    mouth2()
    
else:
    print("Invalid mood. Please choose 'serious' or 'angery'.")
    