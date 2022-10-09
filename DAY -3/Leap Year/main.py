print("Enter A year you want to check ?")
year = int(input("Enter A year: "))
if year%4==0:
    if year%100==0:
      if year%400==0:
       print("This is  a Leap year")
      else:
       print("This is not  a Leap year")
    else:
     print("This year is  a leap year")
else:
    print("This is not a Leap year")