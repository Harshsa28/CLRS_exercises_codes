x = {}
x[1] = [1,2]
x[2] = [1,3,3]
x[3] = [1,4]
x[4] = [3,4]

def square(adj_list):
    y = {}
    for i in adj_list:
        y[i] = []
    for i in adj_list:
        for j in adj_list[i]:
            if j != i and j not in y[i]:
                y[i].append(j)

    print(y)
    print('*' * 20)
    for i in adj_list:
        for j in adj_list[i]:
            for k in adj_list[j]:
                if k not in y[i]:
                    y[i].append(k)
    print(adj_list)
    print('_' * 20)
    print(y)

square(x)
