# Chandy Mishra Haas Alogorithm (AND Model Deadlock Detection)
## Assumptions: 
- The whole graph is assumed to follow AND model Deadlock system
- Sites are ignored / All Nodes are assumed to be from different sites
- Input a file in below format:
    - Deadlock Detection Initiatator Node (eg. a)
    - Wait for Graph (WFG) in below format: 
        - a -> b 
        - b -> c 
        - a -> c 
- Only deadlocks formed in a cycle can be detected 

## Input file format 
### Sample Input file with annotations (Whatever shown in bracket is only for understanding purpose and not to be added in actual file): 
- 1st Line should contain the Node that initiates the Deadlock Detection algorithm 
- 2nd line onwards is dependency list to build the Wait For Graph (WFG) 
```
1 (Deadlock detection Initiator Node name) 
1 2 (Node1 depends on Node 2 (1 -> 2)) 
2 3 (Node2 depends on Node 3 (2 -> 3)) 
3 1 (Node 3 depends on Node 1(3 -> 1)) 
1 4 (Node 1 depends on Node 4(1 -> 4)) 
. 
. 
. 
```
## Project Setup and execution 
- Install Python Interpretor with Version 3.6 or above and setup environment variables
- Edit the [input.txt](./input.txt) file for input to the program
- Run below command in terminal/CMD: 
```
python chandy-mishra-haas-algo.py 
```

## Data Structure 
- Each Process maintains:
    - Dependent array with size to the number of nodes
    - direct dependency node list 
- A Hashmap Data structure is used to find the Process for simulation of the algorithm
- Probe - Triplet data structure is used to send message between Nodes

## Performance Analysis
- One probe message is sent of every edge of WFG. 
- The size of probe message is fixed and is very small. 

## Reference: 
- Book: Distributed Computing Ajay D.Kshemkalyani and Mukesh Singhal - Chapter 10.7 - ISBN 978-1-107-64890-6 
- Lecture Notes and Videos from BITS Lecturer BARSHA MITRA