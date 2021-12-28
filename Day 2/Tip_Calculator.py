#If the bill was $150.00, split between 5 people, 12% tip.
#Each person should pay (150.00/5) * 1.12
#Round the result to 2 decimal places

print("Welcome to the tip calculcator")

total_bill = float(input("What was the total bill? $"))

tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
amount_of_people = int(input("How many people want to split the bill? "))

total_tip_percentage = tip_percentage / 100
total_tip_amount = total_bill * total_tip_percentage
total_bill_amount = total_bill + total_tip_amount
bill_per_person = total_bill_amount / amount_of_people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: {final_amount}")


