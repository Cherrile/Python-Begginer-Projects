import random
passlen = int(input("Enter the length of password: "))
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?<.>:;'"
p = "" .join(random.sample(s, passlen))
print(p)


# variable sample returns a list with a random selection of a specified number of items from a sequence
