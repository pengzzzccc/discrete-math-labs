import random

# comment

''' 
string comment
different line
'''

x = 5
print(x)

print(type("Hello World"))
print(type('Hello World'))
print(type('H'))
print(type(123))
print(type(3.1415926))


print(10 // 3)
print(10 % 5)

#omission something

random_int = random.randint(0,9)

print(f"random int number: {random_int}")

#Q1.
print("---------Q1.----------")
base = 6
height = 4

print((base * height) / 2)

#Q2.
print("---------Q2.----------")
Q2x = 7

if(Q2x % 2 == 0):
    print(f"Even: {Q2x}")
else:
    print(f"Odd: {Q2x}")

Q2x = 12

if(Q2x % 2 == 0):
    print(f"Even: {Q2x}")
else:
    print(f"Odd: {Q2x}")

#Q3.
print("---------Q3.----------")
for i in range(20):
    if(i == 0):
        continue
    elif(i % 3 == 1):
        print(f"output: {i}")

#Q4.
print("---------Q4.----------")
die_1 = random.randint(1,6)
die_2 = random.randint(1,6)

print(f"die 1: {die_1}")
print(f"die 2: {die_2}")
print(f"die sum: {die_1 + die_2}")

#Q5.
print("---------Q5.----------")
def factorial(n):
    ret = 1
    for i in range(n):
        ret = ret * (i + 1)
        print(f"n {n}  i {i}")
    return ret

print(f"factorial for 4 is: {factorial(4)}")

#Q6.
print("---------Q6.----------")
def isPrimes(n):
    for i in range(n):
        if(i == 0):
            continue
        elif(n % i != 0):
            return False
    return True

all_number_Primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

for n in all_number_Primes:
    if(isPrimes(n)):
        print(f"is primes: {isPrimes(n) : n}")
    else:
        print(f"is not primes {n}")
