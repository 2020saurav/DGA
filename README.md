Distributed/Parallel Graph Algortihms
===================================================================

### Generating all connected subgraphs of a given graph
___________________________________________________________
*	We will progress in stages. At the end of ith stage we will have all the connected subgraphs which have less than equal to i edges. We will have a distributed global queue which will have all the newly generated subgraphs in the current stage. Each thread/server will pick a one of these subgraph at a time as a job and will process it.
Base case will be each edge as a connected subgraph.
*	When a server picks a graph from the queue it processes it as a job and generates all possible connected subgraphs (of actual graph), which can be constructed by adding exactly one edge to the graph. Then that server tries to put the newly generated graphs to the global queue. Before pushing the graph to the global queue the the graph is hashed and its presence is checked against a global bloom filter. If the newly generated graph was already present it is discarded else it is added to the the global queue.
*	Load balancing is very easy, every server is itself responsible for keeping itself busy. After finishing a job(expanding a given connected subgraph by adding exactly one edge) the server will pull one new subgraph from the global queue and process it.
