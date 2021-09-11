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
        list = []
        if self._adjacency_list.keys():
            for node in self._adjacency_list.keys():
                list.append(node.__str__())
            return list
        else:
            return 'NULL'


    def get_neighbors(self, node):
        """
        Returns a collection of edges connected to the given node
        Include the weight of the connection in the returned collection
        get neighbors
        Arguments: node
        """
        return self._adjacency_list[node]


    def size(self):
        """
        Returns the total number of nodes in the graph
        Arguments: none
        """
        return len(self._adjacency_list)


    def __str__(self):
        str = ''
        for node in self._adjacency_list.keys():

            str += f'[ {node.value} ] -> ['

            for edge in self._adjacency_list[node]:
                str += f" {edge.node.value}, "

            str += ']\n'
        return str


if __name__ == "__main__":
    graph = Graphs()

    a = graph.add_node('A')
    b = graph.add_node('B')
    c = graph.add_node('C')
    d = graph.add_node('D')
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
    print(graph)
    print(graph.size())