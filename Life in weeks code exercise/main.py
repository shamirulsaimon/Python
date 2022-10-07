
age = input("What is your current age?  ")

age_as_int = int(age)

years_remaining = 90-age_as_int

days_remaining = years_remaining*365

months_remaining = years_remaining*12

week_remaining = years_remaining*52

message = f"you have {days_remaining} days ,{months_remaining} months and {week_remaining} weeks remaining  if live 90 years"

print(message)
