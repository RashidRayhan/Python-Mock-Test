#Python Mock Test 04 —   Nested if
#Total Questions: 10
#Level: Beginner → Intermediate
#Topics: if, else, elif, comparison operators, logical operators (and, or, not), nested if

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