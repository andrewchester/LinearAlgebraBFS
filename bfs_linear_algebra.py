import numpy as np

# adjacency matrices, each array is a row, just like how you initialize it in Wolfram Alpha
test_matrices = [
    np.array([[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 1, 0]]), 
    np.array([[0, 1, 1, 0, 0],[1, 0, 1, 1, 0],[1, 1, 0, 1, 1],[0, 1, 1, 0, 1],[0, 0, 1, 1, 0]]),
    np.array([[0, 1, 1, 0, 0, 0],[1, 0, 1, 0, 0, 0],[1, 1, 0, 0, 0, 0],[0, 0, 0, 0, 1, 0],[0, 0, 0, 1, 0, 1],[0, 0, 0, 0, 1, 0]])
]

# these are the premade starting and finishing values for each adjacency matrix
# it's always the first and the last vertex we are testing
test_cases = [
    (0, 3, True),
    (0, 4, True),
    (0, 5, False)
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
def bfs_linear_algebra (adjacency_matrix: list, start: int, finish: int) -> bool:
    n, m = adjacency_matrix.shape

    # testing if our input is a square matrix
    if n != m:
        print ("Didn't recieve an n x n square adjacency matrix.")
        return 0

    # neighbors will be a vector representing the neighbors of a given vertex
    # and it will store the results of repeated matrix multiplication
    neighbors = np.zeros(n)
    neighbors[start] = 1

    # this defines a vectorized function for the ~ operation. It will flip each bit of an array
    invert = np.vectorize(lambda x: int(not x))

    for i in range(1, n):
        # This line does several steps at once
        # First, it extracts the neighbors using np.matmul() which is numpy's matrix multiplication function
        # Then, it converts the result to integers, otherwise, the & operation won't work
        # Then, it inverts the vector from the previous step and &'s it with the new vector, this removes all repeated vertices
        # from previous steps
        neighbors = np.matmul(adjacency_matrix, neighbors).astype(int) & invert(neighbors)

        if neighbors[finish]: # if this isn't a 0, the finishing vertex is connected to start
            return True
    return False

# This is a bit operator implementation of the same idea from bfs_linear_algebra
# Takes an array of integers each represented with n bits for an n x n adjacency matrix (each integer is a row)
# returns true
def bfs_bit_operations(A: np.array, s: int, f: int) -> bool:
    n = A.size
    
    # sets up starting and finishing indices
    # v keeps track of visited nodes
    # f is the integer with the fth bit made 1
    v = (1 << n - s - 1)
    f = (1 << n - f - 1)

    t = 0 # used to calculate the matrix multiplication
    for i in range(n):
        # calculates the matrix multiplication of A * v
        # for each row in A, it element-wise ands it with visited nodes
        # the element-wise and determines if there is a path between
        # visited nodes and the ith node
        # then if there is a path, it sets the ith bit of V to true
        for i in range(n):
            t |= ((A[i] & v) != 0) << (n - i - 1)
        
        # set result of multiplication to visited, reset the temporary variable
        v,t = t,0

        # if the bit at the fth position isn't 0 we reached the end
        if f & v != 0:
            return True
    return False
    
# runs each test case in a loop
def run_tests():
    # we need to convert each test case into an array of integers represented with n bits
    # lambda function based on https://stackoverflow.com/a/66189915, it just works
    decimal = lambda A, n: (A*2**np.arange(n-1,-1,-1,dtype='int64')).sum()
    A = []
    for test in test_matrices:
        A.append(np.array([decimal(arr, arr.size) for arr in test]))

    for i, test in enumerate(test_matrices):
        start, finish, solution = test_cases[i]
        print_matrix(test)
        print(f"Case {i + 1} (finding a path from {start} to {finish}):")
        print(f"\tbfs_linear_algebra: {bfs_linear_algebra(test, start, finish)} solution: {solution}")
        print(f"\tbfs_bit_operations: {bfs_bit_operations(A[i], start, finish)} solution: {solution}")
        print()

if __name__ == '__main__':
    run_tests()
