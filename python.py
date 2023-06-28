print("Hello World")

age = 20
print(age)

price = 19.95
print(price)

first_name = "Jimwell"
is_online = True
print(first_name, is_online)

name = input("What is your name? ")
print("Hello " + name)

birth_year = input("Enter your birth year: ")
age = 2023 - int(birth_year)
print(age)

int()
str()
float()
bool()

full_name = 'Jimwell Ibay'
print(full_name.upper())
print(full_name.lower())
print(full_name.find('y'))
print(full_name.find('Ibay'))
print(full_name.replace('Ibay', 'Bustos'))

print('Ibay' in full_name)

print(10 + 10)
print(10 - 10)
print(10 * 10)
print(10 / 10)
print(10 // 10)
print(10 % 10)
print(10 ** 100)

x = 10
x = x + 3
x += 3
x -= 3
x *= 3
x /= 3
x //= 3
x %= 3
x **= 3
x = 10 + 3 * 2
x = (10 + 3) * 2
print(x)

print(2 > 3)
print(2 < 3)
print(2 == 3)
print(2 >= 3)
print(2 <= 3)
print(2 != 3)

price = 25
print(price > 30 and price < 50)
print(price > 30 or price < 50)
print(not price > 30)


temperature = 5

if temperature > 30:
    print("Hot")
elif temperature > 20: # (20, 30]
    print("Normal")
elif temperature > 10: # (10, 20]
    print("Cold")
else:
    print("So Cold")

print("Done")  

i = 1
while i <= 5_000:
    print(i)
    i = i + 1

i = 1
while i <= 10:
    print(i * '*')
    i = i + 1

names = ['Jimwell', 'Jim', 'Jimz', 'Mr. Jim']
print(name)
print(names[0])
print(names[-1])
print(names[-2])
print(names[-3])

names[0] = 'Jimwell Ibay'
print(names)
print(names[0:2])

numbers = [1,2,4,5,6,7,8,9]
numbers.append(10)
print(numbers)

numbers.insert(3, 'Insert')
print(numbers)

numbers.remove('Insert')
print(numbers)

print('Insert' in numbers)

print(len(numbers))

numbers.clear()
print(numbers)

numbers = [1,2,3,4,5]

for number in numbers:
    print(number)

i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1

numbers = range(5)
for number in numbers:
    print(number)

numbers = range(5, 9)
for number in numbers:
    print(number)

numbers = range(5, 20, 2)
for number in numbers:
    print(number)

for number in range(5):
    print(number)

numbers = (1, 2, 3, 4, 5, 3)
# numbers[0] = 3 # ERROR

print(numbers.count(3))

