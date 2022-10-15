import random

import my_module

random_interger = random.randint(1,100) #randint(a,b) generate random integer number between a and b

print(random_interger)

print(my_module.pi)

#0.00000000000 - 0.99999999999

random_float = random.random() * 5

print(random_float)

love_score = random.randint(1,200)

print(f"Your Love Score is {love_score}")