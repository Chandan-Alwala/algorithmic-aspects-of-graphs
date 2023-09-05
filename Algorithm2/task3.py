import itertools

def calculate_network_reliability(p, number_of_edges, number_of_nodes):
    try:
        # Generate all possible states of the edges (0 for down, 1 for up)
        states = list(itertools.product([0, 1], repeat=number_of_edges))

        def is_network_connected(s):
            adj_matrix = [
                [0,    s[0],  s[1],  0,     0,     s[2],  0   ],
                [s[0], 0,     s[3],  s[4],  0,     0,     0   ],
                [s[1], s[3],  0,     0,     s[5],  s[6],  0   ],
                [0,    s[4],  0,     0,     s[7],  0,     0   ],
                [0,    0,     s[5],  s[6],  0,     0,     s[8]],
                [s[2], 0,     s[7],  0,     0,     0,     s[9]],
                [0,    0,     0,     0,     s[8],  s[9],  0   ]
            ]

            def dfs(node, visited):
                visited[node] = True
                for neighbor in range(number_of_nodes):
                    if adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
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

        return network_reliability

    except Exception as e:
        # Handle exceptions and print error message
        print("An error occurred:", str(e))
        return None

def frange(start, end, step):
    while start <= end:
        yield start
        start += step

def main():
    start_p = 0.05
    end_p = 1.0
    step_size = 0.05

    number_of_edges = 10
    number_of_nodes = 7

    for p in frange(start_p, end_p, step_size):
        reliability = calculate_network_reliability(p, number_of_edges, number_of_nodes)
        print(f"Network reliability for p = {p:.2f}: {reliability:.5f}")
        print("-" * 50)

if __name__ == "__main__":
    main()
