print("Welcome To The Love Calculator")

name = input("What is your name : ")
name2 = input("What is His/Her name : ")


combain_string = name + name2

lower_case = combain_string.lower()

t = lower_case.count("t")
u = lower_case.count("u")
r = lower_case.count("r")
e = lower_case.count("e")

true = t+u+r+e

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
E = lower_case.count("E")

love = l + o + v + E

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90 :
    print(f"Your love score is {love_score} . you go together like coke and mentos")
elif love_score>=40 and love_score<=50:
        print(f"You score is {love_score} . You are alright together")
else:
    print(f"Your score is {love_score} ")

