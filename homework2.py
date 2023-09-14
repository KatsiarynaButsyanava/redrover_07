"""Задание 2.1
Напишите программу, которая проверяет здоровье персонажа в игре.
Если оно равно или меньше нуля, выведите на экран False, в противном случае True.

"""
# health_lavel = int(input("please enter health points))
# if health_lavel <= 0:
#     print("False")
# else:
#     print("True")
# print(health_lavel >= 0)

"""Задание 2.2
Напишите программу, которая проверяет является ли введенное число четным. Если да, выведите на экран текст “Четное”, а иначе - “Нечетное”
"""
# number = int(input())
# if number % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# if number % 2:"""Есть остаток например у 11, то это истино"""
#      print("neЧетное")
# else:
#      print("четное")

"""Задание 2.3
Напишите программу, которая проверяет является ли год 
високосным. Таковыми считаются года, которые делятся без 
остатка на 4 (2004, 2008) и не являются столетиями (500, 600).не кратны 100
 Однако, если год делится без остатка  на 400, он также считается високосным (1200, 2000)
"""
year = int(input("please enter year"))
# if year % 4 == 0 and year / 100 > 10:
#     print("год высокосный")
# elif year % 400 == 0 and year / 100 > 10:
#     print("год высокосный")
# else:
#     print("год neвысокосный")
# более правильный вариант, из сотен берется только 400, 800
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Высокосный")
#         else:
#             print("neВысокосный")
#     else:
#         print("Высокосный")
# else:
#     print("Высокосный")
#
if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
     print("Высокосный")
else:
     print("neВысокосный")

"""Задание 2.4
Напишите программу, которая печатает введенный текст заданное количество раз, построчно. Текст и количество повторений нужно ввести с помощью input()
"""
# num_repeat = int(input())
# text = input()
# for i in range(num_repeat):
#     print(text)

# text = input("enter text")
# num = int(input("enter number of repeat"))
# i = 0
# while i < num:
#     print(text)
#     i += 1

"""Задание 2.5.
Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str), производит заданное арифметическое действие и печатает результат в формате: {num1} {operator) {num2) = {result}
"""
# num_1, num_2 = int(input("Enter the first number")), int(input("Enter the second number"))
# operator = input("Enter operator: '+', '-', '/', '*', '%'")
# result = 0
# if operator == "+":
#     result = num_1 + num_2
# elif operator == "-":
#     result = num_1 - num_2
# elif operator == "*":
#     result = num_1 * num_2
# elif operator == "/":
#     result = num_1 / num_2
# elif operator == "%":
#     result = num_1 % num_2
# print(f"{num_1} {operator} {num_2} = {result}")

