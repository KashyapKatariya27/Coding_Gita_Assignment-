"""Topic 5: Nested if statements (Q36-Q43). Answer each prompt in order."""

# Q36 Login with Role
username = input("Q36 - Username: ")
password = input("Q36 - Password: ")
if username == "admin":
    if password == "admin123":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")

# Q37 Driving License Eligibility
age = int(input("Q37 - Age: "))
test_status = input("Q37 - Test status (pass/fail): ")
if age >= 18:
    if test_status == "pass":
        print("License Approved")
    else:
        print("Test Not Passed")
else:
    print("Age Not Eligible")

# Q38 ATM Withdrawal
balance = float(input("Q38 - Account balance: "))
withdrawal = float(input("Q38 - Withdrawal amount: "))
if withdrawal <= balance:
    if withdrawal % 100 == 0:
        print("Withdrawal Successful")
    else:
        print("Enter Amount in Multiples of 100")
else:
    print("Insufficient Balance")

# Q39 Exam Result with Attendance
marks = float(input("Q39 - Marks: "))
attendance = float(input("Q39 - Attendance: "))
if attendance >= 75:
    if marks >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not Eligible Due to Attendance")

# Q40 Bank Account Verification
account_type = input("Q40 - Account type: ")
balance = float(input("Q40 - Balance: "))
if account_type == "savings":
    if balance >= 1000:
        print("Minimum Balance Maintained")
    else:
        print("Minimum Balance Not Maintained")
else:
    print("Unsupported Account")

# Q41 Online Shopping Eligibility
amount = float(input("Q41 - Order amount: "))
method = input("Q41 - Payment method: ")
if amount >= 500:
    if method == "card":
        print("Card Payment Accepted")
    elif method == "upi":
        print("UPI Payment Accepted")
    else:
        print("Unsupported Payment Method")
else:
    print("Minimum Order Amount Not Reached")

# Q42 Hostel Room Allocation
year = int(input("Q42 - Year of study: "))
attendance = float(input("Q42 - Attendance: "))
if year == 2 or year == 3 or year == 4:
    if attendance >= 75:
        print("Room Eligible")
    else:
        print("Attendance Too Low")
else:
    print("Not Eligible by Year")

# Q43 Internet Plan Upgrade
plan = input("Q43 - Current plan: ")
usage = float(input("Q43 - Monthly usage in GB: "))
if plan == "basic":
    if usage > 100:
        print("Recommend Upgrade")
    else:
        print("Basic Plan Is Sufficient")
else:
    print("Already on Higher Plan")
