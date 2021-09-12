from graph.stack_and_queue import Stack, Queue

class Node():

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Edge():
    def __init__(self, node, weight=1):
        self.node = node
        self.weight = weight


class Graphs():

    def __init__(self):
        self._adjacency_list = {}


    def add_node(self, value):
        """
        Add a node to the graph
        Arguments: value
        Returns: The added node
        """
        node = Node(value)
        self._adjacency_list[node] = []
        return node

    def add_Edge(self, node1, node2, weight=1):
        """
        Adds a new edge between two nodes in the graph
        If specified, assign a weight to the edge
        Both nodes should already be in the Graph

        Arguments: 2 nodes to be connected by the edge, weight (optional)
        Returns: nothing
        """
        if node1 and node2 in self._adjacency_list:
            self._adjacency_list[node1].append(Edge(node2, weight))

    def get_nodes(self):
        """
        Returns all of the nodes in the graph as a collection (set, list, or similar)
        Arguments: none
        """
        if self._adjacency_list:
            return [key.value for key in self._adjacency_list]
        else:
            return 'null'


    def get_neighbors(self, node):
        """
        Returns a collection of edges connected to the given node
        Include the weight of the connection in the returned collection
        get neighbors
        Arguments: node
        """
        return [(edge.node.value, edge.weight) for edge in self._adjacency_list[node]]

    def size(self):
        """
        Returns the total number of nodes in the graph
        Arguments: none
        """
        return len(self._adjacency_list)


    def breadth_first(self, node):
        """
        Write the following method for the Graph class:
        breadth first
        Arguments: Node
        Return: A collection of nodes in the order they were visited.
        Display the collection
        """
        if node not in self._adjacency_list:
            return 'node are  not in Graph'
        elif self._adjacency_list[node]==[]:
            return 'node does not have any neighbors'
        breadth = Queue()
        visited = []
        nodes = []
        breadth.enqueue(node)
        visited.append(node)
        
        while breadth.front:
            front = breadth.dequeue()
            nodes.append(front.value)

            for child in self._adjacency_list[front]:

                if child.node not in visited:
                    visited.append(child.node)
                    breadth.enqueue(child.node)

        return nodes

    def __str__(self):
        str = ''
        for node in self._adjacency_list:
            str += f'[{node.value}] -> {self.get_neighbors(node)}\n'
        return str

if __name__ == "__main__":
    graph = Graphs()
    a = graph.add_node('A')
    b = graph.add_node('B')
    c = graph.add_node('C')
    d = graph.add_node('D')
    graph.add_Edge(a, a, 1)
    graph.add_Edge(a, b, 4)
    graph.add_Edge(a, d, 9)
    graph.add_Edge(a, c, 3)
    graph.add_Edge(b, a, 4)
    graph.add_Edge(b, d, 5)
    graph.add_Edge(c, a, 3)
    graph.add_Edge(c, d, 6)
    graph.add_Edge(d, a, 9)
    graph.add_Edge(d, b, 5)
    graph.add_Edge(d, c, 6)
    print(graph.get_nodes())
    print(graph.get_neighbors(a))
    print(graph.get_neighbors(b))
    print(graph.get_neighbors(c))
    print(graph.get_neighbors(d))
    print(graph.size())
    print(graph)


    graph_new = Graphs()
    pandora = graph_new.add_node('Pandora')
    arendelle = graph_new.add_node('Arendelle')
    metroville = graph_new.add_node('Metroville')
    monstroplolis = graph_new.add_node('Monstroplolis')
    narnia = graph_new.add_node('Narnia')
    naboo = graph_new.add_node('Naboo')
    graph_new.add_Edge(pandora, arendelle, 1)
    graph_new.add_Edge(arendelle, metroville, 1)
    graph_new.add_Edge(arendelle, monstroplolis, 1)
    graph_new.add_Edge(metroville, arendelle, 1)
    graph_new.add_Edge(metroville, monstroplolis, 1)
    graph_new.add_Edge(metroville, narnia, 1)
    graph_new.add_Edge(metroville, naboo, 1)
    graph_new.add_Edge(monstroplolis, arendelle, 1)
    graph_new.add_Edge(monstroplolis, metroville, 1)
    graph_new.add_Edge(monstroplolis, arendelle, 1)
    graph_new.add_Edge(narnia, metroville, 1)
    graph_new.add_Edge(narnia, naboo, 1)
    graph_new.add_Edge(naboo, monstroplolis, 1)
    graph_new.add_Edge(naboo, metroville, 1)
    graph_new.add_Edge(naboo, narnia, 1)
    print(graph_new.breadth_first(pandora))