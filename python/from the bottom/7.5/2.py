Дано натуральное число n, (n≥10). Напишите программу, которая определяет его максимальную и минимальную цифры.

num = int(input())
last_digit = num % 10
min = 9
max = 0
while num != 0:
    last_digit = num % 10
    if last_digit > max:
        max = last_digit
    if last_digit < min:
        min = last_digit
    num = num // 10
print("Максимальная цифра равна", max)
print("Минимальная цифра равна", min)
