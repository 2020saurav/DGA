Distributed/Parallel Graph Algortihms
===================================================================
## Generating all connected subgraphs of a given graph
___________________________________________________________
### Algorithm
* Initailly each edge represents a connected subgraph of the given graph.
* The algorithm progresses in stages. In the ith stage, generate all the subgraphs of the given graph that have exactly i edges.
* In ith stage pick all subgraphs generated in (i-1)th stage, and extend the graphs by exactly one edge. In this way you will obtain all the subgraphs with exactly i edges from subgraphs of (i-1) edges((i-1)th stage).
* Keep only distinct subgraphs in each step using bloomfilter (which maybe cleared after each step to improve accuracy).
____________________________________________________________
### Architecture
* We implement this algorithm in a distributed environment using a master-slave architecture.
* Master is just for initialization and bookeeping. Slaves do all the processing.
* Suppose, we map(hash) each subgraph to a value(128 bit number). We use a distributed bloom filter on these values to maintain only distinct subgraphs. Initally, we shard the range of hash values. Each slave will maintain a bloom filter for a particular range of hash values. And each slave knows which bloom filter it must contact to check a hash value of a subgraph. This way no slave gets loaded and checking uniqueness is properly distributed.
* Each slave also has a task queue which actually consists of subgraphs. A slave will pick a task from any of the task queue(maybe randomly) and process it. After processing it will produce many subgraphs(i.e. tasks for the next stage) which would further be distributed (again maybe randomly) among all the task queues. 
