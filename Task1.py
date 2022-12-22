# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

# num = int(input("Введите вещественное число: "))
# a = num
# sumOfNumbers = 0
# if num
#     intermedNum = num % 10
#     sumOfNumbers + num
# print(sumOfNumbers)


num = input("Введите вещественное число: ")
num = num.replace('.', '')
num = num.replace(',', '')
sumOfNumbers = 0
for i in num:
    sumOfNumbers += int(i)
print(sumOfNumbers)
