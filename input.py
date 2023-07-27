name = input('What is your name? ')
print('Hello ' + name)

birth_year = input('Birth year: ')
print(type(birth_year))
age = 2023 - int(birth_year)
print(type(age))
print('Age: ' + str(age))

first = input("First: ")
second = input("Second: ")
sum = float(first) + float(second)
print("Sum: " + str(sum))

str()
int()
float()
bool()

name = input('What is your name? ')
favourite_color = input('What is your favourite color? ')
print(name + ' likes ' + favourite_color)

username = input('Username: ')
if len(username) < 3:
    print('Username must be at least 3 character')
elif len(username) > 50:
    print('Username can be maximum of 50 character')
else:
    print('Username looks good!')

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print('Failed')

phone = input('Phone: ')
digits = ''
digits_maping = {
    '0': 'Zero',
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine'
}

for num in phone:
    digits += ' ' + digits_maping.get(num, '#')
print(digits)

age = int(input('Age: '))
print(age)

try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age);
except ZeroDivisionError:
    print('Age cannot be zero')
except ValueError:
    print('Invalid value')
