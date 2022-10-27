
def even_number():
    add = 0
    for number in range(0,100):  # for loop with range function
        if number % 2 ==0:
            add += number
            # prin(number)
    print(f"The Toatl of Even number from 1 to 100 are  {add}")

loop = 6
while loop > 0:   # while loop syntax
    even_number()
    loop-=1   
