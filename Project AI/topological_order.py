import copy


# visita in profondità
def dfs(nodes, adj_matrix):
    for i in range(len(nodes)):
        nodes[i].color = "White"
        nodes[i].pi = None
    global time
    time = 0
    for i in range(len(nodes)):
        if nodes[i].color == "White":
            dfs_visit(nodes, i, adj_matrix)


def dfs_visit(nodes, index, matrix):
    global time
    time += 1
    nodes[index].color = "Gray"
    # controlla i nodi adiacenti al nodo con indice nodeIndex
    for i in range(len(nodes)):
        if matrix[index, i] == 1 and nodes[i].color == "White":
            nodes[i].pi = index
            dfs_visit(nodes, i, matrix)
    nodes[index].color = "Black"
    time += 1
    nodes[index].f = time
    return nodes[index].f


def topological_order(nodes, adj_matrix):
    c = copy.deepcopy(nodes)
    dfs(c, adj_matrix)
    c.sort(key=lambda n: n.f, reverse=True)
    ordered = []
    for i in range(len(nodes)):
        ordered.append(c[i].value)
    return ordered
