import random

symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""
count = int(input("Длина пароля: "))

for i in range(count):
    password += random.choice(symbols)

print(password)
