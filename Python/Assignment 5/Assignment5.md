# Assignment 5 — Single `for` Loop: Solutions

**Rule followed everywhere:** exactly one `for` loop, no nested loops, no `while` / `break` / `continue`, no lists or functions.

> **Trick used in digit problems (no `while` allowed):** a number `n` can never have more than `n` digits, so `for _ in range(n)` is always enough iterations. Inside the loop, `if temp > 0:` makes sure we only process real digits. Each iteration takes `temp % 10` (last digit) and then does `temp //= 10` (drops it).

---

# Level 1 — Loop Thinking & `range()`

## Q1. Predict the Loop Values
```python
for i in range(2, 15, 3):
    print(i)
```
**Answer**
```text
2
5
8
11
14
```
Starts at 2, adds 3 each time, stops before reaching 15.

## Q2. Reverse `range()` Prediction
```python
for i in range(15, 2, -3):
    print(i)
```
**Answer**
```text
15
12
9
6
3
```
Starts at 15, subtracts 3 each time, stops before reaching 2.

## Q3. How Many Iterations?
```python
for i in range(4, 31, 5):
    print(i)
```
**Answer:** The loop runs **6 times**. Values of `i`: `4, 9, 14, 19, 24, 29` (the next value, 34, is beyond 31).

## Q4. Correct the Boundary
The stop value is *excluded*, so it must be `19` (or anything from 19 to 21).
```python
for i in range(3, 19, 3):
    print(i)
```
**Output**
```text
3
6
9
12
15
18
```

## Q5. Number and Distance from 20
```python
for i in range(5, 11):
    print(i, 20 - i)
```
**Output**
```text
5 15
6 14
7 13
8 12
9 11
10 10
```

## Q6. Number, Square and Cube
```python
for i in range(1, 7):
    print(i, i ** 2, i ** 3)
```
**Output**
```text
1 1 1
2 4 8
3 9 27
4 16 64
5 25 125
6 36 216
```

---

# Level 2 — Counting & Accumulation

## Q7. Sum of Numbers in a Range
```python
start, end = map(int, input().split())
total = 0
for i in range(start, end + 1):
    total += i
print(total)
```
`5 10` → `45`, `12 15` → `54`

## Q8. Count Multiples of 3
```python
n = int(input())
count = 0
for i in range(1, n + 1):
    if i % 3 == 0:
        count += 1
print(count)
```
`10` → `3`, `20` → `6`

## Q9. Sum of Multiples of 4
```python
n = int(input())
total = 0
for i in range(1, n + 1):
    if i % 4 == 0:
        total += i
print(total)
```
`20` → `60`, `30` → `112`

## Q10. Count Numbers Divisible by Both 3 and 5
```python
n = int(input())
count = 0
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        count += 1
print(count)
```
`50` → `3`, `100` → `6`

## Q11. Sum Numbers Except Multiples of 3
```python
n = int(input())
total = 0
for i in range(1, n + 1):
    if i % 3 != 0:
        total += i
print(total)
```
`10` → `37` ✔
`15` → **`75`**

> ⚠️ **Note:** The assignment lists `80` for input `15`, but that appears to be a typo. Sum of 1..15 is 120, multiples of 3 add up to 45 (3+6+9+12+15), and 120 − 45 = **75**. The code is correct.

## Q12. Count Even and Odd Together
```python
n = int(input())
even = 0
odd = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even =", str(even) + ",", "Odd =", odd)
```
`10` → `Even = 5, Odd = 5`, `7` → `Even = 3, Odd = 4`

## Q13. Running Sum
```python
n = int(input())
total = 0
for i in range(1, n + 1):
    total += i
    print(total)
```
**Output (N=5)**
```text
1
3
6
10
15
```

## Q14. Running Product
```python
n = int(input())
product = 1
for i in range(1, n + 1):
    product *= i
    print(product)
```
**Output (N=5)**
```text
1
2
6
24
120
```

---

# Level 3 — Factorial & Product Logic

## Q15. Factorial of a Number
```python
n = int(input())
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)
```
`5` → `120`, `7` → `5040`

## Q16. Factorial from 1 to N
```python
n = int(input())
fact = 1
for i in range(1, n + 1):
    fact *= i
    print(str(i) + "! =", fact)
```
**Output (N=5)**
```text
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
```
Each factorial is built from the previous one, so one loop is enough.

## Q17. Product of Even Numbers
```python
n = int(input())
product = 1
for i in range(2, n + 1, 2):
    product *= i
print(product)
```
`10` → `3840`, `6` → `48`

## Q18. Product of Odd Numbers
```python
n = int(input())
product = 1
for i in range(1, n + 1, 2):
    product *= i
print(product)
```
`7` → `105`, `9` → `945`

## Q19. Double Factorial — Even Numbers
```python
n = int(input())
product = 1
for i in range(n, 0, -2):
    product *= i
print(product)
```
`8` → `384`, `10` → `3840`

## Q20. Sum of Squares
```python
n = int(input())
total = 0
for i in range(1, n + 1):
    total += i ** 2
print(total)
```
`5` → `55`, `10` → `385`

## Q21. Sum of Cubes
```python
n = int(input())
total = 0
for i in range(1, n + 1):
    total += i ** 3
print(total)
```
`4` → `100`, `5` → `225`

## Q22. Factorial-Based Sum
```python
n = int(input())
fact = 1
total = 0
for i in range(1, n + 1):
    fact *= i        # fact is now i!
    total += fact    # add i! to the sum
print(total)
```
`4` → `33`, `5` → `153`

---

# Level 4 — Number & Digit Logic

## Q23. Count Digits Using a Loop
```python
n = int(input())
temp = n
count = 0
for _ in range(n):
    if temp > 0:
        count += 1
        temp //= 10
print(count)
```
`58321` → `5`, `904` → `3`

## Q24. Sum of Digits
```python
n = int(input())
temp = n
total = 0
for _ in range(n):
    if temp > 0:
        total += temp % 10
        temp //= 10
print(total)
```
`58321` → `19`, `907` → `16`

## Q25. Product of Digits
```python
n = int(input())
temp = n
product = 1
for _ in range(n):
    if temp > 0:
        product *= temp % 10
        temp //= 10
print(product)
```
`234` → `24`, `105` → `0`

## Q26. Count Even Digits
```python
n = int(input())
temp = n
count = 0
for _ in range(n):
    if temp > 0:
        d = temp % 10
        if d % 2 == 0:
            count += 1
        temp //= 10
print(count)
```
`58321` → `2`, `24680` → `5`

## Q27. Sum of Even Digits
```python
n = int(input())
temp = n
total = 0
for _ in range(n):
    if temp > 0:
        d = temp % 10
        if d % 2 == 0:
            total += d
        temp //= 10
print(total)
```
`58321` → `10`, `24681` → `20`

## Q28. Largest Digit Without `max()`
```python
n = int(input())
temp = n
largest = 0
for _ in range(n):
    if temp > 0:
        d = temp % 10
        if d > largest:
            largest = d
        temp //= 10
print(largest)
```
`58321` → `8`, `40796` → `9`

## Q29. Smallest Digit Without `min()`
```python
n = int(input())
temp = n
smallest = 9
for _ in range(n):
    if temp > 0:
        d = temp % 10
        if d < smallest:
            smallest = d
        temp //= 10
print(smallest)
```
`58321` → `1`, `40796` → `0`

## Q30. Reverse a Number
```python
n = int(input())
temp = n
rev = 0
for _ in range(n):
    if temp > 0:
        rev = rev * 10 + temp % 10
        temp //= 10
print(rev)
```
`58321` → `12385`, `12040` → `4021` (leading zero disappears because the result is an integer)

## Q31. Palindrome Number
```python
n = int(input())
temp = n
rev = 0
for _ in range(n):
    if temp > 0:
        rev = rev * 10 + temp % 10
        temp //= 10
if rev == n:
    print("Palindrome")
else:
    print("Not Palindrome")
```
`1221` → `Palindrome`, `1234` → `Not Palindrome`

## Q32. Count a Specific Digit
```python
n, target = map(int, input().split(","))
temp = n
count = 0
for _ in range(n):
    if temp > 0:
        if temp % 10 == target:
            count += 1
        temp //= 10
print(count)
```
Input `1223342, 2` → `3`; `505550, 5` → `4`

## Q33. First Digit Using Repeated Division
```python
n = int(input())
temp = n
first = 0
for _ in range(n):
    if temp > 0:
        first = temp % 10   # keeps getting overwritten
        temp //= 10
print(first)
```
The *last* digit we extract is the leftmost one. `58321` → `5`, `9047` → `9`

## Q34. Difference Between Largest and Smallest Digit
```python
n = int(input())
temp = n
largest = 0
smallest = 9
for _ in range(n):
    if temp > 0:
        d = temp % 10
        if d > largest:
            largest = d
        if d < smallest:
            smallest = d
        temp //= 10
print(largest - smallest)
```
`58321` → `7`, `40796` → `9`

## Q35. Digit Position Value
```python
n = int(input())
temp = n
pos = 1
for _ in range(n):
    if temp > 0:
        print(temp % 10, pos)
        pos += 1
        temp //= 10
```
**Output (58321)**
```text
1 1
2 2
3 3
8 4
5 5
```

## Q36. Armstrong Number — 3 Digit
```python
n = int(input())
temp = n
total = 0
for _ in range(3):
    d = temp % 10
    total += d ** 3
    temp //= 10
if total == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
```
`153` → `Armstrong Number`, `123` → `Not Armstrong Number`

---

# Level 5 — String & Character Logic

## Q37. Print Characters with Index
```python
s = input()
for i in range(len(s)):
    print(i, s[i])
```
**Output (Python)**
```text
0 P
1 y
2 t
3 h
4 o
5 n
```

## Q38. Count Characters Without `len()`
```python
s = input()
count = 0
for ch in s:
    count += 1
print(count)
```
`Python` → `6`, `Hello World` → `11` (the space counts too)

## Q39. Count Vowels and Consonants
```python
s = input()
vowels = 0
consonants = 0
for ch in s:
    if ch != " ":
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
print("Vowels =", str(vowels) + ",", "Consonants =", consonants)
```
`Python` → `Vowels = 1, Consonants = 5`; `Hello World` → `Vowels = 3, Consonants = 7`

## Q40. Character Frequency
```python
s, target = input().split(",")
s = s.strip()
target = target.strip()
count = 0
for ch in s:
    if ch == target:
        count += 1
print(count)
```
`programming, g` → `2`, `banana, a` → `3`

## Q41. First Occurrence Position
```python
s, target = input().split(",")
s = s.strip()
target = target.strip()
pos = -1                       # -1 means "not found yet"
for i in range(len(s)):
    if s[i] == target and pos == -1:   # only remember the FIRST match
        pos = i
if pos == -1:
    print("Not Found")
else:
    print(pos)
```
`programming, g` → `3`, `banana, n` → `2`, `Python, z` → `Not Found`

## Q42. Count Uppercase and Lowercase
```python
s = input()
upper = 0
lower = 0
for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
print("Uppercase =", str(upper) + ",", "Lowercase =", lower)
```
`PyThOn` → `Uppercase = 3, Lowercase = 3`; `HelloWORLD` → `Uppercase = 6, Lowercase = 4`

## Q43. Character Code Analyzer
```python
s = input()
for ch in s:
    print(ch, ord(ch))
```
**Output (ABC)**
```text
A 65
B 66
C 67
```

## Q44. String Without Vowels
```python
s = input()
result = ""
for ch in s:
    if ch.lower() not in "aeiou":
        result += ch
print(result)
```
`education` → `dctn`, `Python` → `Pythn`

---

# Level 6 — Midpoint, Half & String Logic

## Q45. Find the Middle Character
```python
s = input()
mid = len(s) // 2
for i in range(len(s)):
    if i == mid:
        print(s[i])
```
`Python` → `h`, `abcde` → `c`

## Q46. First Half and Second Half
```python
s = input()
half = len(s) // 2
first = ""
second = ""
for i in range(len(s)):
    if i < half:
        first += s[i]
    else:
        second += s[i]
print("First Half:", first)
print("Second Half:", second)
```
`PythonCode` → `Pytho` / `nCode`; `ABCDEF` → `ABC` / `DEF`

## Q47. Split a String by Length — Odd vs Even
```python
s = input()
n = len(s)
half = n // 2
first = ""
middle = ""
second = ""
for i in range(n):
    if i < half:
        first += s[i]
    elif n % 2 == 1 and i == half:
        middle = s[i]
    else:
        second += s[i]
print("First Half:", first)
if n % 2 == 1:
    print("Middle:", middle)
print("Second Half:", second)
```
- `PROGRAM` → First `PRO`, Middle `G`, Second `RAM`
- `PYTHON` → First `PYT`, Second `HON`
- `HELLO` → First `HE`, Middle `L`, Second `LO`

## Q48. Compare Two Halves
```python
s = input()
half = len(s) // 2
same = True
for i in range(half):
    if s[i] != s[i + half]:
        same = False
if same:
    print("Equal Halves")
else:
    print("Different Halves")
```
`ABCABC` → `Equal Halves`, `ABCABD` → `Different Halves`, `XYZXYZ` → `Equal Halves`

## Q49. Mirror the String
```python
s = input()
n = len(s)
symmetric = True
for i in range(n):
    if s[i] != s[n - 1 - i]:
        symmetric = False
if symmetric:
    print("Symmetric")
else:
    print("Not Symmetric")
```
`ABCCBA` → `Symmetric`, `ABCD` → `Not Symmetric`, `MADAM` → `Symmetric`

## Q50. Alternate Character Extraction
```python
s = input()
result = ""
for i in range(0, len(s), 2):
    result += s[i]
print(result)
```
`ABCDEFGH` → `ACEG`, `Python` → `Pto`

## Q51. Count Characters at Even and Odd Indexes
```python
s = input()
even = 0
odd = 0
for i in range(len(s)):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even Index =", str(even) + ",", "Odd Index =", odd)
```
`Python` → `Even Index = 3, Odd Index = 3`; `ABCDE` → `Even Index = 3, Odd Index = 2`

## Q52. Swap Adjacent Characters
```python
s = input()
result = ""
for i in range(0, len(s), 2):
    result += s[i + 1] + s[i]
print(result)
```
`ABCD` → `BADC`, `ABCDEFGH` → `BADCFEHG`

---

# Level 7 — Tricky Single-Loop Problems

## Q53. Second Largest Digit
```python
n = int(input())
temp = n
first = -1
second = -1
for _ in range(n):
    if temp > 0:
        d = temp % 10
        if d > first:
            second = first     # old largest becomes second
            first = d
        elif d != first and d > second:
            second = d
        temp //= 10
print(second)
```
`58321` → `5`, `987654` → `8`, `99852` → `8` (the `d != first` check stops the repeated 9 from counting twice)

## Q54. Longest Consecutive Equal Character Run
```python
s = input()
current = 0
best = 0
for i in range(len(s)):
    if i > 0 and s[i] == s[i - 1]:
        current += 1
    else:
        current = 1
    if current > best:
        best = current
print(best)
```
`aaabbccccd` → `4`, `programming` → `2`, `abcde` → `1`

## Q55. Character Frequency Percentage
```python
s, target = input().split(",")
s = s.strip()
target = target.strip()
count = 0
for ch in s:
    if ch == target:
        count += 1
percent = round(count / len(s) * 100, 2)
print("Count =", str(count) + ",", "Frequency = " + str(percent) + "%")
```
`banana, a` → `Count = 3, Frequency = 50.0%`; `programming, g` → `Count = 2, Frequency = 18.18%`

## Q56. Running Digit Sum Until the End
```python
n = int(input())
temp = n
total = 0
for _ in range(n):
    if temp > 0:
        total += temp % 10
        print(total)
        temp //= 10
```
**Output (58321)**
```text
1
3
6
14
19
```

## Q57. Number with Most Even Digits
```python
n = int(input())
temp = n
even = 0
odd = 0
for _ in range(n):
    if temp > 0:
        if (temp % 10) % 2 == 0:
            even += 1
        else:
            odd += 1
        temp //= 10
if even > odd:
    print("More Even Digits")
elif odd > even:
    print("More Odd Digits")
else:
    print("Equal")
```
`24681` → `More Even Digits`, `13579` → `More Odd Digits`, `1234` → `Equal`

## Q58. Alternating Digit Sum
```python
n = int(input())
temp = n
sign = 1          # +1 for add, -1 for subtract
total = 0
for _ in range(n):
    if temp > 0:
        total += sign * (temp % 10)
        sign = -sign      # flip the sign every iteration
        temp //= 10
print(total)
```
`12345` → `3`, `58321` → `-1`, `2468` → `4`

## Q59. Output Prediction — Accumulator Trap
```python
total = 0
for i in range(1, 6):
    total = total + i * 2
    print(total)
```
**Answer**
```text
2
6
12
20
30
```
Trace: 0+2=2, 2+4=6, 6+6=12, 12+8=20, 20+10=30.

## Q60. Output Prediction — Condition Inside Loop
```python
count = 0
for i in range(1, 11):
    if i % 2 == 0:
        count = count + 1
print(count)
```
**Answer:** `5`

**Why:** The loop checks `i` from 1 to 10. `count` goes up only when `i` is even, i.e. at `i = 2, 4, 6, 8, 10`, which is 5 times. The `print` is outside the loop, so it runs once at the end.

## Q61. Debug the Accumulator
```python
sum = 0
for i in range(1, 6):
    sum = i
print(sum)
```
1. **Mistake:** `sum = i` *replaces* the accumulator with the current number on every iteration, so only the last value (5) survives. It should be *added* to what is already stored.
2. **Corrected program:**
```python
total = 0
for i in range(1, 6):
    total = total + i
print(total)
```
(The variable is also renamed from `sum` to `total` so it doesn't shadow Python's built-in `sum()`.)
3. **Accumulator each iteration:** keep its old value and add the new number to it: 0→1→3→6→10→15.

**Output**
```text
15
```

---

# Level 8 — Real-Life Single-Loop Problems

## Q62. Daily Expense Analyzer
```python
n = int(input())
total = 0
highest = 0
lowest = 0
for i in range(n):
    x = int(input())
    total += x
    if i == 0:
        highest = x
        lowest = x
    else:
        if x > highest:
            highest = x
        if x < lowest:
            lowest = x
print("Total:", total)
print("Highest:", highest)
print("Lowest:", lowest)
```
Input `5` then `250 180 400 120 300` (one per line) → Total `1250`, Highest `400`, Lowest `120`

## Q63. Student Marks Analyzer
```python
n = int(input())
total = 0
highest = 0
lowest = 0
for i in range(n):
    m = int(input())
    total += m
    if i == 0:
        highest = m
        lowest = m
    else:
        if m > highest:
            highest = m
        if m < lowest:
            lowest = m
print("Total:", total)
print("Average:", total / n)
print("Highest:", highest)
print("Lowest:", lowest)
```
Marks `78 65 92 81 74` → Total `390`, Average `78.0`, Highest `92`, Lowest `65`

## Q64. Attendance Analyzer
```python
n = int(input())
present = 0
absent = 0
for i in range(n):
    status = input()
    if status == "P":
        present += 1
    else:
        absent += 1
print("Present:", present)
print("Absent:", absent)
print("Attendance: " + str(round(present / n * 100, 2)) + "%")
```
`P P A P A P` → Present `4`, Absent `2`, Attendance `66.67%`

## Q65. Electricity Usage Analyzer
```python
n = int(input())
total = 0
above = 0
for i in range(n):
    units = int(input())
    total += units
    if units > 10:
        above += 1
print("Total Units:", total)
print("Days Above 10:", above)
```
`8 12 15 7 13` → Total Units `55`, Days Above 10: `3`

## Q66. Shopping Bill Analyzer
```python
n = int(input())
total = 0
expensive = 0
for i in range(n):
    price = int(input())
    total += price
    if price > 1000:
        expensive += 1
print("Total Bill:", total)
print("Products Above 1000:", expensive)
```
`450 1200 800 2500 600` → Total Bill `5550`, Products Above 1000: `2`

## Q67. Login Attempt Analyzer
```python
n = int(input())
success = 0
failed = 0
for i in range(n):
    attempt = input()
    if attempt == "success":
        success += 1
    else:
        failed += 1
print("Successful:", success)
print("Failed:", failed)
print("Success Rate: " + str(round(success / n * 100, 2)) + "%")
```
`success failed success failed success` → Successful `3`, Failed `2`, Success Rate `60.0%`

---

# Level 9 — Final Challenges

## Q68. Number Profile
```python
n = int(input())
temp = n
digits = 0
total = 0
largest = 0
smallest = 9
even = 0
odd = 0
for _ in range(n):
    if temp > 0:
        d = temp % 10
        digits += 1
        total += d
        if d > largest:
            largest = d
        if d < smallest:
            smallest = d
        if d % 2 == 0:
            even += 1
        else:
            odd += 1
        temp //= 10
print("Digits:", digits)
print("Sum:", total)
print("Largest:", largest)
print("Smallest:", smallest)
print("Even Digits:", even)
print("Odd Digits:", odd)
```
**Output (58321)**
```text
Digits: 5
Sum: 19
Largest: 8
Smallest: 1
Even Digits: 2
Odd Digits: 3
```

## Q69. String Balance Challenge
```python
s = input()
total = 0
vowels = 0
consonants = 0
upper = 0
lower = 0
even_idx = 0
for i in range(len(s)):
    ch = s[i]
    total += 1
    if i % 2 == 0:
        even_idx += 1
    if ch != " ":
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
        if ch.isupper():
            upper += 1
        else:
            lower += 1
print("Total Characters:", total)
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Uppercase:", upper)
print("Lowercase:", lower)
print("Even Index Characters:", even_idx)
```
**Output (Hello World)**
```text
Total Characters: 11
Vowels: 3
Consonants: 7
Uppercase: 2
Lowercase: 8
Even Index Characters: 6
```

---

# Quick Notes

- **Q11:** the printed expected value `80` for input `15` looks like a typo in the assignment; the correct answer is `75`.
- **Q45:** the example `Python` has an even length, but `len(s) // 2` still gives the expected `h`.
- For inputs given on one line in the question (e.g. expenses `250 180 400 120 300`), the programs read them one per `input()` call, as the questions say "enter … one by one". Press Enter after each value.