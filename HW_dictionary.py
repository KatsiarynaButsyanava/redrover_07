'''1. Создать словарь my_dict с 3 парами ключ: значение.
2. Создать словарь new_dict с 2 парами ключ: значение(отличные от первого словаря) '''
# my_dict = {
#     'class':'fantasy',
#     'name':'Star Wars',
#     'year':1977
#     }
#
# new_dict = {
#     'author':'George Lucas',
#     'count_film':9,
#      }
# print(my_dict['name'])

'''Добавление новой пары'''
# book_2['actor'] = 'Like vv'
# print(book_2)

''' Оператор | для объединения двух или более словарей'''
# all_dict = book_1 | book_2
# print(all_dict)
# my_dict_copy = my_dict.copy()
# my_dict_copy = new_dict.update(my_dict)
# print(my_dict)

'''Объединение методом распаковки'''
# all_dict = {**my_dict, **new_dict}
# print(all_dict)

'''Измение значения любого ключа в all_dict на '0' методом pop. 
Вывести в терминал изменённый словарь'''

# print(all_dict.pop('year'))
# print(all_dict)
# print(all_dict.setdefault('year'), '0')
# print(all_dict)

'''Удалить последнюю пару ключ: значение из словаря all_dict методом popitem'''
# print(all_dict.popitem())
# print(all_dict)

'''Создать список из 3 кортежей в которых по 2 значения'''
# tuple_1 = {1, 'Anna'}
# tuple_2 = {2, 'Serge'}
# tuple_3 = {3, 'Margo'}
# print(tuple_1, tuple_2, tuple_3)
# new_list = []
# new_list.append(tuple_1)
# new_list.append(tuple_2)
# new_list.append(tuple_3)
# print(new_list)
# print(dict(new_list), type(new_list))


'''Преобразовать этот список в словарь и вывести в терминал значение второго(позиция 1) ключа'''
# all_dict_tuple = dict(new_list)
# print(all_dict_tuple, type(all_dict_tuple))
# print(list(all_dict_tuple.values())[1])


