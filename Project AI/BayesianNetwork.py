from Node import Node


class BayesianNetwork:
    def __init__(self, nodes_number, adj_matrix):
        self.n = nodes_number  # numero nodi
        self.nodes = []  # vettore dei nodi del grafo
        for i in range(0, self.n):
            self.nodes.append(Node(i))

        self.adj_matrix = adj_matrix  # matrice di adiacenza
        for i in range(len(self.adj_matrix)):
            for j in range(len(self.adj_matrix)):
                if self.adj_matrix[j, i] == 1:
                    self.nodes[i].pi.append(j)
