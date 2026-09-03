#Python Mock Test 03 —  Combined Conditions
#Total Questions: 10
#Level: Beginner → Intermediate
#Topics: if, else, elif, comparison operators, logical operators (and, or, not), nested if

#🔴 Part D — Combined Conditions (31–40)

#31. Largest of Three Numbers — Take three numbers and print the largest number.Use logical conditions.

#32. Smallest of Three Numbers —Take three numbers and print the smallest number.

#33. Leap Year — Take a year. A year is a leap year if: divisible by 400 OR divisible by 4 AND not divisible by 100 Print "Leap Year" or "Not Leap Year".

"""34. Triangle Validation — Take three sides. A triangle is valid if:
a + b > c
AND
a + c > b
AND
b + c > a
Print "Valid Triangle" or "Invalid Triangle".

35. Triangle Type —
Take three sides.
Print:
All equal → "Equilateral"
Two equal → "Isosceles"
All different → "Scalene"
First make sure the triangle is valid.

36. Login + Role —
Create a login system.
Conditions:
Correct username/password
Then check role:
"admin" → "Admin Dashboard"
"user" → "User Dashboard"
Anything else → "Unknown role

7. Temperature Warning —
Take temperature.
Below 0 → "Freezing"
0–15 → "Cold"
16–30 → "Normal"
31–40 → "Hot"
Above 40 → "Extreme Heat
#Additionally, if temperature is above 40, print "Warning!".

38. Bank Loan Eligibility — 
A person is eligible if:
Age is 21–60
Salary ≥ 30,000
Credit score ≥ 650
Otherwise print "Not Eligible".

39. Online Shopping Discount —
Take:
Purchase amount
Membership status
Rules:
Premium + amount ≥ 5000 → 20% discount
Premium + amount < 5000 → 10%
Normal + amount ≥ 5000 → 5%
Otherwise → No discount


40. Employee Bonus — 2 marks
Take salary and years of experience.
Rules:
Experience ≥ 10 → 20% bonus
Experience 5–9 → 10% bonus
Experience 2–4 → 5% bonus
Below 2 → No bonus


#🔥 Part E — Nested if (41–50)
41. Nested Login —
Create:
username = "admin"
password = "python123"
First check username.
If username is correct, check password.
Output:
Username correct
Login successful
If username is wrong:
Invalid username
If password is wrong:
Wrong password"""


"""42. ATM System — 2 marks
Create:
correct_pin = 1234
balance = 50000
Ask for PIN.
If PIN is correct → ask withdrawal amount.
Check whether balance is sufficient.
If sufficient → withdraw.
Otherwise → "Insufficient balance"."""


"""43. Driving License — 2 marks
Ask for:
Age
Written test result
Conditions:
If age ≥ 18:
If test result is "pass" → "License approved"
Otherwise → "Pass the test first"
If age < 18 → "Too young"""


"""44. Student Result System — 2 marks
Ask for marks in:
Python
Math
English
First check whether all subjects are passed.
If all are ≥ 40:
Average ≥ 80 → "A"
Average ≥ 60 → "B"
Otherwise → "C"
If any subject is below 40 → "Fail"."""

"""45. Restaurant Ordering System — 2 marks
Ask:
Are you vegetarian? yes/no
If yes:
Ask whether they want "rice" or "vegetables".
If no:
Ask whether they want "chicken" or "fish".
Print the selected meal."""

"""46. Job Eligibility — 2 marks
Ask:
Age
Experience
Python skill (yes/no)
Rules:
If age ≥ 18:
If Python skill is yes:
Experience ≥ 2 → "Eligible for developer job"
Otherwise → "Junior developer"
Otherwise → "Learn Python first"
Under 18 → "Not eligible"""

"""47. ATM with Account Status — 2 marks
Create:
pin = 1234
balance = 50000
account_active = True
Ask for PIN.
Nested conditions:
Check PIN.
Check account status.
Ask withdrawal amount.
Check sufficient balance.
Complete transaction."""


"""48. Exam Admission —
A student can sit for an exam if:
Registration is completed
AND fees are paid.
If both are true:
Check attendance.
If attendance ≥ 75% → "Allowed"
Otherwise → "Attendance too low"
If registration or fees are incomplete → "Not allowed"."""

"""49. Shopping Checkout — 2 marks
Ask:
Product price
Membership (yes/no)
Coupon (yes/no)
Rules:
If membership is yes:
If coupon is yes → 20% discount
Otherwise → 10%
If membership is no:
If coupon is yes → 5%
Otherwise → No discount
Finally print the final price."""

"""50. 🔥 Advanced Nested Challenge — 2 marks
Create a University Admission System.
Ask for:
SSC marks
HSC marks
English score
Age
Rules:
Step 1: Check SSC:
If SSC ≥ 60 → continue
Otherwise → "SSC result too low"
Step 2: Check HSC:
If HSC ≥ 60 → continue
Otherwise → "HSC result too low"
Step 3: Check English:
If English ≥ 6.0 → continue
Otherwise → "English score too low"
Step 4: Check age:
18–30 → "Admission Eligible"
Otherwise → "Age requirement not satisfied"
Use nested if statements rather than putting everything into one condition."""