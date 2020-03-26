from dataset_generator import dataset_gen, probabilities_dataset
from BayesianNetwork import BayesianNetwork
from jensen_shannon import js_divergence
from parameter_learning import learning
import matplotlib.pyplot as plt
import numpy as np


def main():
    probabilities = [0.9, 0.1, 0.83, 0.17, 0.2, 0.8, 0.21, 0.79, 0.05, 0.95, 0.8, 0.2, 0.78, 0.22, 0.69, 0.31,
                     0.05, 0.95, 0.8, 0.2, 0.6, 0.4]

    adj_matrix = np.array([[0, 1, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 1, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

    network = BayesianNetwork(5, adj_matrix)
    nodes = network.nodes
    prob_dataset = probabilities_dataset(nodes)

    x = []
    y = []
    start = 10
    end = 5010
    attempt = 50
    iteration = 100
    for n in range(start, end, iteration):
        x.append(n)
        z = []
        for j in range(attempt):
            dataset = dataset_gen(n, adj_matrix, nodes, prob_dataset)
            qn = learning(nodes, dataset, n)
            divergence = js_divergence(probabilities, qn)
            z.append(divergence)
        y.append(sum(z) / attempt)

    print("x: ", x)
    print("y: ", y)
    plt.title("Learning curve of Jensen-Shannon divergence")
    plt.xlabel("Dimensione del dataset")
    plt.ylabel("Divergenza tra probabilità e qn")
    plt.plot(x, y)
    plt.savefig('Jensen-Shannon divergence.png')
    plt.clf()


if __name__ == '__main__':
    main()
