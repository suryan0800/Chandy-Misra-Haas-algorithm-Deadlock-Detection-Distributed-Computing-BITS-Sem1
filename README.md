# Chandy Mishra Haas Alogorithm (Deadlock Detection)
## Assumptions: 
- Sites are ignored / All Nodes are from different sites
- Input a file in below format:
    - Deadlock Detection Initiatator Node (eg. a)
    - Wait for Graph (WFG) in below format: 
        - a -> b 
        - b -> c 
        - a -> c 
- Only deadlocks formed in a cycle can be detected 
