"""Topic 1: Basic if statements (Q1-Q8). Run and answer each prompt in order."""

# Q1 Positive Number
number = int(input("Q1 - Integer: "))
if number > 0:
    print("Positive Number")

# Q2 Voting Eligibility
age = int(input("Q2 - Age: "))
if age >= 18:
    print("Eligible to Vote")

# Q3 Temperature Warning
temperature = float(input("Q3 - Temperature in Celsius: "))
if temperature > 40:
    print("High Temperature")

# Q4 Divisible by 5
number = int(input("Q4 - Integer: "))
if number % 5 == 0:
    print("Divisible by 5")

# Q5 Free Delivery
amount = float(input("Q5 - Order amount: "))
if amount >= 1000:
    print("Free Delivery")

# Q6 Character Check
character = input("Q6 - Character: ")
if character == "A":
    print("You entered A")

# Q7 Password Length
password = input("Q7 - Password: ")
if len(password) >= 8:
    print("Strong Length")

# Q8 Number of Digits (as specified, 100 through 999)
number = int(input("Q8 - Integer: "))
if 100 <= number <= 999:
    print("Three Digit Number")
