def prime(number):
    prime_number = True
    for i in range(2,number):
        if number%i==0:
            prime_number = False
    if prime_number:
        print("It is a prime Number")
    else:
        print("It is not a prime number")
            
num = int(input("Enter The Number You Want To Cheek: "))
prime(number = num)