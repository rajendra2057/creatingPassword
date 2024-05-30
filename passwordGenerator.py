import random
letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!', '@', '#', '$', '%', '^', '&', '*',  '_', '+','=','?']


print("!!!Welcome to password Generator!!!")
n_letters=int(input("How many alpahbets do you want in your password: "))
n_symbols=int(input("How many special character do you want in your password: "))
n_numbers= int(input("How many numbers do you want in your password: "))
password=""
for i in range(n_letters):
    x=random.choice(letters)
    password=password+x


for i in range(n_symbols):
    x=random.choice(symbols)
    password=password+x
    
for i in range(n_numbers):
    x=random.choice(numbers)
    password=password+x
password_list=list(password)
# print(password_list)
random.shuffle(password_list)
# print(password_list)
password_string=""
for items in password_list:
    password_string+=items
print(f"your password is: {password_string}")