total =0

for number in range(0,101):
    if number%2==0:
        total+=number
print(f"The Sum Of Even Number 1 To 100 {total}")


even=0

for number in range(2,101,2):
    even+=number

print(f"The Sum Of Even Number 1 To 100 {even}")