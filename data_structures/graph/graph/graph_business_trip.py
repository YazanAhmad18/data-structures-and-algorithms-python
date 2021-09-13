from graph.graph import Graphs

def graph_business_trip(graph, townes_array):
    """
    Write a function called business trip
    Determine whether the trip is possible with direct flights, and how much it would cost.
    Arguments: graph, array of city names
    Return: cost or null
    """
    journey = False
    journey_two = False
    cost = 0
    for town_name in range(len(townes_array) - 1):
        line_edges = graph._adjacency_list[townes_array[town_name]]
        journey_two = False

        for line in line_edges:
            if townes_array[town_name + 1] == line.node:
                cost += line.weight
                journey = True
                journey_two = True

    journey = journey and journey_two
   
    if not journey:
        cost = 0
        journey = False
        return f"{journey},${cost}"

    return f"{journey},${cost}"
if __name__ == "__main__":
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

    print(graph_business_trip(g, [metroville, pandora,]))
    print(graph_business_trip(g, [arendelle, monstroplolis, naboo]))
    print(graph_business_trip(g, [naboo, pandora]))
    print(graph_business_trip(g, [narnia, arendelle, naboo]))

