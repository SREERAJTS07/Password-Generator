import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'

print('Welcome to the Password Generator!')

# Ensuring minimum length of 8 characters
while True:
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input('How many symbols would you like?\n'))
    nr_numbers = int(input('How many numbers would you like?\n'))

    total_length = nr_letters + nr_symbols + nr_numbers
    if total_length >= 8:
        break
    else:
        print("Password must be at least 8 characters long. Please add more characters.")

password_list = []

for _ in range(nr_letters):
    password_list.append(random.choice(letters))

for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
password = ''.join(password_list)

print(f'Your password is: {password}')
