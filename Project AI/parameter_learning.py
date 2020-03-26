import numpy as np
import itertools


def learning(nodes, dataset, n):
    # ogni nodo i-esimo può assumere valori 0/1
    ri = 2
    # si utilizza Laplace Smoothing
    aij = 2
    aijk = 1
    qn = []
    Nij = []  # 2 dimensioni
    Nijk = []  # 3 dimensioni
    event = False
    # per ogni nodo i-esimo
    for i in range(len(nodes)):
        nij = []
        nijk = []
        config = []
        parents = nodes[i].pi
        # per ogni possibile configurazione dei genitori
        for c in itertools.product([0, 1], repeat=len(parents)):
            config.append(c)
        # se il nodo i-esimo ha dei genitori
        if len(parents) > 0:
            # per ogni configurazione j-esima dei genitori
            for j in range(2 ** len(parents)):
                counter_ijk = np.zeros(2)
                # per ogni riga del dataset n
                for n in range(n):
                    # per ogni genitore p
                    for p in range(len(parents)):
                        # per ogni possibile configurazione del nodo i-esimo
                        for k in range(ri):
                            # per ogni nodo controlla se la configurazione j-esima dei genitori è presente nel dataset
                            if dataset[n][parents[p]] == config[j][p] and event is False:
                                event = True
                                if len(parents) == 1:
                                    # controlla se è uguale alla configurazione k-esima del nodo
                                    if int(dataset[n][i]) == k:
                                        counter_ijk[int(dataset[n][i])] += 1
                                    event = False
                            # per ogni nodo controlla se la configurazione j-esima dei genitori è presente nel dataset
                            elif dataset[n][parents[p]] == config[j][p] and event is True:
                                # controlla se è uguale alla configurazione k-esima del nodo
                                if int(dataset[n][i]) == k:
                                    counter_ijk[int(dataset[n][i])] += 1
                                    event = False
                            else:
                                break
                # memorizzo per ogni configurazione j-esima
                nijk.append(counter_ijk)
                nij.append(sum(counter_ijk))
        # se il nodo i-esimo non ha i genitori
        else:
            counter_ijk = np.zeros(2)
            for n in range(n):
                for k in range(ri):
                    # controlla se è uguale alla configurazione k-esima del nodo
                    if int(dataset[n][i]) == k:
                        counter_ijk[int(dataset[n][i])] += 1
            nijk.append(counter_ijk)
            nij.append(sum(counter_ijk))
        # e per ogni nodo i
        Nijk.append(nijk)
        Nij.append(nij)
    # nodo i-esimo
    for i in range(len(nodes)):
        parents = nodes[i].pi
        # se il nodo ha dei genitori
        if len(parents) > 0:
            # configurazione j-esima dei genitori
            for j in range(2 ** len(parents)):
                # k-esima configurazione del nodo i
                for k in range(ri):
                    qn.append((aijk + Nijk[i][j][k]) / (aij + Nij[i][j]))
        # se il nodo non ha i genitori
        else:
            j = 0
            for k in range(ri):
                qn.append((aijk + Nijk[i][j][k]) / (aij + Nij[i][j]))
    return qn
