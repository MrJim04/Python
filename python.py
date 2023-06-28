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

print("Git")








