print("Welcome to the rollercoaster!")
print("Please Enter Your height")
height = int(input("Your height in CM : "))
if height >= 120:
    print("Yon can ride the rollarcoaster")
    age = int(input("What Is your age? "))
    if age<12:
        print("You have to pay $5 Dollar")
    elif age<=18:
        print("You have to pay $7 Dollar")
    else:
        print("You have to pay $12 Dollar")
else:
    print("Sorry!You have to grow taller")