import pandas as pn
dataBase = pn.read_csv('lab9.txt', names=['Артикул','Название','Цена','Кол-во товара','Краткое описание'])
print("База данных: ")
print(dataBase)
print("Введите артикул: ")
value = input()
print(dataBase[dataBase['Артикул'] == value])



