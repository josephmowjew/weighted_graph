# Import the networkx library with the alias nx
import networkx as nx

# Define a class for a weighted graph
class WeightedGraph:
    def __init__(self):
        # Initialize an undirected graph using the networkx Graph class
        self.graph = nx.Graph()

    def add_edge(self, node1, node2, weight):
        """
        Add an edge to the graph with specified nodes and weight.

        Parameters:
        - node1, node2: Nodes to connect with an edge
        - weight: The weight associated with the edge
        """
        # Add an edge to the graph with the specified weight
        self.graph.add_edge(node1, node2, weight=weight)

    def shortest_path(self, source, destination):
        """
        Calculate the shortest path and its cost from the source to the destination.

        Parameters:
        - source: The starting node
        - destination: The ending node

        Returns:
        - If a path exists, return a tuple containing the path and its total cost.
        - If no path exists, return None.
        """
        try:
            # Use networkx's shortest_path function to find the shortest path
            path = nx.shortest_path(self.graph, source=source, target=destination, weight='weight')
            
            # Use networkx's shortest_path_length function to find the length (cost) of the shortest path
            path_cost = nx.shortest_path_length(self.graph, source=source, target=destination, weight='weight')
            
            # Return the path and its cost as a tuple
            return path, path_cost
        except nx.NetworkXNoPath:
            # Handle the case where no path exists between the source and destination
            return None

# Instantiate the weighted graph object
weighted_graph = WeightedGraph()

# Add edges with weights to the graph
weighted_graph.add_edge("Dedza", "Ntcheu", 74)
weighted_graph.add_edge("Dedza", "Lilongwe", 92)
weighted_graph.add_edge("Lilongwe", "Mchinji", 109)
weighted_graph.add_edge("Mchinji", "Kasungu", 141)
weighted_graph.add_edge("Mchinji", "Kasungu", 141)
weighted_graph.add_edge("Kasungu", "Ntchisi", 66)
weighted_graph.add_edge("Ntchisi", "Nkhotakota", 66)
weighted_graph.add_edge("Nkhotakota", "Salima", 112)
weighted_graph.add_edge("Salima", "Dedza", 96)
weighted_graph.add_edge("Salima", "Dowa", 67)
weighted_graph.add_edge("Dowa", "Lilongwe", 55)
weighted_graph.add_edge("Dowa", "Ntchisi", 38)
weighted_graph.add_edge("Dowa", "Kasungu", 117)
# Add more edges as needed

# Specify the source and destination nodes
source_district = "Lilongwe"
destination_district = "Nkhotakota"

# Calculate and print the shortest path and its cost
result = weighted_graph.shortest_path(source_district, destination_district)
print("Shortest path:", result[0])
print("Path cost:", result[1])
