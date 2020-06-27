x = {}
x[1] = [2]
x[2] = [4]
x[3] = [1,2]
x[4] = [3]
print(x)


def transpose(adj_list):
    y = {}
    for i in adj_list:
        for j in adj_list[i]:
            if j in y:
                y[j].append(i)
            else:
                y[j] = [i]
    print(y)

transpose(x)

