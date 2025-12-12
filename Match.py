#This program is answer to Exercise: Day of the Week
def DayOftheWeek():
    match num:
        case 1:
            print("Monday!")
        case 2:
            print("Tuesday!")
        case 3:
            print("Wednesday!")
        case 4:
            print("Thursday!")
        case 5:
            print("Friday!")
        case 6:
            print("Saturday!")
        case 7:
            print("Sunday!")
        case _: # Default case if no case matches
            print("Invalid day number!")

num = int(input("Enter a number between 1–7: "))
print("Day:", end = " ")
DayOftheWeek()
