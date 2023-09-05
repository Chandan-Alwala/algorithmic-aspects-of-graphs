# algorithmic-aspects-of-graphs

## Algorithm1
### K-Core Analysis on a graph
This program is designed to perform k-core analysis on an undirected graph represented by its adjacency matrix. The program takes a positive integer k and the adjacency matrix of the graph as input and outputs the list of nodes that belong to the k-core of the graph. 

### Task 1: Algorithm Implementation
The core functionality of this program is implemented in the k_core_analysis function. It takes two inputs: k and the adjacency matrix of the graph. The function calculates the k-core and returns a list of nodes belonging to the k-core.

### Task 2: Generating Input Graph
The input graph for this program is generated based on your 10-digit student ID. Here are the steps to generate the adjacency matrix:

- Replace even digits with 0 and odd digits with 1 in your student ID.
- Repeat the resulting bit sequence 68 times to create a 680-bit long sequence.
- Fill a 26x26-sized adjacency matrix with the 26-bit sub-sequences.
- Transform the matrix to ensure it's undirected with no self-loops, parallel edges, and isolated nodes.

### Task 3: Running K-Core Analysis
The program runs the k_core_analysis function for all values of k starting from 1, and continues until it produces non-empty k-cores. The results are stored and can be visualized.

### Task 4: Visualization
To illustrate the results, the program generates a figure similar to Figure 1. It uses software to create a professional-quality visualization of the k-core structure of the graph.

### Task 5: Experimenting with Edge Deletion
The program also allows for experimenting with the effect of edge deletion on the k-cores of the graph. You can remove edges from the adjacency matrix and re-run the k-core analysis to observe how the k-cores change.


