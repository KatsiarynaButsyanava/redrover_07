"""3.1 Дан список my_list = ['a', 'b', [1, 2, 3], 'd'].
Распечатайте значения 1, 2, 3"""
# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(my_list[2][0], my_list[2][1], my_list[2][2])
# print(my_list[2][0:3])

"""3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
- получите сумму всех чисел,
- распечатайте все строки, где есть буква 'a'
"""

# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
'''создать новый список где только цифры'''
# new_lst = [x for x in list_1 if isinstance(x,int)]
'''Сумма цифр в списке'''
# print(sum(new_lst))

# Выбираем из списка элементы строк
# new_lst = [x for x in list_1 if isinstance(x,str)]
# print(new_lst)
# Создаем список где в элементе списка есть буква а
# n_lst = [x for x in new_lst if "a" in x]
'''тоже но циклом'''
 # for i in new_lst:
#     if 'a' in i:
#         n_lst.append(i)
# print(n_lst)
# print(' '.join(n_lst))

"""3.3 Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж"""
# lst_3 = ['cat', 'dog', 'horse', 'cow']
# tuple_1 = tuple(lst_3)
# print(tuple_1)

"""3.4 Напишите программу, которая определяет, какая семья больше. 
      1) Программа имеет два input() - например, family_1, family_2. 
    mam pap daughter sister bro
    mam dad granny pap sister bro other
      2) Членов семьи нужно перечислить через запятую. 
     Ожидаемый результат - программа выводит семью с бОльшим составом. 
     Если состав одинаковый, print("Equal')"""
# family_1 = map(str, input().split())
# family_2 = map(str, input().split())
# # print(family_1, type(family_1))
# family_1 = list(family_1)
# family_2 = list(family_2)
# if len(family_1) > len(family_2):
#     print(' '.join(family_1))
# elif len(family_1) < len(family_2):
#     print(' '.join(family_2))
# else:
#     print('Equal')

"""3.5. Создайте словарь film c ключами title, director, 
year, budget, main_actor, slogan. 
В значения можете передать информацию о вашем любимом фильме. 
    - распечатайте только ключи
    - распечатайте только значения
    - распечатайте пары ключ - значение"""

# film = {
#     'title':'triller',
#     'director':'Wain',
#     'year':2008,
#     'budget':250000,
#     'main_actor':'Luce Luceen',
#     'slogan': 'Never give up'
#     }
# print(film, type(film))
# print(film.keys())
# print(film.values())
# print(film['year'])
# print(film.items())
# print(len(film))

"""3.6. Найдите сумму всех значений в словаре 
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}"""
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# print(my_dictionary.values())
# new_list = list(my_dictionary.values())
# print(sum(new_list))

"""3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1] """
# list_1 = [1, 2, 3, 4, 5, 3, 2, 1]
# '''Коротко'''
# new_list = list(set(list_1))
# print(new_list, type(new_list))
'''Длинный путь'''
# new_list = set(list_1)
# print(new_list, type(new_list))
# list_2 = list(new_list)
# print(list_2, type(list_2))

"""3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, 
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
     - найдите значения, которые встречаются в обоих множествах
     - найдите значения, которые не встречаются в обоих множествах
     - проверьте являются ли эти множества подмножествами друг друга """
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
'''значения, которые встречаются в обоих множествах'''
# print(set1 & set2)
# print(set1.intersection(set2))
'''значения, которые не встречаются в обоих множествах'''
print(set1 ^ set2)

# print(set1.difference(set2))
# print(set2.difference(set1))
# print(set1 == set2)

'''проверьте являются ли эти множества подмножествами друг друга'''
# print(set1 > set2)
# print(set1 < set2)
'''Объединение без дубликатов'''
# print(set1 | set2)
# print(set1.union(set2))
# print(set1, set2)
