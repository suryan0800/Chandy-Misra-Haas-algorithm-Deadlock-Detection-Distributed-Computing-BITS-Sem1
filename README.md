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
- Initially all dependent array is set to false

## Input file format: 
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
## Project setup and execution: 
- Install Python Interpretor with Version 3.6 or above and setup environment variables
- Edit the [input.txt](./input.txt) file for input to the program
- Run below command in terminal/CMD: 
```
python chandy-mishra-haas-algo.py 
```
- Run any of below command to specify an input file manually:
```
python chandy-mishra-haas-algo.py ./input-no-deadlock.txt 
```
```
python chandy-mishra-haas-algo.py ./input-self-loop-deadlock.txt
```
```
python chandy-mishra-haas-algo.py ./input-no-deadlock-in-cycle-but-deadlock-exists.txt
```
```
python chandy-mishra-haas-algo.py ./input-multicycle-deadlock.txt
```

## Sample Output of the Program
```
Input File Name/Path:  input.txt

Initiator Node Name:  11

WFG Node Edges:
11  ->  21
11  ->  32
21  ->  24
24  ->  54
44  ->  24
54  ->  11
32  ->  33

Wait For Graph:
{'11': Node(node_name: 11, depends_on: ['21', '32'], dependent: {}), '21': Node(node_name: 21, depends_on: ['24'], dependent: {}), '24': Node(node_name: 24, depends_on: ['54'], dependent: {}), '44': Node(node_name: 44, depends_on: ['24'], dependent: {}), '54': Node(node_name: 54, depends_on: ['11'], dependent: {}), '32': Node(node_name: 32, depends_on: ['33'], dependent: {})}

Deadlock Detection Algorithm Simulation Initiated:
Started probing for Deadlock Detection
Probe(initiator: 11, sender: 11, receiver: 21)
Probe(initiator: 11, sender: 11, receiver: 32)
Probe(initiator: 11, sender: 21, receiver: 24)
Probe(initiator: 11, sender: 32, receiver: 33)
One Probe discarded:  Probe(initiator: 11, sender: 32, receiver: 33)
Probe(initiator: 11, sender: 24, receiver: 54)
Probe(initiator: 11, sender: 54, receiver: 11)
Deadlock Detected.
```

## Data Structure:
- Each Process maintains:
    - Dependent array with size to the number of nodes
    - Direct dependency node list 
- A Hashmap Data structure is used to find the Process for simulation of the algorithm
- Probe - Triplet data structure is used to send message between Nodes

## Performance Analysis:
- One probe message is sent of every edge of WFG. 
- The size of probe message is fixed and is very small. 

## Reference: 
- Book: Distributed Computing Ajay D.Kshemkalyani and Mukesh Singhal - Chapter 10.7 - ISBN 978-1-107-64890-6 
- Lecture Notes and Videos from BITS Lecturer BARSHA MITRA