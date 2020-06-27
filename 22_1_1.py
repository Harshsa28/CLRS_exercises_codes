def out_degree(adj_list):
    for i in adj_list:
        print(i,":",  len(adj_list[i]))

def in_degree(adj_list):
    in_deg = [0 for i in range(len(adj_list))]
    for i in adj_list:
        for j in adj_list[i]:
            in_deg[j-1] += 1
    for i in adj_list:
        print(i, ":" , in_deg[i-1])


x = {}
x[1] = [2]
x[2] = [4]
x[3] = [1,2]
x[4] = [3]

print(x)
in_degree(x)
