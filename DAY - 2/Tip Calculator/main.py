print("Welcome to Tip Calculator...")

bill = float(input("What was the total  bill ? $"))

tip = float(input("What percentage tip would you like to give? 10, 12 or 15 ? "))

people = int(input("How many people split the Bill ? "))

tip_as_persentage = tip/100

total_bill = tip_as_persentage * bill

total_bill_wth_tip = total_bill+bill

bill_per_person = total_bill_wth_tip/people

final_amount = round(bill_per_person, 2)

final_amount = "{:.2f}".format(bill_per_person)

print(f"Every Person Should Pay ${final_amount} dollar")

