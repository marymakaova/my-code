b = float(input("Введите b: "))
c = float(input("Введите c: "))
d = float(input("Введите d: "))
f = float(input("Введите f (f != 0): "))

def poisk_korney(x, b, c, d, f):
    #Проверяет, является ли x целым корнем уравнения
    return x**4 + b*x**3 + c*x**2 + d*x + f == 0

def find(b, c, d, f):
    #Находит целые корни и выводит их на экран.
    cnt = 0  # Счетчик найденных корней
    for i in range(1, int(abs(f)**0.5) + 1):
        if f % i == 0:
            for divisor in {i, -i, f // i, -f // i}:
                if poisk_korney(divisor, b, c, d, f):
                    print("Целый корень:", divisor)
                    cnt += 1

    if cnt == 0:
        print("Целых корней нет")

find(b, c, d, f)