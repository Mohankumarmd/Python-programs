print("Hello world")


num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

largest = a

if b > largest:
    largest = b
if c > largest:
    largest = c

print("Largest number is:", largest)



string = input("Enter a string: ")
reverse = string[::-1]
print("Reversed string:", reverse)

num = 1234
reverse = 0

while num != 0:
    reverse = reverse * 10 + num % 10
    num = num // 10

print("Reversed Number:", reverse)


num = 121
original = num
reverse = 0

while num != 0:
    reverse = reverse * 10 + num % 10
    num //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


num = 5
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial:", fact)


n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c


num = int(input("Enter a number: "))
count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime number")
else:
    print("Not a prime number")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

largest = max(a, b, c)

print("Largest number is:", largest)


a = 10
b = 20
sum = a + b
print("Sum =", sum)

num = 7

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

a = 10
b = 25
c = 15

if a > b and a > c:
    print("Largest:", a)
elif b > c:
    print("Largest:", b)
else:
    print("Largest:", c)


num = int(input("Enter number: "))
print("Square:", num*num)


text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)

for i in range(1, 11):
    print(i)

num = int(input("Enter number: "))
count = len(str(num))
print("Digits:", count)


numbers = [1, 2, 3, 4, 5]

print("Sum:", sum(numbers))


n = int(input("Enter n: "))
sum = 0

for i in range(1, n+1):
    sum += i

print("Sum:", sum)


num = int(input("Enter number: "))
flag = True

for i in range(2, num):
    if num % i == 0:
        flag = False
        break

if flag:
    print("Prime")
else:
    print("Not Prime")


for i in range(1,21):
    if i % 2 == 0:
        print(i)


year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")


c = 25

f = (c * 9/5) + 32

print("Fahrenheit:", f)


num = int(input("Enter number: "))
temp = num
sum = 0

while num > 0:
    digit = num % 10
    sum += digit ** 3
    num //= 10

if sum == temp:
    print("Armstrong")
else:
    print("Not Armstrong")


num = int(input("Enter number: "))
count = 0

while num > 0:
    num //= 10
    count += 1

print("Digits =", count)


num = int(input("Enter number: "))
sum = 0

while num > 0:
    sum += num % 10
    num //= 10

print("Sum =", sum)


import math

a = int(input())
b = int(input())

lcm = (a*b)//math.gcd(a,b)

print(lcm)


num = int(input())

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


import random

print(random.randint(1,100))


a = "listen"
b = "silent"

if sorted(a) == sorted(b):
    print("Anagram")


arr = [1,2,3,4,5]
key = 3

low, high = 0, len(arr)-1

while low <= high:
    mid = (low+high)//2
    if arr[mid] == key:
        print("Found")
        break

arr = [64,25,12,22]

for i in range(len(arr)):
    min_idx = i
    for j in range(i+1,len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)


arr = [10,20,4,45]
arr.sort()
print(arr[-2])



import random

print(random.randint(1,100))