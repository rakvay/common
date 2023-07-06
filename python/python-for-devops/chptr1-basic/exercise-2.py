#Write a Python function that takes a string as an argument and prints whether it is upper- or lowercase.

def case_func(name):
    if name.islower():
        print(name, "is a lowercase string")
    elif name.isupper():
        print(name, "is an uppercase string")

case_func("BOB")