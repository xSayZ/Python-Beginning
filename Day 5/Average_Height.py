student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0

'# Counts the total height and adds them to total_height'
for student_height in student_heights:
    total_height += student_height

print(f"Total height is: {total_height}")

number_of_students = 0

'# Counts the amount of students in the list and adds one'
for students in student_heights:
    number_of_students += 1

'# Calculates the average height by subtracting the total height by the number of students'
'# and rounds it off at the end.'
average_height = (total_height / number_of_students).__round__()

print(f"Average height is: {average_height}")