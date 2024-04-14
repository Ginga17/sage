

# Damian Basso's Thesis: Software for Computing Graph Parameters


## Synopsis

This repository is for my thesis completed to fulfill the honours portion of my Software Engineering (Honours) Bachelor's degree at UNSW.

The thesis is focused on graph theory, and graph parameters. In particular, treewidth and tree decomposition are explored for their usefulness in computing minimum vertex covers for graphs. Additionally, as part of this thesis the idea of 'Semi-Nice Tree Decompositions', an adjustment to the 'Nice Tree Decomposition' with performance benefits.

The software implementations for this project were designed with, and for the SageMath library. SageMath is a fantastic open-source mathematics software system that integrates numerous mathematics software packages. SageMath is maintained by a diverse community of developers and contributors from around the world. 

- [Read more about SageMath](https://www.sagemath.org)
- [SageMath's main GitHub repository](https://github.com/sagemath/sage)
- [SageMath's official documentation](https://doc.sagemath.org/html/en/index.html)

## Directory

Here are the directions to each of my pieces of code in this repository. 

### Nice Tree Decomposition and Semi-Nice Tree Decomposition Generators

The functions `nice_tree_decomposition` and `semi_nice_tree_decomposition` can be found in the following file: `src/sage/graphs/graph_decompositions/tree_decomposition.pyx`

These functions are responsible for generating nice tree decompositions and semi-nice tree decompositions of graphs. They take a graph as input and give back their respective data structure and a root node for it.

### Minimum Vertex Cover Algorithms

The functions `vertex_cover_from_ntd` and `vertex_cover_from_semi_ntd` can be found in the following file: `src/sage/graphs/graph.py`.

These functions are designed to determine a minimum vertex cover for a given graph. They take either a nice tree decomposition or semi-nice tree decomposition along with the graph as input and return a set of vertices that forms a minimum vertex cover for the graph.

### Random K-Tree and Partial K-Tree Generation

The functions `RandomKTree` and `RandomPartialKTree` can be found in the following file: `src/sage/graphs/generators/random.py`.

These functions are designed to generate random k trees and partial k trees. 

### Random K-Tree and Partial K-Tree Generation

The functions `RandomKTree` and `RandomPartialKTree` can be found in the following file: `src/sage/graphs/generators/random.py`.

### Testing

The functions `tests.py` and `combineData.py` can be found in the `/test` folder.

In `tests.py` are the tests written for my functions. In `combineData.py` are helpers functions I used to put colate the data into my desired csv format.


## Pull Request

[Here is the link to my accepted Pull Request into SageMath. ](https://github.com/sagemath/sage/pull/36587)

The PR adds functionality for random k-tree and partial k-tree generation
## Thesis Document

`Insert link to thesis here`

## Testing results

`Add the excel doc to repoo`



## Presentation
`Add the 3 completed powerpoints to the repo`
