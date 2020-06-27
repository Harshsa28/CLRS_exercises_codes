x = {}
x[1] = [1,2]
x[2] = [1,3,3]
x[3] = [1,4]
x[4] = [3,4]

def multi_to_single(adj_list):
    y = {}
    for i in adj_list:
        if i not in y:
            y[i] = []
    for i in adj_list:
        for j in adj_list[i]:
            if j != i and j not in y[i]:
                y[i].append(j)
                y[j].append(i)
    print(y)

multi_to_single(x)
