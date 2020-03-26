class Node:
    def __init__(self, value):
        self.value = value
        self.pi = []  # vettore dei nodi padri
        self.color = None  # colore dei nodi
        self.d = 0  # tempo di scoperta
        self.f = 0  # tempo di fine
