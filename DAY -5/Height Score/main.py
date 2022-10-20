
student_scores = input("Enter The List Of Student Scores: ").split()

for n in range(0,len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

height_score = 0

for score in student_scores:
    if score>height_score:
        height_score = score
        
print(f"{height_score} Is the Height Score")


# max() is a function which help find maximum value 

# min() is a function which help find minimum value 