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