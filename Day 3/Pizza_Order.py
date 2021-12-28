
print("Welcome to Python Pizza Deliveries")

size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# Prices
small_size = 15
medium_size = 20
large_size = 25

small_pepperoni = 2
other_pepperoni = 3
cheese_int = 1

if size == "S":
    bill = small_size
    if add_pepperoni == "Y":
        bill += small_pepperoni

if size == "M":
    bill = medium_size
    if add_pepperoni == "Y":
        bill += other_pepperoni

else:
    bill = large_size
    if add_pepperoni == "Y":
        bill += other_pepperoni

if extra_cheese == "Y":
    bill += cheese_int

print(f"Your final bill is: ${bill}")

