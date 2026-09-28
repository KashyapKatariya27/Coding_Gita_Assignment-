"""Topic 6: Nested if-elif-else (Q44-Q49). Answer each prompt in order."""

# Q44 Greatest of Three Numbers; ties are handled explicitly.
a = int(input("Q44 - A: "))
b = int(input("Q44 - B: "))
c = int(input("Q44 - C: "))
if a == b and b == c:
    print("All are Equal")
elif a == b:
    if a > c:
        print("A and B are Equal and Greatest")
    else:
        print("C is Greatest")
elif a == c:
    if a > b:
        print("A and C are Equal and Greatest")
    else:
        print("B is Greatest")
elif b == c:
    if b > a:
        print("B and C are Equal and Greatest")
    else:
        print("A is Greatest")
elif a > b:
    if a > c:
        print("A is Greatest")
    else:
        print("C is Greatest")
elif b > c:
    print("B is Greatest")
else:
    print("C is Greatest")

# Q45 Student Result with Grade
marks = float(input("Q45 - Marks: "))
attendance = float(input("Q45 - Attendance: "))
if attendance >= 75:
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 60:
        print("Grade C")
    elif marks >= 40:
        print("Grade D")
    else:
        print("Grade F")
else:
    print("Not Eligible")

# Q46 Employee Bonus
salary = float(input("Q46 - Salary: "))
rating = int(input("Q46 - Performance rating: "))
if salary >= 30000:
    if rating == 5:
        print("Bonus: 20%")
    elif rating == 4:
        print("Bonus: 15%")
    elif rating == 3:
        print("Bonus: 10%")
    else:
        print("Bonus: 5%")
else:
    print("Not Eligible for Bonus")

# Q47 Bus Ticket Category
age = int(input("Q47 - Age: "))
distance = float(input("Q47 - Distance in km: "))
if age < 5:
    print("Free")
elif age >= 60:
    print("Senior")
else:
    if distance <= 10:
        print("Regular - Short Distance")
    else:
        print("Regular - Long Distance")

# Q48 Product Purchase Validation
stock = int(input("Q48 - Stock quantity: "))
payment_status = input("Q48 - Payment status: ")
if stock > 0:
    if payment_status == "paid":
        print("Order Confirmed")
    elif payment_status == "pending":
        print("Payment Pending")
    else:
        print("Invalid Payment Status")
else:
    print("Out of Stock")

# Q49 Travel Ticket Validation
age = int(input("Q49 - Age: "))
ticket_type = input("Q49 - Ticket type (AC/Sleeper): ")
if age < 5:
    print("Free Travel")
elif age >= 60:
    print("Senior Passenger")
else:
    if ticket_type == "AC":
        print("AC Ticket")
    elif ticket_type == "Sleeper":
        print("Sleeper Ticket")
    else:
        print("Invalid Ticket Type")
