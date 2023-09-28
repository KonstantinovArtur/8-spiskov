
numbers = [1, 2, 3, 4, 5, 6]
summa = sum(numbers)
print (summa)

bolshee = [23, 46, 97, 35, 67, 77]
max = max(bolshee)
print (max)

dubli = [8, 5, 7, 8, 2, 2, 4]
dubl = (set(dubli))
print(dubl)

spisok1= [1, 4, 5, 7, 9]
spisok2 = [10, 24, 66, 78, 99]
spisok3 = spisok1 + spisok2
print(spisok3)

print('введи кортеж')
kortezh = input()
kortezh1 = []
for a in kortezh.split(" "):
    kortezh1.append(a)
print(kortezh1)
b = input('введи элемент:')
if b in kortezh1:
    c = kortezh1.index(b)
    print(c)
else: 
    print('нет такого числа')

point = (1, 2, 3, 4, 5)
point2 = (11, 22, 33, 44, 55)
point3 = point + point2
print(point3)

abc = (1, 2, 3, 4, 5)
abc = list(abc)
cba = abc.index(3)
abc.remove(3)
back_to_tuple = tuple(abc)
print(abc)

chisla = (1, 2, 3, 2, 4, 7, 8, 2, 5)
print(chisla.count(2))
