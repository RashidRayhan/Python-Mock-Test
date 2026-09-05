#Python Mock Test 03 —  Combined Conditions
#Total Questions: 10
#Level: Beginner → Intermediate
#Topics: if, else, elif, comparison operators, logical operators (and, or, not), nested if

#🔴 Part D — Combined Conditions (31–40)

#31. Largest of Three Numbers — Take three numbers and print the largest number.Use logical conditions.

"""num1 = int(input("Enter your 1st number: "))
num2 = int(input("Enter your 2nd number: "))
num3 = int(input("Enter your 3rd Number: "))
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
print("The lergest Number is: ", largest)"""


#32. Smallest of Three Numbers —Take three numbers and print the smallest number.

"""num1 = int(input("Enter your 1st number: "))
num2 = int(input("Enter your 2nd number: "))
num3 = int(input("Enter your 3rd Number: "))
if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3
print("The smallest Number is: ", smallest)"""


#33. Leap Year — Take a year. A year is a leap year if: divisible by 400 OR divisible by 4 AND not divisible by 100 Print "Leap Year" or "Not Leap Year".


#34. Triangle Validation — Take three sides. A triangle is valid if: a + b > c AND a + c > b AND b + c > a Print "Valid Triangle" or "Invalid Triangle".

#35. Triangle Type — Take three sides. Print: All equal → "Equilateral", Two equal → "Isosceles", All different → "Scalene", First make sure the triangle is valid.

#36. Login + Role —Create a login system. Conditions: Correct username/password Then check role: "admin" → "Admin Dashboard" "user" → "User Dashboard" Anything else → "Unknown role

#37. Temperature Warning — Take temperature. Below 0 → "Freezing" 0–15 → "Cold" 16–30 → "Normal" 31–40 → "Hot" Above 40 → "Extreme Heat
#Additionally, if temperature is above 40, print "Warning!".

#38. Bank Loan Eligibility —  A person is eligible if: Age is 21–60 Salary ≥ 30,000 Credit score ≥ 650 Otherwise print "Not Eligible".

#39. Online Shopping Discount — Take: Purchase amount Membership status Rules: Premium + amount ≥ 5000 → 20% discount Premium + amount < 5000 → 10%, Normal + amount ≥ 5000 → 5%,Otherwise → No discount


#40. Employee Bonus — 2 marks, Take salary and years of experience. Rules: Experience ≥ 10 → 20% bonus, Experience 5–9 → 10% bonus, Experience 2–4 → 5% bonus, Below 2 → No bonus
