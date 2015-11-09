# Distributed/Parallel Graph Algorithms

### Generating all connected subgraphs of a given graph

##### Presentation: http://www.slideshare.net/SauravKumar145/distributed-graph-algorithms

##### Algorithm

* Initailly each edge represents a connected subgraph of the given graph.
* The algorithm progresses in stages. In the ith stage, generate all the subgraphs of the given graph that have exactly i edges.
* In ith stage pick all subgraphs generated in (i-1)th stage, and extend the graphs by exactly one edge. In this way you will obtain all the subgraphs with exactly i edges from subgraphs of (i-1) edges((i-1)th stage).
* Keep only distinct subgraphs in each step using bloomfilter (which maybe cleared after each step to improve accuracy).

##### Architecture

* We implement this algorithm in a distributed environment using a master-slave architecture.
* Master is just for initialization and bookeeping. Slaves do all the processing.
* Suppose, we map(hash) each subgraph to a value(128 bit number). We use a distributed bloom filter on these values to maintain only distinct subgraphs. Initally, we shard the range of hash values. Each slave will maintain a bloom filter for a particular range of hash values. And each slave knows which bloom filter it must contact to check a hash value of a subgraph. This way no slave gets loaded and checking uniqueness is properly distributed.
* Each slave also has a task queue which actually consists of subgraphs. A slave will pick a task from any of the task queue(maybe randomly) and process it. After processing it will produce many subgraphs(i.e. tasks for the next stage) which would further be distributed (again maybe randomly) among all the task queues.


#### Messaging Protocols (Some are no longer needed. Check config/messageHeads)

- GETSERVERINFO : Request for list of servers from master
- INPUT : Send input to master
- HEARTBEAT : Pulse from slaves to master
- PING : Ping from a server to another
- PONG : Reply of PING, if server is alive
- PARTIALRESULT : Response from slaves with their results
- JOBCOMPLETE : Notification from slave to master
- SERVERINFO : Response with list of servers
- GRAPH : Graph from master to slaves
- PUSHTASK : Request to save the task in task queue
- POPPEDTASK : Response task after popping from task queue
- STARTPROCESSING : Notification from master to begin processing
- REQUESTTASK : Request a new task from another slave
- SENDPARTIALRESULT : Request to send partial result
- HASHCHECK : Request to check if the hash exists
- HASHRESPONSE : Response of HASHCHECK

Instant responses to be returned in cases of GETSERVERINFO, PING, HASHCHECK, REQUESTTASK, SENDPARTIALRESULT

#### Instructions to set up:
- Add environment variable PYTHONPATH.
  ```
  export PYTHONPATH="$PYTHONPATH:/path/to/DGA"
  ```
- Run `python setup.py` with args as serverID, serverIPaddr, port
- Deploy listeners of slaves
- Update config/servers of master server and deploy its listener
- Send input to master through user/run.py

