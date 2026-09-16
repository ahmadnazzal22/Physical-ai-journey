
j = "john"
namber = 35
print(f"There once was a man named {j}")
print(f"He was {namber} years old")
print(f"He really liked the name {j}")
print(f"But he didn't like being {namber}")
print(f"Hello {j}")
print(f"{j.lower()}")
print(f"{j.upper()}")
print(f"{j.upper().isupper()}")
print(f"{len(j)}")

name = "Ahmad Nazzal 12/8/2002"
print(f"{name[0]}{name[1]}{name[2]}{name[3]}{name[4]}")
print(f"{name[6:13]}")
print(f"{name[13:]}")
print(f"{name[:]}")
print(f"{name[15:-1]}")
print(name.index("N"))
print(name.replace("Nazzal", "Ryiad nazzal"))



name = input("Enter Your Name: ")
age = input("Enter Your Age: ")
print(f"Hello {name}, you are {age} years old")

nmber = input("Enter a number: ")
if int(nmber) % 2 == 0:
    print(f"{nmber} is an even number")
else:
    print(f"{nmber} is an odd number")


numbers = []

for x in range(3):
    a = int(input("Enter a number: "))
    numbers.append(a)

total = numbers[0] + numbers[1] + numbers[2]

print(f"The sum of the numbers is: {total / 3}")

if total >= 60 :
    print("You passed the test")
else:
    print("You failed the test")

for x in range(0,51):
    if x % 3 == 0 or x % 5 == 0:
        print(f"{x} is divisible by 3 or 5")

total = 0
for x in range(0, 101):
        total += x

print(f"The sum of the numbers from 0 to 100 is {total}")

a = [ 0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]
i = int(input(f"Enter a number to multiply by : "))
for x in a:
    print (f"{i} * {x} = {i*x}")

names = ["Ahmad", "Sara", "Omar"]
for x in names:
    print(f"Hello {x}")


x ={
    "Backpack": 350 , 
    "Headphones":530,
    "Smartphone":600,
    "Laptop": 820,
    "Apple": 1250
    }
most_expensive = max(x, key=x.get)

print(f"{most_expensive} costs {x[most_expensive]}")

cheapest = min(x, key=x.get)
print(f"{cheapest} costs {x[cheapest]}")

average = sum(x.values()) / len(x)
print(f"The average cost is {average}") # x.values() = كل الأسعار

max(x, key=x.get)   # الأغلى
min(x, key=x.get)   # الأرخص
sum(x.values()) / len(x)   # المتوسط



nambers = [1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 7]
x  = list(set(nambers))# set => يحدف التكرر 
print(x)


def distance(x1, y1, x2, y2):
    r = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return r

print(distance(0, 0, 4, 3))


def factorial(n):
    result = 1
    for x in range(1, n+1):
        result *= x
    return result

print(factorial(5))

def stats(numbers:[int]): # type: ignore
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total, average, maximum, minimum

print(stats([5,10,15,20,25,30]))




names = ["Ahmad", "Sara", "Omar", "Ali", "lina", "Huda"]
attendance = {}

def mark_presence(attendance, name):
    attendance[name] = True

def mark_absent(attendance, name):
    attendance[name] = False

def attendance_rate(attendance, names):
    present_count = sum(attendance.get(name, False) for name in names)
    total_count = len(names)
    return present_count / total_count * 100

mark_presence(attendance, "Ahmad")
mark_presence(attendance, "Sara")
mark_absent(attendance, "Omar")

print(attendance)
print(attendance_rate(attendance, names))


