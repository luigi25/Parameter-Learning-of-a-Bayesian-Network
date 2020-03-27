# Parameter Learning of a Bayesian Network
Il programma tratta di un semplice modello di rete Bayesiana inerente al problema di un cancro metastatico. Si genera un data set casuale, di dimensione n crescente, a partire dalla rete Bayesiana considerata e dalle probabilità condizionate dei vari nodi che costituiscono la rete stessa. Successivamente, da questa generazione del data set, si ricavano i parametri da apprendere e si confrontano con le probabilità iniziali, che sono state fornite precedentemente, attraverso la divergenza di Jensen-Shannon. Infine, i risultati vengono visualizzati su un grafico per la visione della learning curve, verificando che la divergenza si riduce progressivamente al crescere di n.


## Useful links

Link utile per la visione della struttura della rete Bayesiana [**metastatic_cancer**](https://github.com/luigi25/EsameAI/blob/master/Project%20AI/Metastatic%20Cancer/metastic_cancer.bn) memorizzata nel progetto.

Link utile usato per l'apprendimento dei parametri in reti Bayesiane, dove è stato utilizzato l'approccio Bayesiano descritto in [**Heckerman 1997**](http://machinelearning102.pbworks.com/f/Tutorial-BayesianNetworks.pdf).


## Requirements

Il linguaggio di programmazione scelto per l'elaborato è Python, utilizzato con l'ambiente di sviluppo PyCharm IDE.

Necessaria l'installazione di alcuni packages nell'ambiente di sviluppo:

* **random**: implementa generatori di numeri pseudo-casuali per diverse distribuzioni e, nel progetto, viene utilizzato per la generazione del data set.
        
* itertools: implementa una serie di funzioni per lavorare con data sets iterabili. In questo caso viene utilizzato per la creazione di tutte le possibili configurazioni dei nodi genitori del vertice in questione.
        
* numpy: implementa funzioni scientifiche ideate per compiere operazioni su vettori e matrici dimensionali, difatti viene utilizzato proprio con questo scopo.
        
* copy: implementa funzioni utilizzate per la copia di oggetti, dunque viene utilizzato per eseguire la copia del vettore dei nodi.
        
* matplotlib: implementa funzioni per la creazione di grafici per il linguaggio di programmazione Python, infatti, viene utilizzato per la visualizzazione grafica della learning curve della divergenza di Jensen-Shannon.


## Code

### Node.py
        
* La classe Node costituisce i nodi della rete Bayesiana. Ogni nodo possiede un valore, un vettore dei nodi genitori, un colore, un tempo di scoperta e un tempo di terminazione. Questi campi sono utilizzati per la visita in profondità, al fine di ottenere un ordinamento topologico dei nodi: è indispensabile controllare se un evento, rappresentato da un nodo, si sia verificato o meno in base alle possibili configurazioni dei nodi genitori.

### BayesianNetwork.py

* La classe BayesianNetwork rappresenta il directed acyclic graph, detto DAG, ovvero la rete Bayesiana considerata. Contiene il numero di nodi presenti, il vettore dei nodi della rete e la matrice di adiacenza che riproduce la rete implementata.

### topological_order.py

* Contiene le funzioni per eseguire la visita in profondità dei nodi della rete: la dfs e la dfs_visit prendono in ingresso i nodi della rete e la matrice di adiacenza del DAG per l'esecuzione della visita. La funzione topological_order restituisce, dopo l'esecuzione della dfs, l'ordinamento topologico dei nodi della rete, ovvero, il vettore dei vertici in ordine di tempo di fine decrescente.
        
### dataset_generator.py

* La funzione probabilities_dataset riceve il vettore dei nodi e crea un array contenente, per ogni vertice, il vettore di tutte le probabilità che accada l'evento considerato in base alle possibili configurazioni dei nodi genitori, se presenti.
       
* La funzione dataset_gen prende in ingresso un numero n di elementi del data set, la matrice di adiacenza della rete, il vettore dei nodi di questa e l'array delle probabilità creato dalla funzione probilities_dataset. La funzione restituisce un data set di dimensione n, generando un numero casuale tra 0 e 1 e confrontandolo, nodo per nodo in base all'ordinamento topologico, alle probabilità condizionate presenti. Il data set è creato inserendo i valori 0 o 1 in base al risultato del confronto.
       
### parameter_learning.py

* La funzione learning prende in ingresso i nodi del grafo, il data set e le righe n di quest'ultimo al fine di apprendere i parametri da stimare. In principio, vengono fatte una serie di assunzioni descritte nell'articolo presente nella sezione "Useful links" e nella relazione del progetto e, successivamente, sono stati calcolati gli Nij/Nijk. In seguito, viene eseguito il calcolo dei paramentri usando come prior pseudo-counts unitari, ovvero, aijk=1 e aij=2 (Laplace Smoothing). La funzione restituisce qn, il vettore contenente la distribuzione appresa su un data set di dimensione n.
        
### jensen_shannon.py
        
* La funzione js_divergence prende in ingresso il vettore delle probabilità p e il vettore contenente la distribuzione appresa su un data set di dimensione n, qn. Restituisce la distanza misurata tra le due distribuzioni di probabilità, utilizzando la formula della divergenza di Jensen-Shannon.
        
### main.py

* Nel main viene creato il vettore di tutte le probabilità associate alla rete, la matrice di adiacenza che rappresenta la rete Bayesiana considerata e, infine, viene creata la rete con il nome di "Metastatic Cancer" contenente 5 nodi e 5 archi. Successivamente, si ha la generazione di diversi data sets di dimensione n crescente, infatti, partendo con un numero di 10 prove si arriva fino ad un massimo di 5010 con passo 100. A quel punto, è eseguito il learning dei parametri e viene calcolata la divergenza di Jensen-Shannon. In conclusione, è visualizzata la learning curve della divergenza calcolata, effettuando diverse prove (50) e facendo la media di queste per ottenere un risultato più verosimile possibile al target.
