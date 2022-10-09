height = float(input("What is your height in meters : "))

weight = float(input("What is your weight in KG : "))

bmi = round((weight/height**2),2)

if bmi<18.5:
    print(f"your BMI is {bmi} and you are under weight")
elif bmi<25:
    print(f"your BMI is {bmi} and you have normal weight")
elif bmi>30:
    print(f"your BMI is {bmi} you are obese")
elif bmi<35:
    print(f"your BMI is {bmi} you are obese")
else:
    print(f"Your BMI is {bmi} above 35 yoe are clinically obese")