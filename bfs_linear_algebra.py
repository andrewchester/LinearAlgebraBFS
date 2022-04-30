import numpy as np

# adjacency matrices, each array is a row, just like how you initialize it in Wolfram Alpha
test_matrices = [
    np.array([[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 1, 0]]), # 4x4 adjacency matrix, solution is 2
    np.array([[0, 1, 1, 0, 0],[1, 0, 1, 1, 0],[1, 1, 0, 1, 1],[0, 1, 1, 0, 1],[0, 0, 1, 1, 0]]), # 5x5 adjacency matrix, solution is 2
    np.array([[0, 1, 1, 0, 0, 0],[1, 0, 1, 0, 0, 0],[1, 1, 0, 0, 0, 0],[0, 0, 0, 0, 1, 0],[0, 0, 0, 1, 0, 1],[0, 0, 0, 0, 1, 0]]) # 6x6 adjacency matrix, no solution
]

# these are the premade starting and finishing values for each adjacency matrix
# it's always the first and the last vertex we are testing
test_cases = [
    (0, 3),
    (0, 4),
    (0, 5)
]

# prints a 2-dimensional matrix to the console
def print_matrix (A: list) -> None:
    for row in A:
        print (row)

# adjacency_matrix: this is an n x n square matrix. All connections are represented as 1's.
# start: the index of the starting vertex, the minimum is 0 and the max is n - 1 where n is the number of nodes
# finish: the index of the vertex we are searching for
# 
# if there is a connection, it will return an integer indicating the number of steps
# it takes to get from start -> finish
# if there isn't a connection, it will return 0 
def bfs_linear_algebra (adjacency_matrix: list, start: int, finish: int) -> int:
    n, m = adjacency_matrix.shape

    # testing if our input is a square matrix
    if n != m:
        print ("Didn't recieve an n x n square adjacency matrix.")
        return 0

    # neighbors will be a vector representing the neighbors of a given vertex
    # and it will store the results of repeated matrix multiplication
    neighbors = np.zeros(n)
    neighbors[start] = 1

    for i in range(n):
        if neighbors[finish]: # if this isn't a 0, the finishing vertex is connected to start
            return i
        neighbors = np.matmul(adjacency_matrix, neighbors) # multiplies the adjacency matrix by the neighbors vector
    return 0

# runs each test case in a loop
def run_tests():
    n = len(test_matrices)
    for i in range(n):
        start, finish = test_cases[i]
        matrix = test_matrices[i]
        
        print_matrix(matrix)
        print(f'Searching for path from {start} to {finish}')
        steps = bfs_linear_algebra(matrix, start, finish)
        if steps:
            print(f'Path exists {finish} can be reached in {steps} steps')
        else:
            print("No connection exists.")
        print()


if __name__ == '__main__':
    run_tests()