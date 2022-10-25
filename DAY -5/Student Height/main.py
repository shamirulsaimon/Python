student_heights = input("Input a list of student heights: ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  
total_height = 0
for height in student_heights:
    total_height += height
    
print(f"Total Height Of the Student is {total_height}")

number_of_student = 0
for student in student_heights:
    number_of_student +=1

print(f"Number Of Students Heights are {number_of_student}")

# average = "{:.2f}".format(total_height/number_of_student)
average = round((total_height/number_of_student))

print(f"The Average Height Of The Students are {average}")