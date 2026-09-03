"""Python Mock Test 01 — If, Else, Elif, Logical & Nested Conditions

Total Questions: 50
Level: Beginner → Intermediate
Topics: if, else, elif, comparison operators, logical operators (and, or, not), nested if"""

"""#1. Take a number from the user. Print "Positive" if the number is greater than 0.
number = int(input("Enter a Number: "))
if number > 0:
    print("Positive")

#2. Take an integer and print whether it is "Even" or "Odd".
numbers = int(input("Enter a Number: "))
if numbers %2 ==0:
    print("Even")
else:
    print("Odd")

#3. Take a person's age. If age is 18 or above, print "Adult", otherwise print "Minor".
person_age = int(input("Enter Your Age: "))
if person_age >= 18:
    print("Adult")
else:
    print("Minor")

#4. Take a student's mark. If the mark is 40 or above, print "Pass", otherwise print "Fail".
student_marks = int(input("Enter your mark: "))
if student_marks >= 40:
    print("Pass")
else:
    print("Fail")

#5. Take two numbers and print the greater number.
a = 200
b = 100
if a > b:
    print(a)
else:
    print(b)

#6. Take a number. Print "Divisible by 5" if it can be divided by 5, otherwise print "Not divisible by 5".
divisible_number = int(input("Enter your number: "))
if divisible_number % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5") 

#7. Take temperature as input. If temperature is above 30 → "Hot" Otherwise → "Normal"
temperature = int(input("Enter temperature: "))
if temperature > 30:
    print("Hot")
else:
    print("Normal") 

#8. Take age as input. 18 or above → "Eligible to vote" Otherwise → "Not eligible"
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible")
else:
    print("Not eligible") 

#9. Create:
#username = "admin"
#password = "1234"
#Ask the user for username and password. Print "Login successful" if both are correct, otherwise "Invalid login".
username = "admin"
password ="1234"
user_login= input("Enter Username: ")
pass_login = input("Enter password: ")
if user_login == username and pass_login == password:
    print("Login successful")
else:
    print("Invalid login") 

#10. Take a number. Print "Between 10 and 50" if the number is between 10 and 50, otherwise print "Outside range".
num = int(input("Enter a number: "))
if 10 <= num <= 50:
    print("Between 10 and 50")
else:
    print("Outside range")

#11. Grade Calculator
#Take marks and print:
#80–100 → A+
#70–79 → A
#60–69 → B
#50–59 → C
#40–49 → D
#Below 40 → F

marks = int(input("Enter Your marks: "))
if marks >= 80:
    print("A+")
elif marks >= 70:
    print("A")
elif marks >= 60:
    print("B")
elif marks >= 50:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("F") 

#12.Take a number and print: Positive, Negative, Zero
input_number = int(input("Enter a Number: "))
if input_number > 0:
    print("Positive")
elif input_number == 0:
    print("Zero")
else:
    print("Negative") 

#13. Take age: 0–12 → "Child" 13–19 → "Teenager" 20–59 → "Adult" 60+ → "Senior"
input_age = int(input("Enter Your Age: "))
if input_age >= 60:
    print("Senior")
elif input_age >= 20:
    print("Adult")
elif input_age >= 13:
    print("Teenger")
else:
    print("Child") 

#14. Take a number from 1–7 and print the corresponding day.
#Example:
#1 → Monday
#2 → Tuesday
#...
#7 → Sunday
take_day_number = int(input("Enter Your day Number: "))
if take_day_number == 1:
    print("Monday")
elif take_day_number == 2:
    print("Tuesday")
elif take_day_number == 3:
    print("Wednesday")
elif take_day_number == 4:
    print("Thursday")
elif take_day_number == 5:
    print("Friday")
elif take_day_number == 6:
    print("Saturday")
elif take_day_number ==7:
    print("Sunday")
else:
    print("Please Enter 1 to 7 number")  

# 15 Take a month number: 1–3 → "First Quarter" 4–6 → "Second Quarter" 7–9 → "Third Quarter" 10–12 → "Fourth Quarter" Otherwise → "Invalid month"
monthly_number = int(input("Enter Your Monthly Number: "))
if 1 <= monthly_number <= 3:
    print("First Quarter")
elif 4 <= monthly_number <= 6:
    print("Second Quarter")
elif 7 <= monthly_number <= 9:
    print("Third Quarter")
elif 10 <= monthly_number <= 12:
    print("Fourth Quarter")
else:
    print("Invalid month") 

#17. Take electricity units: 0–100 → "Low usage", 101–300 → "Medium usage", 301–500 → "High usage" Above 500 → "Very high usage"
units = int(input("Enter your electricity units: "))
if 0 <= units <= 100:
    print("Low usage")
elif units <= 300:
    print("Medium Usage")
elif units <= 500:
    print("High usage")
else:
    print("Very High usage") 

#18. Take BMI: Below 18.5 → Underweight, 18.5–24.9 → Normal, 25–29.9 → Overweight, 30+ → Obese
bmi = float(input("Enter your BMI Number: "))
if bmi <= 18.5:
    print("Underweight")
elif bmi <= 24.9:
    print("Normal")
elif bmi <= 29.9:
    print("Overweight")
else:
    print("Obese") 
#19. Take vehicle speed: Below 40 → "Too slow" 40–80 → "Normal" 81–100 → "Fast" Above 100 → "Overspeed"
vehicle = float(input("Enter your vehicle speed: "))
if vehicle <= 40:
    print("Too Slow")
elif vehicle <= 80:
    print("Normal")
elif vehicle <= 100:
    print("fast")
else:
    print("Overspeed") 

#20. Take marks: 90+ → "Excellent" 75–89 → "Very Good" 60–74 → "Good" 40–59 → "Pass" Below 40 → "Fail"
exam_marks = int(input("Enter your marks: "))
if exam_marks >= 90:
    print("Excellent")
elif exam_marks >= 75:
    print("Very Good")
elif exam_marks >= 60:
    print("Good")
elif exam_marks >= 40:
    print("Pass")
else:
    print("Fail") """

#🟠 Part C — Logical Operators and, or, not (21–30)
#21. Number Range with and — Take a number. Print "Valid" if it is greater than 10 and less than 100.

#22. Even and Positive — Take a number. Print "Valid number" if it is both: Positive Even

#23. Voting Condition — A person can vote if:Age is 18 or above AND they have a valid voter ID Take age and voter ID status (yes/no) as input.

#24. Login System — Login is successful only if: Username is correct AND Password is correct AND Account is active Create suitable variables and test the conditions.

#25. Weekend Check — Take a day name. Print "Weekend" if the day is Saturday or Sunday. Otherwise print "Weekday".

#26. Scholarship Eligibility — A student gets a scholarship if: Marks ≥ 80 AND Attendance ≥ 75%

#27. Free Delivery — Free delivery is available if: Order amount ≥ 1000 OR Customer is a premium member.

#28. Number Outside Range — Take a number. Print "Outside" if the number is: Less than 10 OR Greater than 100.

#29. Not Operator — Create: is_raining = False, Use not to print "Go outside" when it is not raining.

#30. Password Validation — Ask for a password. Print "Strong password" if: Length is at least 8 AND password is not "12345678". Otherwise print "Weak password".

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
Print "Valid Triangle" or "Invalid Triangle"."""

"""35. Triangle Type —
Take three sides.
Print:
All equal → "Equilateral"
Two equal → "Isosceles"
All different → "Scalene"
First make sure the triangle is valid."""

"""36. Login + Role —
Create a login system.
Conditions:
Correct username/password
Then check role:
"admin" → "Admin Dashboard"
"user" → "User Dashboard"
Anything else → "Unknown role""""

"""37. Temperature Warning —
Take temperature.
Below 0 → "Freezing"
0–15 → "Cold"
16–30 → "Normal"
31–40 → "Hot"
Above 40 → "Extreme Heat""""
#Additionally, if temperature is above 40, print "Warning!".

"""38. Bank Loan Eligibility — 
A person is eligible if:
Age is 21–60
Salary ≥ 30,000
Credit score ≥ 650
Otherwise print "Not Eligible"."""

"""39. Online Shopping Discount —
Take:
Purchase amount
Membership status
Rules:
Premium + amount ≥ 5000 → 20% discount
Premium + amount < 5000 → 10%
Normal + amount ≥ 5000 → 5%
Otherwise → No discount"""


"""40. Employee Bonus — 2 marks
Take salary and years of experience.
Rules:
Experience ≥ 10 → 20% bonus
Experience 5–9 → 10% bonus
Experience 2–4 → 5% bonus
Below 2 → No bonus"""


#🔥 Part E — Nested if (41–50)
"""41. Nested Login —
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
If age < 18 → "Too young""""


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
Under 18 → "Not eligible""""

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