"""Topic 4: Logical conditions (Q29-Q35). Answer each prompt in order."""

# Q29 College Admission Eligibility
marks = float(input("Q29 - Marks: "))
attendance = float(input("Q29 - Attendance: "))
if marks >= 60 and attendance >= 75:
    print("Eligible")
else:
    print("Not Eligible")

# Q30 Scholarship Eligibility
marks = float(input("Q30 - Marks: "))
income = float(input("Q30 - Family income: "))
if marks >= 85 or income < 300000:
    print("Scholarship Available")
else:
    print("No Scholarship")

# Q31 Weekend Check
day = input("Q31 - Day name: ")
if day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Weekday")

# Q32 Online Exam Access
username = input("Q32 - Username: ")
password = input("Q32 - Password: ")
if username == "student" and password == "python123":
    print("Access Granted")
else:
    print("Access Denied")

# Q33 Delivery Availability
city = input("Q33 - City: ")
if city == "Ahmedabad" or city == "Gandhinagar":
    print("Delivery Available")
else:
    print("Delivery Unavailable")

# Q34 Number Range Check
number = int(input("Q34 - Integer: "))
if number >= 10 and number <= 50:
    print("Inside Range")
else:
    print("Outside Range")

# Q35 Secure Transaction
amount = float(input("Q35 - Amount: "))
otp = input("Q35 - OTP: ")
if amount <= 50000 and otp == "1234":
    print("Transaction Approved")
else:
    print("Transaction Declined")
