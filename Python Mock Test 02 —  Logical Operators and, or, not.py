#Python Mock Test 02 —  Logical Operators and, or, not
#Total Questions: 10
#Level: Beginner → Intermediate
#Topics: if, else, elif, comparison operators, logical operators (and, or, not), nested if


#🟠 Part C — Logical Operators and, or, not (21–30)
#21. Number Range with and — Take a number. Print "Valid" if it is greater than 10 and less than 100.
num = int(input("Enter a number: "))
if 10 < num and num < 100:
    print("Valid")
else:
    print("Invaild")

#22. Even and Positive — Take a number. Print "Valid number" if it is both: Positive Even
even_num = int(input("Enter your Number: "))
if even_num > 0:
    if even_num % 2 == 0:
        print("Valid Number")
else:
    print("Invalid Number")

#23. Voting Condition — A person can vote if:Age is 18 or above AND they have a valid voter ID Take age and voter ID status (yes/no) as input.
age = int(input("Enter your age: "))
id = input("Have you Voter Id (Yes/No): ").strip().lower()
if age >= 18 and id == "yes":
    print("Yes, You can vote")
else:
    print("No, You can not vote")

#24. Login System — Login is successful only if: Username is correct AND Password is correct AND Account is active Create suitable variables and test the conditions.
correct_username = "Jhon"
correct_password = "1234"
active_account = True
username = input("Enter your username: ")
password = int(input("Enter your password: "))
if username == correct_username and password == correct_password and active_account:
    print("Login is Successful")
else:
    print("Failed to login")

#25. Weekend Check — Take a day name. Print "Weekend" if the day is Saturday or Sunday. Otherwise print "Weekday".
day_name = input("Enter your day name: ").strip().lower()
if day_name == "saturday" or day_name == "sunday":
    print("Weekend")
else:
    print("Weekday")
#26. Scholarship Eligibility — A student gets a scholarship if: Marks ≥ 80 AND Attendance ≥ 75%
marks = int(input("Enter Your marks: "))
att = int(input("Enter your attendance(%): "))
if marks >= 80 and att >= 75:
    print("Scholaeship Eligibility")
else:
    print("Not Eligibile")
#27. Free Delivery — Free delivery is available if: Order amount ≥ 1000 OR Customer is a premium member.
order_amount= int(input("Enter your order amount: "))
customer = input("Are you premium member(yes/No): ").strip().lower()
if order_amount >= 1000 or customer == "yes":
    print("Free Delivery")
else:
    print("Take delivery Charge")
#28. Number Outside Range — Take a number. Print "Outside" if the number is: Less than 10 OR Greater than 100.
num = int(input("Enter a number: "))
if num < 10 or num > 100:
    print("outside")
else:
    print("Inside")

#29. Not Operator — Create: is_raining = False, Use not to print "Go outside" when it is not raining.
is_raining = False
if not is_raining:
    print("Go outside")
else:
    print("Raining") 

#30. Password Validation — Ask for a password. Print "Strong password" if: Length is at least 8 AND password is not "12345678". Otherwise print "Weak password".
password = input("Enter your password: ")
if len(password) >= 8 and password != "12345678":
    print("Strong password")
else:
    print("Weak Password")