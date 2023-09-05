def generate_adjacency_matrix(bits):
    sequence = bits * 68
    rows = []
    for i in range(0, len(sequence), 26):
        rows.append(sequence[i:i+26])

    # Create the initial adjacency matrix
    matrix = []
    for row in rows:
        matrix.append([int(bit) for bit in row])

    # Pad the matrix if it's not 26x26
    if len(matrix) < 26:
        padding = [[1] * 26 for _ in range(26 - len(matrix))]
        matrix += padding
    elif len(matrix) > 26:
        matrix = matrix[:26]

    # Eliminate isolated nodes
    isolated_nodes = set()
    for i in range(len(matrix)):
        if sum(matrix[i]) == 0:
            isolated_nodes.add(i)
    for node in isolated_nodes:
        matrix[node][0] = matrix[node][-1] = 1
        matrix[0][node] = matrix[-1][node] = 1

    # Replace main diagonal with 0
    for i in range(len(matrix)):
        matrix[i][i] = 0

    # Make the matrix symmetric
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j] = matrix[j][i]

    return matrix

# Example usage
input_bits = "0001000111"
adjacency_matrix = generate_adjacency_matrix(input_bits)
for row in adjacency_matrix:
    print(row)
