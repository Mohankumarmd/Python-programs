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

n = int(input())
s = str(n)
power = len(s)

sum = 0
for i in s:
    sum += int(i)**power

if sum == n:
    print("Armstrong")
else:
    print("Not Armstrong")



def square(n):
    return n*n

print(square(5))


square = lambda x: x*x
print(square(4))


def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

print(fact(5))


a = [1,2]
b = [3,4]

c = a + b

print(c)

numbers = [1,2,3]

t = tuple(numbers)

print(t)


t = (1,2,3)

l = list(t)

print(l)


class Person:
    def greet(self):
        print("Hello")

p = Person()
p.greet()


class Person:
    def __init__(self,name):
        self.name = name

p = Person("Mohan")

print(p.name)


try:
    a = 10/0
except:
    print("Error occurred")


for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()


n = 5
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

num = int(input("Enter number: "))
count = 0

while num > 0:
    num //= 10
    count += 1

print("Digits =", count)



n = 5

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()


n = 5

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()


n = 5

for i in range(1, n + 1):
    # spaces
    for j in range(n - i):
        print(" ", end="")
    # stars
    for k in range(2 * i - 1):
        print("*", end="")
    print()


a = 10
b = a + 2.5;
print(b)
print(type(b))


x = 10
y = x + 3j;
print(y)
print(type(y))

a = True
b = a + 2
print(b)
print(type(b))


class Car:
    def __init__(self):
        self.name = ""
        self.cost = 0.0
        self.mileage = 0.0

    # Methods
    def start(self):
        print("Car is starting:")

    def accelerate(self):
        print("Car is accelerating:")

    def stop(self):
        print("Car is stopping:")


# Main program
c = Car()

# Taking input
c.name = input("Enter a name of car: ")
c.cost = float(input("Enter a cost: "))
c.mileage = float(input("Enter a mileage: "))

# Printing values
print(c.name)
print(c.cost)
print(c.mileage)


num = 10.75
result = int(num)  # explicit casting

print(result)

num = 130

# simulate Java byte casting
result = (num + 128) % 256 - 128

print(result)

num = 25.99
result = int(num)  # explicit casting (similar to short in this case)

print(result)


class Employee:
    def __init__(self):
        self.eid = 0
        self.ename = None
        self.esalary = 0


# main part
e1 = Employee()

print(e1.eid)
print(e1.ename)
print(e1.esalary)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# creating one object
s1 = Student("Mohan", 20)

# accessing object data
print("Name:", s1.name)
print("Age:", s1.age)


s1 = "MOHAN"
s2 = "MAHESH"

# Comparing strings
if s1 == s2:
    result = 0
elif s1 > s2:
    result = 1
else:
    result = -1

print(result)



num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial is:", fact)


# Python version of long to int casting

l = 9876543210  # Python does not need 'L' for long

# Simulating Java int casting (32-bit overflow)
int_val = l & 0xFFFFFFFF  # keep only lower 32 bits

# Convert to signed 32-bit integer
if int_val >= 2**31:
    int_val -= 2**32

print("Long value:", l)
print("After casting to int (data loss):", int_val)

print("-----------------------------")




# Input string
text = "JAVA PYTHON AI ML"

# Splitting the string into tokens (like StringTokenizer)
tokens = text.split()

# Loop through tokens and print
for token in tokens:
    print(token)


class MathOperations:

   
    def add(self, *args):
        if len(args) == 2:
            return args[0] + args[1]  
        elif len(args) == 3:
            return args[0] + args[1] + args[2]
        else:
            return "Invalid number of arguments"

obj = MathOperations()

print(obj.add(10, 20))        
print(obj.add(10, 20, 30))    
print(obj.add(5.5, 2.5)) 


class Calculator:

    def add(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            return a + b + c   # 3 arguments
        elif a is not None and b is not None:
            return a + b       # 2 arguments
        elif a is not None:
            return a           # 1 argument
        else:
            return 0           # no arguments



obj = Calculator()


print(obj.add(10, 20))        
print(obj.add(10, 20, 30))    
print(obj.add(10))            
print(obj.add())              



num = 10.75
result = int(num)  # explicit casting

print(result)

num = 130

# simulate Java byte casting
result = (num + 128) % 256 - 128

print(result)

num = 25.99
result = int(num)  # explicit casting (similar to short in this case)

print(result)


# Define a class
class Animal:
    
    # Constructor (initializes object data)
    def __init__(self, name, species):
        self.name = name        # object variable
        self.species = species  # object variable

    # Method (function inside class)
    def display(self):
        print("Animal Name:", self.name)
        print("Species:", self.species)


# Create an object
a1 = Animal("Leo", "Lion")

# Access object data using method
a1.display()




# Encapsulation Example
class Student:

    # Constructor (initialize private variables)
    def __init__(self):
        self.__name = None   # private variable
        self.__age = None    # private variable

    # Setter methods
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    # Getter methods
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


# Main program
s1 = Student()

# Set values using setter methods
s1.set_name("Mohan")
s1.set_age(20)

# Get values using getter methods
print("Name:", s1.get_name())
print("Age:", s1.get_age())



name = "mohan kumar"


upper_name = name.upper()

# Output
print("Original:", name)
print("Uppercase:", upper_name)



class BankAccount:
    
    # Constructor (initialize balance)
    def __init__(self):
        self.__balance = 0   # private variable

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount

    # Withdraw method
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance = self.__balance - amount
        else:
            print("Invalid amount!")

    # Getter method
    def get_balance(self):
        return self.__balance


# Main program
acc = BankAccount()

acc.deposit(5000)
acc.withdraw(2000)

print("Remaining Balance:", acc.get_balance())



class Car:
    def __init__(self):
        self.name = None

    def getName(self):
        return self.name
    
    class Demo:
    @staticmethod
    def main():
        c = Car()
        print(c.getName())

    Demo.main()


str1 = input()
str2 = input()

result = (str1 == str2)
print(result)



n = int(input())
arr = []


for i in range(n):
    arr.append(int(input()))


for i in range(n // 2):
    print(arr[i], end=" ")

for i in range(1, 11):
    print(i)


print("Java")

def main():
    print("Python")

number = 10
name = "Mohan"
print(number)
print(name)


class Animal:
    def sound(self):
        print("Animal makes a sound")
        class Dog(Animal):
    def bark(self):
        print("Dog barks")
        d = Dog()
        d.sound()
        d.bark()


class Employee:

    # Private variable
    def __init__(self):
        self.__name = ""

    # Setter method
    def setName(self, n):
        self.__name = n

        def getName(self):
        return self.__name
    
e = Employee()

e.setName("Mohan")

print(e.getName())




# Star Pattern Program in Python

rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()



# Polymorphism Example in Python

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

# Parent reference, child object
a = Dog()

# Calls Dog class method
a.sound()

for i in range(1, 11);
    print(i)

for i in range(1, 7):
    print("Number:", i)
    print("Loop completed")


number = 7

if number % 2 == 0:
        print(number, "is Even")
else:
        print(number, "is Odd")



class Animal:
    def sound(self):
        print("Animal makes a sound")
        class Dog(Animal):
        def bark(self):
        print("Dog barks")
        d = Dog()
        d.sound()
        d.bark()



n = 5
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()



num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial is:", fact)


n = 5

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()



obj = Calculator()


print(obj.add(10, 20))        
print(obj.add(10, 20, 30))    
print(obj.add(10))            
print(obj.add())


num = int(input("Enter number: "))
count = 0

while num > 0:
    num //= 10
    count += 1

print("Digits =", count)