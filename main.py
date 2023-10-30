import networkx as nx

class WeightedGraph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_edge(self, node1, node2, weight):
        self.graph.add_edge(node1, node2, weight=weight)

    def shortest_path(self, source, destination):
        try:
            path = nx.shortest_path(self.graph, source=source, target=destination, weight='weight')
            path_cost = nx.shortest_path_length(self.graph, source=source, target=destination, weight='weight')
            return path, path_cost
        except nx.NetworkXNoPath:
            return None

