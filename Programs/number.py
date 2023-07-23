how_many = int(input('How many numbers? '))
numbers = []
i = 1

while i < how_many + 1:
    number = int(input(f'({i}) Input a number: '))
    numbers.append(number)
    i = i + 1

largest_number = max(numbers)
print(f'The largest number is: {largest_number}')

