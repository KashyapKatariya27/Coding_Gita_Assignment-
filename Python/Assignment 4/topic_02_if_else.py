"""Topic 2: if-else statements (Q9-Q18). Answer each prompt in order."""

# Q9 Even or Odd
number = int(input("Q9 - Integer: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Q10 Pass or Fail
marks = float(input("Q10 - Marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")

# Q11 Adult or Minor
age = int(input("Q11 - Age: "))
if age >= 18:
    print("Adult")
else:
    print("Minor")

# Q12 Number Sign
number = int(input("Q12 - Integer: "))
if number > 0:
    print("Positive")
else:
    print("Non-Positive")

# Q13 Divisible by 3
number = int(input("Q13 - Integer: "))
if number % 3 == 0:
    print("Divisible by 3")
else:
    print("Not Divisible by 3")

# Q14 Login Password
correct_password = "python123"
password = input("Q14 - Password: ")
if password == correct_password:
    print("Login Successful")
else:
    print("Invalid Password")

# Q15 Username Check
username = input("Q15 - Username: ")
if username == "admin":
    print("Welcome Admin")
else:
    print("Invalid Username")

# Q16 Greater Between Two Numbers
a = int(input("Q16 - First integer: "))
b = int(input("Q16 - Second integer: "))
if a > b:
    print(a)
elif b > a:
    print(b)
else:
    print("Both are Equal")

# Q17 Hot or Comfortable
temperature = float(input("Q17 - Temperature in Celsius: "))
if temperature > 30:
    print("Hot")
else:
    print("Comfortable")

# Q18 Shopping Discount Eligibility
amount = float(input("Q18 - Shopping amount: "))
if amount >= 5000:
    print("Discount Available")
else:
    print("No Discount")
