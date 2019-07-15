# Graph

## Overview
A graph is a set of vertices and edges that form connections betweens the vertices

## Keywords

* Node or Vertex : A point, usually represented by a dot in a graph.
* Edge : A connection between two verices(a line connecting two nodes).
* Loop : When an edge from a node is connected to itself. 
* Degree of a vertex : The number of vertices that are connected to to a certain node.
* Adjency : When two nodes are neighbor. Or when two nodes are connected directly(without an interim node in between).
* Path : A sequence of vertices where each adjacent pair is connected by an edge.
* Walk : A sequence of distinct connected edges.
    -- * Open walk : origin is different from destination.
    -- * Closed walk : origin is same as destination.
    
* Trail : A walk with distinct edges.
* Path : An opened trail with no repeated verices.
* Cycle : A closed trail where no other vertices are repeated apart from the start/end vertex

## Types of Graphs

* Graph
* Digraph
* Wighted Digraph


#### Undirected graphs

Those simply represent edges as lines between nodes. No additional information about the relationship about the nodes besides that they are connected.
![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Undirected_graph.svg/1280px-Undirected_graph.svg.png)

#### Directed graphs

In a directed graph, the edges provide orientation(shows direction with an arrow) in addition to connecting nodes.
![alt text](https://computersciencewiki.org/images/c/c6/Directed_graph.png)

#### Weighted graphs

A weighted graph provides an extra information for the edges. This can be a numerical value that represents a certain value.
![alt text](https://i1.wp.com/algorithms.tutorialhorizon.com/files/2018/03/Weighted-Graph.png?ssl=1) 

In the example above, each number on the edge may represent the amount of time it takes to go from a vertex to another.

## Graph Representation

Graphs can be represented in two ways:
* Adjacency List
* Adjacency Matrix

#### Adjacency List

In this representation, a graph is represented as a list where the index represent the vertex and its value(s) are its adjacent verteces.

![alt text](https://www.sanfoundry.com/wp-content/uploads/2017/08/data-structure-questions-answers-directed-graph-q8.png) 

In this example, index O represents vertex A, 1 represents vertex B, and so on. we can use the adjacency list representation as follow:
* [0] -> [B,D]
* [1] -> [C]
* [3] -> []
* [4] -> [E]
* [5] -> []


#### Adjacency Matrix
In this representation, we use a 2d array where cells with value 1 means that there is a connection in (i,j) and cells with value 0 means that there aren't any connection.

