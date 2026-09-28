"""Topic 8: Conditional statements with earlier concepts (Q58-Q68)."""

# Q58 Student ID Validation
student_id = input("Q58 - Student ID (DEGREE-BATCH-BRANCH-ROLL): ")
parts = student_id.split("-")
degree = parts[0]
batch = parts[1]
branch = parts[2]
roll_number = parts[3]
if branch == "CSE":
    print("CSE Student")
else:
    print("Non-CSE Student")

# Q59 Email Domain Checker
email = input("Q59 - Email address: ")
email_parts = email.split("@")
domain = email_parts[1]
if domain == "gmail.com":
    print("Gmail User")
else:
    print("Other Email Provider")

# Q60 Username Generator Validation
full_name = input("Q60 - Enter a three-word full name: ")
name_parts = full_name.split()
generated_username = name_parts[0] + "." + name_parts[2]
if "." in generated_username:
    print("Valid Username Format")
else:
    print("Invalid Username Format")

# Q61 Number Digit Analyzer (positive integer)
number = int(input("Q61 - Positive integer: "))
if number < 10:
    print("One Digit")
elif number < 100:
    print("Two Digits")
elif number < 1000:
    print("Three Digits")
else:
    print("Four or More Digits")

# Q62 Shopping Bill Category
price = float(input("Q62 - Product price: "))
quantity = int(input("Q62 - Quantity: "))
subtotal = price * quantity
if subtotal >= 5000:
    discount_percent = 20
elif subtotal >= 2000:
    discount_percent = 10
else:
    discount_percent = 0
discount = subtotal * discount_percent / 100
final_amount = subtotal - discount
print(f"Subtotal: {subtotal:g}, Discount: {discount_percent}%, Final: {final_amount:.2f}")

# Q63 Electricity Bill Category (single rate applied to all units)
units = float(input("Q63 - Units consumed: "))
if units <= 100:
    rate = 5
elif units <= 300:
    rate = 7
else:
    rate = 10
bill = units * rate
print(f"Units: {units:g}")
print(f"Rate: ₹{rate}, Bill: ₹{bill:g}")

# Q64 ATM Menu
balance = 10000
print("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
choice = int(input("Q64 - Choice: "))
match choice:
    case 1:
        print(f"Balance: {balance}")
    case 2:
        deposit = float(input("Deposit amount: "))
        balance += deposit
        print(f"Deposit Successful, Balance: {balance:g}")
    case 3:
        withdrawal = float(input("Withdrawal amount: "))
        if withdrawal <= balance:
            balance -= withdrawal
            print(f"Withdrawal Successful, Balance: {balance:g}")
        else:
            print("Insufficient Balance")
    case 4:
        print("Exit")
    case _:
        print("Invalid Choice")

# Q65 Restaurant Ordering System
item = int(input("Q65 - Item (1 Pizza, 2 Burger, 3 Pasta, 4 Sandwich): "))
quantity = int(input("Quantity: "))
match item:
    case 1:
        item_name, price = "Pizza", 250
    case 2:
        item_name, price = "Burger", 150
    case 3:
        item_name, price = "Pasta", 200
    case 4:
        item_name, price = "Sandwich", 120
    case _:
        item_name, price = "Invalid Item", 0
if price == 0:
    print("Invalid Choice")
else:
    total = price * quantity
    if total >= 500:
        discount = total * 0.10
    else:
        discount = 0
    print(f"{item_name} Total: {total}, Discount: {discount:.2f}, Final: {total - discount:.2f}")

# Q66 Exam Result Analyzer
m1 = float(input("Q66 - Subject 1 marks: "))
m2 = float(input("Subject 2 marks: "))
m3 = float(input("Subject 3 marks: "))
attendance = float(input("Attendance: "))
total = m1 + m2 + m3
average = total / 3
if attendance >= 75:
    if average >= 90:
        print("Outstanding")
    elif average >= 75:
        print("Very Good")
    elif average >= 60:
        print("Good")
    elif average >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not Eligible")

# Q67 Cab Fare Calculator
distance = float(input("Q67 - Distance in km: "))
ride_type = input("Ride type (normal/premium): ")
match ride_type:
    case "normal":
        rate = 15
    case "premium":
        rate = 25
    case _:
        rate = 0
if rate == 0:
    print("Invalid Ride Type")
else:
    fare = distance * rate
    if distance > 20:
        fare = fare * 1.10
    print(f"Fare: {fare:.2f}")

# Q68 College Admission System
score = float(input("Q68 - Entrance score: "))
percentage = float(input("12th percentage: "))
category = input("Category (general/obc/sc): ")
match category:
    case "general":
        required_score, required_percentage = 80, 75
    case "obc":
        required_score, required_percentage = 70, 70
    case "sc":
        required_score, required_percentage = 60, 60
    case _:
        required_score, required_percentage = 101, 101
if score >= required_score:
    if percentage >= required_percentage:
        print("Admission Eligible")
    else:
        print("Admission Not Eligible")
else:
    print("Admission Not Eligible")
