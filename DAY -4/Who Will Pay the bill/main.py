import random

names_string = input("Enter The Names : ")

names = names_string.split(",")

num_item = len(names)

random_choise = random.randint(0,num_item -1)

who = names[random_choise]

print(f"{who} is going to pay the bill Today")

