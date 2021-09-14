from graph.graph import Graphs
import pytest


def test_depth_first(graph):

    actual = graph[0].depth_first(graph[1])
    expected = ['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']
    assert actual == expected



def test_depth_first_node_is_not_in_the_graph(graph):
    g2 = Graphs()
    m = g2.add_node('M')
    actual = graph[0].depth_first(m)
    expected = 'node does not exist Graph'
    assert actual == expected




def test_depth_first_node_does_not_have_any_neighbors(graph):
    actual = graph[0].depth_first(graph[9])
    expected = 'node does not have any neighbors'
    assert actual == expected



@pytest.fixture
def graph():
    graph = Graphs()
    a = graph.add_node('A')
    b = graph.add_node('B')
    c = graph.add_node('C')
    d = graph.add_node('D')
    e = graph.add_node('E')
    f = graph.add_node('F')
    h = graph.add_node('H')
    g = graph.add_node('G')
    y = graph.add_node('Y')
    graph.add_Edge(a, b, 1)
    graph.add_Edge(a, d, 1)
    graph.add_Edge(b, a, 1)
    graph.add_Edge(b, c, 1)
    graph.add_Edge(b, d, 1)
    graph.add_Edge(c, b, 1)
    graph.add_Edge(c, g, 1)
    graph.add_Edge(d, a, 1)
    graph.add_Edge(d, b, 1)
    graph.add_Edge(d, e, 1)
    graph.add_Edge(d, h, 1)
    graph.add_Edge(d, f, 1)
    graph.add_Edge(e, d, 1)
    graph.add_Edge(f, d, 1)
    graph.add_Edge(f, h, 1)
    graph.add_Edge(g, c, 1)
    graph.add_Edge(h, d, 1)
    graph.add_Edge(h, f, 1)
    return [graph, a, b, c, d, e, f, h, g, y]