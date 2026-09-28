"""Topic 3: if-elif-else (Q19-Q28). Answer each prompt in order."""

# Q19 Grade Calculator
marks = float(input("Q19 - Marks: "))
if marks >= 90 and marks <= 100:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("F")

# Q20 Temperature Category
t = float(input("Q20 - Temperature in Celsius: "))
if t >= 40:
    print("Very Hot")
elif t >= 30:
    print("Hot")
elif t >= 20:
    print("Warm")
else:
    print("Cold")

# Q21 Traffic Signal
signal = input("Q21 - Signal color (red/yellow/green): ")
if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Wait")
elif signal == "green":
    print("Go")
else:
    print("Invalid Signal")

# Q22 Electricity Usage
units = float(input("Q22 - Units: "))
if units <= 100:
    print("Low Usage")
elif units <= 300:
    print("Medium Usage")
elif units <= 500:
    print("High Usage")
else:
    print("Very High Usage")

# Q23 Movie Ticket Category
age = int(input("Q23 - Age: "))
if age < 5:
    print("Free Ticket")
elif age <= 12:
    print("Child Ticket")
elif age <= 59:
    print("Regular Ticket")
else:
    print("Senior Ticket")

# Q24 BMI Category
bmi = float(input("Q24 - BMI: "))
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

# Q25 Month Days
month = int(input("Q25 - Month number: "))
if month in (1, 3, 5, 7, 8, 10, 12):
    print("31 Days")
elif month in (4, 6, 9, 11):
    print("30 Days")
elif month == 2:
    print("28 or 29 Days")
else:
    print("Invalid Month")

# Q26 Simple Calculator
a = float(input("Q26 - First number: "))
b = float(input("Q26 - Second number: "))
operator = input("Q26 - Operator (+, -, *, /): ")
if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    if b == 0:
        print("Cannot divide by zero")
    else:
        print(a / b)
else:
    print("Invalid Operator")

# Q27 Day Number
day = int(input("Q27 - Day number (1-7): "))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid Day")

# Q28 Performance Level
score = float(input("Q28 - Score (0-100): "))
if score >= 90:
    print("Excellent")
elif score >= 75:
    print("Very Good")
elif score >= 60:
    print("Good")
elif score >= 40:
    print("Average")
else:
    print("Needs Improvement")
