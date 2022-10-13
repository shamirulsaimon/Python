print("Welcome to Pizza Deliveriers")
size = input("What size pizza Do want? S , M , L ")
pepperoni = input("Do You Want To Pepperoni? Y , N ")
cheese = input("Do You Want Extra Cheese In Pizza? Y , N ")
bill = 0
if size == "S":
   bill = 15
   print(f"Your Bill Is ${bill}")
elif size == "M":
    bill = 20
    print(f"Your Bill Is ${bill}")
else:
    bill = 25
    print(f"Your Bill Is ${bill}")


if size == "S":
    if pepperoni == "Y":
     bill +=2
     print(f"Your Bill Is ${bill}")
    if size == "M":
     bill +=3
     print(f"Your Bill Is ${bill}")
    if size == "L":
     bill +=3
     print(f"Your Bill Is ${bill}")
else:
    print(f"Your Bill Is ${bill}")

if cheese == "Y":
    bill+=1
    print(f"Your Bill Is ${bill}")
else:
    print(f"Your Bill Is ${bill}")