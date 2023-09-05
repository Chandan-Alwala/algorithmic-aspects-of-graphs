import itertools

def calculate_network_reliability(p, number_of_edges, number_of_nodes, adj_matrix):
    try:
        # Generate all possible states of the edges (0 for down, 1 for up)
        states = list(itertools.product([0, 1], repeat=number_of_edges))

        def is_network_connected(s):
            updated_adj_matrix = [row[:] for row in adj_matrix]
            
            for edge, status in zip(range(number_of_edges), s):
                i, j = divmod(edge, number_of_nodes)  # Convert edge index to matrix coordinates
                updated_adj_matrix[i][j] = status
                updated_adj_matrix[j][i] = status

            def dfs(node, visited):
                visited[node] = True
                for neighbor in range(number_of_nodes):
                    if updated_adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
                        dfs(neighbor, visited)

            visited = [False] * number_of_nodes
            dfs(0, visited)

            return all(visited)

        network_reliability = 0

        for state in states:
            if is_network_connected(state):
                state_probability = 1
                for i in range(len(state)):
                    if state[i] == 1:
                        state_probability *= p  # Edge is up
                    else:
                        state_probability *= (1 - p)  # Edge is down
                network_reliability += state_probability

        # Add debug information
        # print("All possible states of edges:", states)
        # print("Network reliability for each state:", [is_network_connected(state) for state in states])
        # print("Probabilities of each state:", [p if edge_up else (1 - p) for edge_up in states])
        print("Network reliability:", network_reliability)

        return network_reliability

    except Exception as e:
        # Handle exceptions and print error message
        print("An error occurred:", str(e))
        return None

# Example usage:
p = 0.9
number_of_edges = 10
number_of_nodes = 7
adj_matrix = [
    [0, 1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 0]
]

calculate_network_reliability(p, number_of_edges, number_of_nodes, adj_matrix)


# def calculate_network_reliability(number_of_edges, number_of_nodes, adj_matrix):
#     try:
#         def update_adj_matrix(s):
#             updated_adj_matrix = [row[:] for row in adj_matrix]

#             temp = number_of_edges        
#             for i in range(number_of_nodes):
#                 for j in range(i+1, number_of_nodes):
#                     if updated_adj_matrix[i][j] == 1:
#                         updated_adj_matrix[i][j] = s[number_of_edges - temp]
#                         temp = temp - 1

#             for i in range(number_of_nodes):
#                 for j in range(i + 1, number_of_nodes):
#                     updated_adj_matrix[j][i] = updated_adj_matrix[i][j]

#             return updated_adj_matrix
        
#         s = [9,8,7,6,5,4,3,2,2,2]
#         updated_matrix = update_adj_matrix(s)

#         for row in updated_matrix:
#             print(row)

#     except Exception as e:
#         # Handle exceptions and print error message
#         print("An error occurred:", str(e))
#         return None

# # Example usage:
# number_of_edges = 10
# number_of_nodes = 7
# adj_matrix = [
#     [0, 1, 1, 0, 0, 1, 0],
#     [1, 0, 1, 1, 0, 0, 0],
#     [1, 1, 0, 0, 1, 1, 0],
#     [0, 1, 0, 0, 1, 0, 0],
#     [0, 0, 1, 1, 0, 0, 1],
#     [1, 0, 1, 0, 0, 0, 1],
#     [0, 0, 0, 0, 1, 1, 0]
# ]

# calculate_network_reliability(number_of_edges, number_of_nodes, adj_matrix)
