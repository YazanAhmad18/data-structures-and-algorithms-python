from graph.graph import Graphs
from graph.graph_business_trip import graph_business_trip
import pytest



def test_graph_business_trip_one(graph_townes):
    actual = graph_business_trip(
        graph_townes[0], [graph_townes[3], graph_townes[1]])
    expected = "True,$82"

    assert actual == expected

def test_graph_business_trip_two(graph_townes):

    actual = graph_business_trip(
        graph_townes[0], [graph_townes[2], graph_townes[4], graph_townes[6]])
    expected = "True,$115"
    assert actual == expected

def test_graph_business_trip_three(graph_townes):

    actual = graph_business_trip(
        graph_townes[0], [graph_townes[6], graph_townes[1]])
    expected = "False,$0"
    assert actual == expected


def test_graph_business_trip_four(graph_townes):

    actual = graph_business_trip(
        graph_townes[0], [graph_townes[5], graph_townes[2], graph_townes[6]])
    expected = "False,$0"
    assert actual == expected


@pytest.fixture
def graph_townes():
    g = Graphs()
    pandora = g.add_node('Pandora')
    arendelle = g.add_node('Arendelle')
    metroville = g.add_node('Metroville')
    monstroplolis = g.add_node('Monstroplolis')
    narnia = g.add_node('Narnia')
    naboo = g.add_node('Naboo')
    g.add_Edge(pandora, arendelle, 150)
    g.add_Edge(pandora, metroville, 82)
    g.add_Edge(arendelle, pandora, 150)
    g.add_Edge(arendelle, metroville, 99)
    g.add_Edge(arendelle, monstroplolis, 42)
    g.add_Edge(metroville, pandora, 82)
    g.add_Edge(metroville, arendelle, 99)
    g.add_Edge(metroville, monstroplolis, 105)
    g.add_Edge(metroville, naboo, 26)
    g.add_Edge(metroville, narnia, 37)
    g.add_Edge(monstroplolis, arendelle, 42)
    g.add_Edge(monstroplolis, metroville, 105)
    g.add_Edge(monstroplolis, naboo, 73)
    g.add_Edge(naboo, monstroplolis, 73)
    g.add_Edge(naboo, metroville, 26)
    g.add_Edge(naboo, narnia, 250)
    g.add_Edge(narnia, metroville, 37)
    g.add_Edge(narnia, naboo, 250)
    return [g, pandora, arendelle, metroville, monstroplolis, narnia, naboo]
