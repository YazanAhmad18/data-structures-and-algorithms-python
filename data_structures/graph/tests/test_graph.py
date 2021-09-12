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




def test_breadth_1():
    graph = Graphs()
    pandora = graph.add_node('Pandora')
    arendelle = graph.add_node('Arendelle')
    metroville = graph.add_node('Metroville')
    monstroplolis = graph.add_node('Monstroplolis')
    narnia = graph.add_node('Narnia')
    naboo = graph.add_node('Naboo')
    graph.add_Edge(pandora, arendelle, 1)
    graph.add_Edge(arendelle, metroville, 1)
    graph.add_Edge(arendelle, monstroplolis, 1)
    graph.add_Edge(metroville, arendelle, 1)
    graph.add_Edge(metroville, monstroplolis, 1)
    graph.add_Edge(metroville, narnia, 1)
    graph.add_Edge(metroville, naboo, 1)
    graph.add_Edge(monstroplolis, arendelle, 1)
    graph.add_Edge(monstroplolis, metroville, 1)
    graph.add_Edge(monstroplolis, arendelle, 1)
    graph.add_Edge(narnia, metroville, 1)
    graph.add_Edge(narnia, naboo, 1)
    graph.add_Edge(naboo, monstroplolis, 1)
    graph.add_Edge(naboo, metroville, 1)
    graph.add_Edge(naboo, narnia, 1)
    actual = graph.breadth_first(pandora)
    expected = ['Pandora', 'Arendelle', 'Metroville', 'Monstroplolis', 'Narnia', 'Naboo']
    assert actual == expected


def test_breadth_2():
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
    actual = graph.breadth_first(a)
    expected = ['A', 'B', 'D', 'C']
    assert actual == expected


def test_breadth_node_is_not_in_graph():
    graph = Graphs()
    pandora = graph.add_node('Pandora')
    arendelle = graph.add_node('Arendelle')
    metroville = graph.add_node('Metroville')
    monstroplolis = graph.add_node('Monstroplolis')
    narnia = graph.add_node('Narnia')
    naboo = graph.add_node('Naboo')
    graph.add_Edge(pandora, arendelle, 1)
    graph.add_Edge(arendelle, metroville, 1)
    graph.add_Edge(arendelle, monstroplolis, 1)
    graph.add_Edge(metroville, arendelle, 1)
    graph.add_Edge(metroville, monstroplolis, 1)
    graph.add_Edge(metroville, narnia, 1)
    graph.add_Edge(metroville, naboo, 1)
    graph.add_Edge(monstroplolis, arendelle, 1)
    graph.add_Edge(monstroplolis, metroville, 1)
    graph.add_Edge(monstroplolis, arendelle, 1)
    graph.add_Edge(narnia, metroville, 1)
    graph.add_Edge(narnia, naboo, 1)
    graph.add_Edge(naboo, monstroplolis, 1)
    graph.add_Edge(naboo, metroville, 1)
    graph.add_Edge(naboo, narnia, 1)
    graph_sample = Graphs()
    xx = graph_sample.add_node('xx')
    actual = graph.breadth_first(xx)
    expected = 'node are  not in Graph'
    assert actual == expected



def test_breadth_node_donot_have_neighbors():
    graph = Graphs()
    pandora = graph.add_node('Pandora')
    arendelle = graph.add_node('Arendelle')
    metroville = graph.add_node('Metroville')
    monstroplolis = graph.add_node('Monstroplolis')
    narnia = graph.add_node('Narnia')
    naboo = graph.add_node('Naboo')
    dd = graph.add_node('dd')
    graph.add_Edge(pandora, arendelle, 1)
    graph.add_Edge(arendelle, metroville, 1)
    graph.add_Edge(arendelle, monstroplolis, 1)
    graph.add_Edge(metroville, arendelle, 1)
    graph.add_Edge(metroville, monstroplolis, 1)
    graph.add_Edge(metroville, narnia, 1)
    graph.add_Edge(metroville, naboo, 1)
    graph.add_Edge(monstroplolis, arendelle, 1)
    graph.add_Edge(monstroplolis, metroville, 1)
    graph.add_Edge(monstroplolis, arendelle, 1)
    graph.add_Edge(narnia, metroville, 1)
    graph.add_Edge(narnia, naboo, 1)
    graph.add_Edge(naboo, monstroplolis, 1)
    graph.add_Edge(naboo, metroville, 1)
    graph.add_Edge(naboo, narnia, 1)
    actual = graph.breadth_first(dd)
    expected = 'node does not have any neighbors'
    assert actual == expected

