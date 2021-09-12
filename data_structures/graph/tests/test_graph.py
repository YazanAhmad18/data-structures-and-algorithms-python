from graph import __version__

from graph.graph import Graphs

def test_version():
    assert __version__ == '0.1.0'

def test_add_node():
    graph = Graphs()
    a = graph.add_node('D')
    actual = a.value
    expected = 'D'
    assert actual == expected



def test_add_edge():
    graph = Graphs()
    a = graph.add_node('A')
    b = graph.add_node('B')
    graph.add_Edge(a, b, 4)
    actual = graph._adjacency_list[a][0].node
    expected = b
    assert actual == expected

def test_get_nodes():
    graph = Graphs()
    a = graph.add_node('A')
    b = graph.add_node('B')
    c = graph.add_node('C')
    d = graph.add_node('D')
    actual = graph.get_nodes()
    expected = ['A', 'B', 'C', 'D']
    assert actual == expected

def test_get_neighbors():
    graph = Graphs()
    a = graph.add_node('A')
    b = graph.add_node('B')
    c = graph.add_node('C')
    d = graph.add_node('D')
    graph.add_Edge(a, b, 4)
    graph.add_Edge(a, d, 9)
    graph.add_Edge(a, c, 3)
    actual = graph.get_neighbors(a)
    expected = [('B', 4), ('D', 9), ('C', 3)]
    assert actual == expected

def test_size():
    graph = Graphs()
    a = graph.add_node('A')
    b = graph.add_node('B')
    c = graph.add_node('C')
    d = graph.add_node('D')
    actual = graph.size()
    expected = 4
    assert actual == expected


def test_size_empty():
    graph = Graphs()
    actual = graph.size()
    expected = 0
    assert actual == expected

def test_graph_with_only_one_node_and_edge():
    graph = Graphs()
    a = graph.add_node('A')
    graph.add_Edge(a, a, 1)
    actual = graph.get_neighbors(a)
    expected = [('A', 1)]
    assert actual == expected



def test_empty_graph():
    graph = Graphs()
    actual = graph.get_nodes()
    expected = "null"
    assert actual == expected

