import random
upper = "ABCDEFGHIJKLMNOPQRSTUVWXZ"
lower = "abcdefghijklmnopqrstuvwxyz"
Number = "0123456789"
symbol = "!@#$%&*{}[]()_+-"
all = lower+upper+Number+symbol
length=8
password = "".join(random.sample(all,length))
print("Your Generated Password is :",password)