import sys 

class Node: 
    def __init__(self): 
        self.node_name: str = None 
        self.depends_on: list[str] = []
        self.dependent: dict[str, bool] = {}

    def __str__(self) -> str: 
        return 'Node(node_name: {0}, depends_on: {1}, dependent: {2})'.format(self.node_name, self.depends_on, self.dependent)
    
    def __repr__(self) -> str:
        return self.__str__()

class Probe: 
    initiator: str = None 
    sender: str = None 
    receiver: str = None 

    def __init__(self, initiator: str, sender: str, receiver: str): 
        self.initiator = initiator
        self.sender = sender
        self.receiver = receiver

    def __str__(self) -> str: 
        return 'Probe(initiator: {0}, sender: {1}, receiver: {2})'.format(self.initiator, self.sender, self.receiver)
    
    def __repr__(self) -> str:
        return self.__str__()


if __name__ == '__main__': 
    INPUT_FILE = 'input.txt'
    if len(sys.argv) >= 2:
        print(sys.argv[1])
        INPUT_FILE = sys.argv[1]
    print('Input File Name/Path: ', INPUT_FILE)
    print()

    with open(INPUT_FILE, 'r') as file:   
        if len(file.readlines()) < 2: 
            print('''The Input file shoud have atleast 2 lines:
            First line containing Initiator Node name.
            Second line onwards, each line should have 2 Node names separated by space: 
                1st Node name is dependent Node.
                2nd Node name is dependent on Node.
            ''')
            exit()
    
    with open(INPUT_FILE, 'r') as file:         
        initiator = file.readline().strip()
        print('Initiator Node Name: ', initiator)
        print()
        if len(initiator.strip().split(' ')) > 1: 
            print('Enter valid Initiator name. Initiator Node name should not contain spaces.')
            exit()
        print('WFG Node Edges: ')
        wait_for_graph: dict[str, Node] = {} 
        for line in file: 
            edge_lst = line.strip().split(' ')
            if len(edge_lst) != 2:
                print('''Edge Node connections should exactly have only 2 node name with a space inbetween''')
                exit()

            dependent_node = edge_lst[0] 
            depends_on_node = edge_lst[1]
            print(dependent_node, ' -> ', depends_on_node)
            if dependent_node in wait_for_graph: 
                wait_for_graph[dependent_node].depends_on.append(depends_on_node)
            else: 
                node = Node()
                node.node_name = dependent_node 
                node.depends_on.append(depends_on_node)
                wait_for_graph[dependent_node] = node 

        print()
        print('Wait For Graph: ')
        print(wait_for_graph)
        print()

    if initiator not in wait_for_graph: 
        print('Unable to find the initiator ({0}) in the WFG. Please provide a valid initiator node name'.format(initiator))
        exit()
    
    print('Deadlock Detection Algorithm Simulation Initiated:')
    print('Started probing for Deadlock Detection')
    if initiator in wait_for_graph[initiator].depends_on: 
        print('Deadlock Detected (Self Loop).')
        exit()

    # Initiate Probe 
    queue = [ Probe(initiator, initiator, node_name) for node_name in wait_for_graph[initiator].depends_on]

    while len(queue): 
        probe = queue.pop(0)
        print(probe)

        receiver_node = wait_for_graph[probe.receiver] if probe.receiver in wait_for_graph else None 
        if receiver_node is not None and len(receiver_node.depends_on) != 0 and probe.initiator not in receiver_node.dependent: 
            receiver_node.dependent[probe.initiator] = True 
            if probe.receiver == probe.initiator:
                print('Deadlock Detected.')
                exit()

            new_probes = [ Probe(initiator, probe.receiver, node_name) for node_name in wait_for_graph[probe.receiver].depends_on]
            queue.extend(new_probes)
        else: 
            print('One Probe discarded: ', probe)

    print('No Deadlock Detected by the Initiator ({0}).'.format(initiator))

        
    