"""Python Mock Test 01 — If, Else, Elif, Logical & Nested Conditions

Total Questions: 50
Level: Beginner → Intermediate
Topics: if, else, elif, comparison operators, logical operators (and, or, not), nested if"""

#1. Take a number from the user. Print "Positive" if the number is greater than 0.
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

#16. Simple Calculator — Take two numbers and an operator (+, -, *, /). Use if/elif/else to calculate the result.
num1 = int(input("Enter First number: "))
op = input("Enter your operator (+, -, x, /): ")
num2 = int(input("Enter You last Number: "))
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Invaild Division Operator")
else:
    print("Invaild Operator")

print("Result is ", result)


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
    print("Fail")