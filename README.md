# Breadth-First Search with Matrix Multiplication
An implementation of a rudimentary Breadth-First Search using Linear Algebra Methods. The script is based on [this paper](https://ieeexplore.ieee.org/document/7046157) and implements a modified, rudimentary, version using repeated matrix multiplication to determine if a path exists between two vertices, and the number of steps involved. Additional resources related to this topic include the book Graph Algorithms in the Language of Linear Algebra by Jeremy Kepner and John Gilbert. I uploaded this small script here as a part of an assignment for Linear Algebra 1 at OSU.

This method takes advantage of the fact that when you multiply an nxn matrix by a unit vector, the ith column of the vector is extracted and returned as the result of the operation. When applied to graphs, it means you can extract the neighbors of a vertex using matrix multiplication. Repeating matrix multiplication allows you to discover every vertex that is possible to reach from a source vertex since every vertex that is n steps away from a source vertex will be discovered after n multiplications of the unit vector. 

Bilbliography:

H. M. Bücker and C. Sohr, "Reformulating a Breadth-First Search Algorithm on an Undirected Graph in the Language of Linear Algebra," 2014 International Conference on Mathematics and Computers in Sciences and in Industry, 2014, pp. 33-35, doi: 10.1109/MCSI.2014.40.
