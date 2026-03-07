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