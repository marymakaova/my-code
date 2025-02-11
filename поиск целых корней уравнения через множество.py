b = float(input("Введите b: "))
c = float(input("Введите с: "))
d = float(input("Введите d: "))
f = float(input("Введите f (f != 0): "))
def poisk_deliteley(b, c, d, f):
    mnogestvo = set() #инициализируем множество внутри функции
    if f != 0:
        for i in range(1, int(f ** 0.5) + 1): #универсальный оптимизированный метод поиска делителей(проверяются все числа до корня)
            if f % i == 0:
                delitel = {i, f // i, -i, -(f // i)}  #Все делители числа f
    # так как f делится на i, то число f // i будет делиться на f. Так же эти числа могут быть отрицательными, что и прописано.
                for delitel in delitel:
                    if poisk_korney(delitel, b, c, d, f):
                        mnogestvo.add(delitel)
                #нахождение целых корнейуравнения среди делителей
    return mnogestvo
def poisk_korney(x, b, c, d, f):
    #поиск корней уравнения
    return x ** 4 + b * x ** 3 + c * x ** 2 + d * x + f == 0

result = poisk_deliteley(b, c, d, f)
if result:
    print(f'Целые корни: {result}')
else:
    print('Целых корней нет')
