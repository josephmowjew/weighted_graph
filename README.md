# Weighted Graph Shortest Path

This Python solution demonstrates the creation of a weighted graph data structure using the `networkx` library. It includes functionality to add edges with weights, calculate the shortest path between two nodes, and visualize the graph.

## How It Works

The solution utilizes the `networkx` library to create an undirected graph and provides methods to add edges with weights and calculate the shortest path between nodes. It also employs the `matplotlib` library to draw and visualize the graph, highlighting the shortest path in red, if it exists.

## Required Libraries

Ensure you have the following libraries installed on your machine:

- `networkx`: For creating and manipulating graphs.
 ```bash
 pip install networkx
 ```

- `matplotlib`: For graph visualization.
 ```bash
 pip install matplotlib
 ```

## Usage

1. Instantiate the `WeightedGraph` class.
2. Add edges with weights using the `add_edge` method.
3. Specify the source and destination nodes.
4. Calculate the shortest path using the `shortest_path` method.
5. Visualize the graph with the highlighted shortest path.

Example:

```python
# Instantiate the weighted graph object
weighted_graph = WeightedGraph()

# Add edges with weights to the graph
weighted_graph.add_edge("Dedza", "Lilongwe", 40)
weighted_graph.add_edge("Lilongwe", "Nkhotakota", 60)
# Add more edges as needed

# Specify the source and destination nodes
source_district = "Dedza"
destination_district = "Nkhotakota"

# Calculate and print the shortest path and its cost
result = weighted_graph.shortest_path(source_district, destination_district)
print("Shortest path:", result[0])
print("Path cost:", result[1])

# Draw and visualize the graph
weighted_graph.visualize_graph()
