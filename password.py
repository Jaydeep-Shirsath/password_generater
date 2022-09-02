import random
from symtable import Symbol

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!~@#$%^&*/.,<>\+-_"

Use_for = upper_case + lower_case + numbers + symbols

length = int(input("Enter length for password: "))

password = "".join(random.sample(Use_for, length))

print("Your password is ",password)