from topological_order import topological_order
import numpy as np
import random


def dataset_gen(n, adj_matrix, nodes, prob):
    random.seed()
    dataset = np.zeros((n, len(nodes)))
    ordered = topological_order(nodes, adj_matrix)
    for i in range(n):
        for j in ordered:
            value = random.random()
            parents = nodes[j].pi
            # se il nodo non ha genitori
            if len(parents) == 0:
                if value <= prob[j]:
                    dataset[i, j] = 1
                else:
                    dataset[i, j] = 0
            # se il nodo ha genitori
            else:
                position = 0
                # calcola la posizione in base al valore dei genitori, necessitando dell' ordine topologico
                for k in range(len(parents)):
                    position += dataset[i, parents[k]] * (2 ** k)
                if value <= prob[j][int(position)]:
                    dataset[i, j] = 1
                else:
                    dataset[i, j] = 0
    return dataset


def probabilities_dataset(nodes):
    prob = []

    for i in range(len(nodes)):
        parents = nodes[i].pi
        if len(parents) == 0:
            a = np.array([0.9])
            prob.append(a)
        if len(parents) == 1:
            if i == 1:
                a = np.array([0.2, 0.83])
                prob.append(a)
            elif i == 2:
                a = np.array([0.05, 0.21])
                prob.append(a)
            else:
                a = np.array([0.6, 0.8])
                prob.append(a)
        if len(parents) == 2:
            a = np.array([0.05, 0.69, 0.78, 0.8])
            prob.append(a)
    return prob
