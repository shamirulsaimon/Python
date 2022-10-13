print("Welcome to Roller coaster!")
height = int(input("What is your height: "))
bill =0
if height>=120:
    print("You are able to ride roller coaster")
    age = int(input("Your age : "))
    if age<12:
        bill = 5
        print("Child ticket is $5")
    elif age<=18:
        bill = 7
        print("youth ticket is $7")
    else:
        bill = 12
        print("Adult Ticket is $12")
    photo = input("Do Yo want to take photo when you ride the roller coasrter... ? Y/N")
    if photo=="Y":
        bill += 3
        
    print(f"Your Total bill will be {bill}")
else:
    print("Sorry! You have to grow taller ")