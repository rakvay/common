#Напишите программу, которая определяет, оканчивается ли год с данным номером на два нуля. Если год оканчивается, то выведите «YES», иначе выведите «NO».

#Формат входных данных
#На вход программе подаётся натуральное число.

num = int(input())
a = num // 1000
b = (num // 100) % 10
c = (num % 100) // 10
d = num % 10

if c == 0 and d == 0:
    print("YES")
else:
    print("NO")
