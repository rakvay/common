#Write a generator that alternates between returning Even and Odd.

def my_gen():
    a = "Even"
    b = "Odd"
    while True:
        yield a
        a, b = b, a

generator = my_gen()

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))