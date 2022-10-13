print("Welcome To Pizza Deliver ")
size = input("What Size pizza you want? S , M , L : \n")
pepperoni = input("Do you want Peeperoni In your Pizza? Y/N : \n")
chesees = input("Do ypu want Extra chesees In your Pizza? Y/N : \n")
bill = 0
bill_s = 0
bill_m = 0

if size =="S":
    bill_s =15
    if pepperoni =="Y":
        bill_s += 2
    else:
        bill_s =15
    if chesees =="Y":
        bill_s +=1
        print(f"Your Bill Is {bill_s}")
    else:
        print(f"Your Bill  is {bill_s}")


if size =="M":
    bill_m =20
    if pepperoni =="Y":
        bill_m += 3
    else:
        bill_m = 20
    if chesees =="Y":
        bill_m +=1
        print(f"Your Bill Is {bill_m}")
    else:
        print(f"Your Bill  is {bill_m}")
        
        

if size =="L":
    bill =25
    if pepperoni =="Y":
        bill += 3
    else:
        bill = 25
    if chesees =="Y":
        bill +=1
        print(f"Your Bill Is {bill}")
    else:
        print(f"Your Bill  is {bill}")