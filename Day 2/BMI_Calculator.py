height = input("Enter your height in metres: ")
weight = input("Enter your weight in kgs: ")


BMI = int(weight) / float(height) ** 2
BMI_as_int = int(BMI)
print(BMI_as_int)