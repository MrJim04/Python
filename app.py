print('Hello World')
print('o----')
print(' ||||')
print('*' * 10)

price = 10
price = 40
rating = 4.4
name = 'Jimwell'
is_publish = False
print(price, rating, name, is_publish)

name = 'Mikie'
age = 70
is_new = True
print(name, age, is_new)

course = 'Python tutorial for "Beginners"'
print(course)

message = '''
Hi Jimwell,

You are doing great keep going

Thank you.
'''

print(message)
print(course[0], course[-2])
print(course[0:4])
print(course[:4])
print(course[1:])
print(course[1:4])

another = course[:]
print(another)

name = 'Jennifer'
print(name[1:-1])

first_name = 'Jimwell'
last_name = 'Ibay'
message = first_name + ' [' + last_name + '] is a coder'
formated_message = f'{first_name} [{last_name}] is a coder'
print(message)
print(formated_message)

print(len(course))
print(course.upper())
print(course.lower())
print(course.find('t'))
print(course.find(('Beginners')))
print(course.replace('Beginners', 'Absolute Beginners'))
print(course.replace('P','J'))
print('Python' in course)

print(10 + 40)
print(10 - 40)
print(10 * 40)
print(10 ** 40)
print(10 / 40)
print(10 // 40)
print(10 % 40)

x = 10
x = x + 3
print(x)

x = 10
x += 3
print(x)

x = 10
x -= 3
print(x)

x = 10
x *= 3
print(x)

x = 10
x **= 3
print(x)

x = 10
x /= 3
print(x)

x = 10
x //= 3
print(x)

x = 10
x %= 3
print(x)

x = 10 + 3 * 2
print(x)

x = (10 + 3) * 2
print(x)

x = 10 + 3 * 2 ** 2
print(x)

x = (10 + 3) * (2 ** 2)
print(x)

x = (2 + 3) * 10 - 3
print(x)

x = 3.8
print(round(x))

x = -2.6
print(abs(x))

import math

x = 2.9
print(math.ceil(x))

is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
elif is_cold:
    print("It's a cold day")
else:
    print("it's a lovely day")
print('Enjoy your day')

price = 1000000
has_good_credit = False
print(f'Price: ${price}')

if has_good_credit:
    print(f'Down payment: ${price * 0.10}')
else:
    print(f'Down payment: ${price * 0.20}')

has_high_income = True
has_high_credit = True

if has_high_income and has_high_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

has_high_income = True
has_high_credit = False

if has_high_income or has_high_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

has_high_income = True
has_criminal_record = True

if has_high_income and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

temperature = 10

if temperature > 30:
    print("It's a hot day")
else:
    print("It's a cold day")

if temperature < 30:
    print("It's a cold day")
else:
    print("It's a hot day")

if temperature > 30:
    print("It's a hot day")
else:
    print("It's a cold day")

i = 1
while i <= 10:
    print(i)
    i = i + 1
print('Done')

i = 1
while i <= 10:
    print('*' * i)
    i = i + 1
print('Done')

for item in 'Python':
    print(item)

for item in ['Jimz', 'Jim', 'Jimwell', 'Ibay', 'Jimwell Ibay']:
    print(item)

for item in [1, 2, 3, 4, 5, 6]:
    print(item)

for item in range(10):
    print(item)
    
for item in range(5, 10):
    print(item)

for item in range(5, 10, 2):
    print(item)
    
prices = [10, 30, 50]
total = 0
for price in prices:
    print(f'${price}')
    total += price
print(f'Total: ${total}')

for x in range(4):
    for y in range(3):
        print(f'({x},{y})')
        
numbers = [5, 2, 5, 2, 2]
f = '\n'
for number in numbers:
    for x in range(number):
        f += 'x'
    f += '\n'
print(f)

for number in numbers:
    f = ''
    for x in range(number):
        f += 'x'
    print(f)
    
numbers = [2, 2, 2, 2, 5]

print('\n')

for number in numbers:
    l = ''
    for x in range(number):
        l += 'x'
    print(l)