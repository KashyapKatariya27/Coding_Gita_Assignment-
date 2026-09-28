"""Topic 7: match-case (Q50-Q57). Requires Python 3.10+. Answer in order."""

# Q50 Basic Menu
choice = int(input("Q50 - Choice (1-4): "))
match choice:
    case 1: print("Add")
    case 2: print("View")
    case 3: print("Update")
    case 4: print("Delete")
    case _: print("Invalid Choice")

# Q51 Day Name
day = int(input("Q51 - Day number (1-7): "))
match day:
    case 1: print("Monday")
    case 2: print("Tuesday")
    case 3: print("Wednesday")
    case 4: print("Thursday")
    case 5: print("Friday")
    case 6: print("Saturday")
    case 7: print("Sunday")
    case _: print("Invalid Day")

# Q52 Calculator
a = float(input("Q52 - First number: "))
b = float(input("Q52 - Second number: "))
operator = input("Q52 - Operator (+, -, *, /): ")
match operator:
    case "+": print(a + b)
    case "-": print(a - b)
    case "*": print(a * b)
    case "/":
        if b == 0:
            print("Cannot divide by zero")
        else:
            print(a / b)
    case _: print("Invalid Operator")

# Q53 Traffic Signal
signal = input("Q53 - Signal color: ")
match signal:
    case "red": print("Stop")
    case "yellow": print("Wait")
    case "green": print("Go")
    case _: print("Invalid Signal")

# Q54 Grade Message
grade = input("Q54 - Grade: ")
match grade:
    case "A": print("Excellent Performance")
    case "B": print("Very Good Performance")
    case "C": print("Good Performance")
    case "D": print("Needs Improvement")
    case "F": print("Failed")
    case _: print("Invalid Grade")

# Q55 Mobile Service Menu
service = int(input("Q55 - Service code: "))
match service:
    case 1: print("Check Balance")
    case 2: print("Recharge")
    case 3: print("Data Usage")
    case 4: print("Customer Support")
    case _: print("Invalid Service")

# Q56 Month Name
month = int(input("Q56 - Month number (1-12): "))
match month:
    case 1: print("January")
    case 2: print("February")
    case 3: print("March")
    case 4: print("April")
    case 5: print("May")
    case 6: print("June")
    case 7: print("July")
    case 8: print("August")
    case 9: print("September")
    case 10: print("October")
    case 11: print("November")
    case 12: print("December")
    case _: print("Invalid Month")

# Q57 File Type Detector
extension = input("Q57 - File extension (without dot): ")
match extension:
    case "py": print("Python File")
    case "txt": print("Text File")
    case "pdf": print("PDF File")
    case "jpg": print("Image File")
    case _: print("Unknown File Type")
