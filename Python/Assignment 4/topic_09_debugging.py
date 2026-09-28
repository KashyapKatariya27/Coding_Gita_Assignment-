"""Topic 9: Debugging conditional programs (Q69-Q70)."""

# Q69: input() returns text, so convert the age to int before comparing it.
age = int(input("Q69 - Enter age: "))
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

# Q70: the original code handles 90+ and 75-89, but has no branch for
# marks from 40 through 74. Add a passing fallback inside the outer condition.
marks = int(input("Q70 - Enter marks: "))
if marks >= 40:
    if marks >= 90:
        print("A")
    elif marks >= 75:
        print("B")
    else:
        print("Pass")
else:
    print("Fail")
