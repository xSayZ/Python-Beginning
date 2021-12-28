# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

height = input("Enter your height in metres: ")
weight = input("Enter your weight in kgs: ")

BMI = int(weight) / float(height) ** 2
BMI_as_int = int(BMI)
print(BMI_as_int)

if BMI < 18.5:
    print("You are underweight.")
elif BMI < 25:
    print("You have a normal weight.")
elif BMI < 30:
    print("You are slightly overweight.")
elif BMI < 35:
    print("You are obese.")
else:
    print("You are clinically obese.")