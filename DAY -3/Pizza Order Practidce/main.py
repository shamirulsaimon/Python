
print("Welscome To Pizza Delveries")
size = input("Please Enter The Size Of Your Pizza ? S,M,L")
pepperoni = input("Do You Want To Add Pepperoni In your Pizza? Y/N")
extra_cheese = input("Do You want to add Extra Cheese In Your Pizza? Y/N")
bill = 0
if size =="S":
    bill +=15
elif size == "M":
    bill +=20
else:
    bill +=25

if pepperoni =="Y":
   if size =="S":
       bill +=2
else:
    bill +=3

if extra_cheese =="Y":
    bill +=1


print(f"Your Bill Will be {bill}")

