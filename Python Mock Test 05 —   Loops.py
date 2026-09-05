#Python Mock Test 04 —   Nested if
#Total Questions: 10
#Level: Beginner → Intermediate
#Topics: for, while, range(), nested loops, break, continue
#Total Marks: 20
#Time: 30 minutes

#1. Print Numbers — Use a for loop to print numbers from 1 to 10.
for i in range(1, 11):
    print(i)

#2. Even Numbers — Use a loop to print all even numbers from 1 to 20.
for x in range(1, 21):
    if x % 2 == 0:
        print(x)

#3. Sum of Numbers — Use a loop to calculate the sum of numbers from 1 to 100. Expected result: 5050
total = 0
for y in range(1, 101):
    total += y
print(total)

#4. Multiplication Table — Take a number from the user and print its multiplication table from 1 to 10.
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#5. Countdown — Use a while loop to print numbers from 10 down to 1, then print: Blast Off!
count = 10
while count >= 1
    count -= 1
    print(count)
else:
    print("Blast Off!")

#6. Positive Number Input — Keep asking the user to enter a number until they enter a positive number.

while True:
    user_input= int(input("Enter your number: "))
    if user_input > 0:
        print("Positive Number accepted!", user_input)
        break
    else:
        print("Nagetive number is not accepted!", user_input)

#7. Count Vowels — Take a word or sentence from the user and use a loop to count how many vowels (a, e, i, o, u) it contains.
user = input("Enter your word: ")
vowels ="aeiouAEIOU"
count = 0
for txt in user:
    if txt in vowels:
        count += 1
print("The number of vowels", count)

#8. break Challenge — Print numbers from 1 to 20, but stop the loop when the number reaches 12.
for i in range(1, 21):
    print(i)
    if i == 12:
        break

#9. continue Challenge — Print numbers from 1 to 20, but skip all numbers divisible by 3.
for z in range(1, 21):
    if z % 3 == 0:
        continue
    print(z)

#10. 🔥 Nested Loop Challenge — Use nested for loops to print this pattern:
for x in range(1, 6):
    for i in range(x):
        print("*", end="")
    print()