import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', '|', '\\', ':', ';', '"', '\'', '<', '>', ',', '.', '?', '/', '`', '~']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print("Welcome to Password Generator")
n_letters = int(input("How many letters do you want?\n"))
n_symbols = int(input("How many symbols do you want?\n"))
n_numbers = int(input("How many numbers do you want?\n"))
password_list = []
for i in range(1, n_letters+1):
    char = list(random.choice(letters))
    password_list = password_list + char
for i in range(1, n_symbols+1):
    char = list(random.choice(symbols))
    password_list = password_list + char
for i in range(1, n_numbers+1):
    char = list(random.choice(numbers))
    password_list = password_list + char
random.shuffle(password_list)
password = ""
for i in password_list:
    password = password+i
print(password)