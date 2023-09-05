import numpy as np

def find_k_core(k, adjacency_matrix):
    n = len(adjacency_matrix)
    degrees = np.sum(adjacency_matrix, axis=0)  # Calculate the degrees of each node

    remaining_nodes = list(range(n))
    changed = True
    
    while changed:
        changed = False
        for node in remaining_nodes:
            if degrees[node] < k:
                degrees -= adjacency_matrix[node]
                remaining_nodes.remove(node)
                changed = True
    
    k_core = remaining_nodes  # Nodes in the k-core
    
    return k_core

def find_all_k_cores(adjacency_matrix):
    n = adjacency_matrix.shape[0]
    max_k = n - 1

    all_k_cores = {}
    for k in range(1, max_k + 1):
        k_core = find_k_core(k, adjacency_matrix)
        if not k_core:  # Break out of the loop if k-core is empty
            break
        all_k_cores[k] = k_core
    
    return all_k_cores

# Example usage
adjacency_matrix = np.array([[0, 1, 1, 1],
                             [1, 0, 1, 0],
                             [1, 1, 0, 0],
                             [1, 0, 0, 0]])

all_k_cores = find_all_k_cores(adjacency_matrix)

# Print the nodes in each k-core
for k, k_core in all_k_cores.items():
    print("Nodes in the", k, "-core:", k_core)
