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
    with open('input.txt', 'r') as file:   
        if len(file.readlines()) < 2: 
            print('''The Input file shoud have atleast 2 lines:
            First line containing Initiator Node name.
            Second line onwards, each line should have 2 Node names separated by space: 
                1st Node name is dependent Node.
                2nd Node name is dependent on Node.
            ''')
            exit()
    
    with open('input.txt', 'r') as file:         
        initiator = file.readline().strip()
        print('Initiator: ', initiator)
        wait_for_graph: dict[str, Node] = {} 
        for line in file: 
            edge_lst = line.strip().split(' ')
            if len(edge_lst) > 2 or len(edge_lst) == 0:
                print('''Edge Node connections should have only 2 node name with a space inbetween''')
                exit()

            dependent_node = edge_lst[0] 
            depends_on_node = edge_lst[1]
            print(dependent_node, depends_on_node)
            if dependent_node in wait_for_graph: 
                wait_for_graph[dependent_node].depends_on.append(depends_on_node)
            else: 
                node = Node()
                node.node_name = dependent_node 
                node.depends_on.append(depends_on_node)
                wait_for_graph[dependent_node] = node 

        print('Wait For Graph', wait_for_graph)
    
    if initiator in wait_for_graph[initiator].depends_on: 
        print('Deadlock Detected.')
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
            print('One Probe discarded', probe)

    print('No Deadlock Detected')

        
    