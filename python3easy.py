# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

def info(name,age,city):
    print(name, age ,'Год(а)','проживает в городе', city)

info('Оскар', 19, 'лондон')


# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

def data(x, y, z):
    return max(x,y,z)


print(data(5,12,30))


# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов


def returning(*args):
    list1 = []
    for i in args:
        list1.append(i)
        list1.sort(key=len) #сортировка по длинне
    return list1[-1] #Возвращаем последний элемент списка так-как после сортировки он самый длинный


print(returning('one', 'threeeee', 'four hundred eighty nine', 'eightysix', 'thirtysix'))
