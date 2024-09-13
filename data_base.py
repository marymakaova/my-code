from random import *
names = ['Jack', 'Robert', 'Mick', 'James', 'Ann', 'Kate', 'Julia']
surnames = ['White',  'Smith',  'Black', 'Simpson', 'Jackson', 'Trueman ']
streets = ['Wall-Street', '5-th Avenue', ' Broadway',  'Baker Street', 'Abbey Road']
data_base = []

for i in range(50):
    ident = str(i)
    while len(ident) != 3:
        ident = '0' + ident
    name = choice(names)
    surname = choice(surnames)
    age = randint(0, 80)
    street = choice(streets)
    profit = randint(100, 5000)
    if age >= 21:
        cr_credit = randint(0, 2)
        career = randint(0, 3)
    else:
        cr_credit = 0
        career = randint(0, 1)

    data_base.append([ident, name, surname, age, street, profit, career, cr_credit])


indexes = set()
data_family = []
for i in range(50):
    cur_family = [data_base[i]]
    for j in range(i + 1, 50):
        if (cur_family[0][2] == data_base[j][2]) and (cur_family[0][4] == data_base[j][4]) and (j not in indexes):
            cur_family.append(data_base[j])
            indexes.add(j)
    if len(cur_family) == 1:
        cur_family = []
    else:
        data_family.append(cur_family)


for i in range(len(data_family)):
    average_profit = 0
    for j in range(len(data_family[i])):
        average_profit += data_family[i][j][5]
    average_profit = average_profit / len(data_family)
    result = 0
    for k in range(len(data_family[i])):
        if data_family[i][k][6] < 1 and average_profit < 2000:
            print(data_family[i][k], 'No credit, cause profit is not enough')
        elif data_family[i][k][3] < 21:
            print(data_family[i][k], 'No credit, cause person is so yang')
        elif data_family[i][k][6] <= 1 and data_family[i][k][7] > 0 and average_profit < 2500:
            print(data_family[i][k], 'No credit, cause you have some current credit')
        else:
            print(data_family[i][k], 'Yes you have a chance to take a credit')
            summa = data_family[i][k][5] * 6
            if summa > 30000:
                p = 10
            else:
                p = 13
            if data_family[i][k][7] > 0:
                p -= 2
            print('Сумма: ', summa, 'Процентная ставка', p, 'Ежемесячный платёж: ', summa * (1 + p / 100 / 12))
