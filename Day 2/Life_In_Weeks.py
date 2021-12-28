

age = input("What is your current age?: ")

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12


print(f"You have {days_remaining} days remaining, {weeks_remaining} weeks remaining and {months_remaining} months left or {years_remaining} years left")