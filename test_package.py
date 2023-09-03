from typing import List
from GraphExplorer import Graph, Node

if __name__ == "__main__":
    print("Testing GraphExplorer package")
    nodes : List[Node] = []
    for i in range(5):
        nodes.append(Node(str(i),False))
    
    nodes[0].addNode(nodes[1])
    nodes[0].addNode(nodes[2])
    nodes[1].addNode(nodes[3])
    nodes[2].addNode(nodes[4])
    nodes[3].addNode(nodes[0])

    graph = Graph(nodes)