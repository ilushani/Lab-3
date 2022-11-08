def find(s, curelement):
    s += 1
    for j in range(curelement, 12):
        number[s - 1] = j
        if j < 11:
            find(s, j + 1)
        else:
            weight = 0
            value = 0
            for i in range(s):
                weight += slist[number[i]][0]
                value += slist[number[i]][1]
            if (weight <= maxweight) and (value >= 100):
                print(number[:s])
    s -= 1


def get_all_points_count(stufflist):
    summ = 0
    for item in stufflist:
        summ += item[1]
    return summ


def get_i(slist, A):
    s = len(slist)
    V = [[0 for a in range(A + 1)] for i in range(s + 1)]

    for i in range(s + 1):
        for a in range(A + 1):
            if i == 0 or a == 0:
                V[i][a] = 0
            elif slist[i - 1][0] <= a:
                V[i][a] = max(slist[i - 1][1] +
                              V[i - 1][a - slist[i - 1][0]], V[i - 1][a])
            else:
                V[i][a] = V[i - 1][a]

    s = len(slist)
    result = V[s][A]
    a = A
    items_list = []

    for i in range(s, 0, -1):
        if result <= 0:
            break
        if result == V[i - 1][a]:
            continue
        else:
            items_list.append(i)
            result -= slist[i - 1][1]
            a -= slist[i - 1][0]

    return items_list


slist = ((3, 25, 'в'), (2, 15, 'п'), (2, 15, 'б'),
             (2, 20, 'а'), (1, 5, 'и'), (1, 15, 'н'),
             (3, 20, 'т'), (1, 25, 'о'), (1, 15, 'ф'),
             (1, 10, 'д'), (2, 20, 'к'), (2, 20, 'р'))

itemslist = get_i(slist, 9)
answer = [['', '', ''], ['', '', ''], ['', '', '']]
i = 0
j = 0
points_count = 0
for s in itemslist:
    points_count += slist[s - 1][1]
    for k in range(slist[s - 1][0]):
        answer[i][j] = slist[s - 1][2]
        if j < 2:
            j += 1
        else:
            j = 0
            i += 1
for i in answer:
    print(i)
print('Итоговые очки выживания:', 10 - get_all_points_count(slist) + 2 * points_count)



allpoints = get_all_points_count(slist)
number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
maxweight = 9
s = 0
find(0, 0)