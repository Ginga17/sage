
print("Results on Sub K Tree with n=50, treewidth=3")
g = graphs.RandomSubKTree(50,3,5)
iterations = 5
g.treewidth()

r=timeit('g.vertex_cover(algorithm="Cliquer")', number=iterations)
print("Vertex cover from Cliquer algorithm: "+ str(r))

r=timeit('g.vertex_cover(algorithm="MILP")', number=iterations)
print("Vertex cover from MILP algorithm: "+ str(r))

T,rootNode = g.semi_nice_tree_decomposition()
r=timeit('g.vertex_cover_from_semi_ntd(T,rootNode)', number=iterations)
print("Vertex cover from semi-nice tree decomposition algorithm: "+ str(r))

T,rootNode = g.nice_tree_decomposition()
r=timeit('g.vertex_cover_from_ntd(T,rootNode)', number=iterations)
print("Vertex cover from nice tree decomposition algorithm: "+ str(r))




print("Results on Tree with n=100 treewidth=1")
g = graphs.RandomTree(100)
g.treewidth()

r=timeit('g.vertex_cover(algorithm="Cliquer")', number=iterations)
print("Vertex cover from Cliquer algorithm: "+ str(r))

r=timeit('g.vertex_cover(algorithm="MILP")', number=iterations)
print("Vertex cover from MILP algorithm: "+ str(r))

T,rootNode = g.semi_nice_tree_decomposition()
r=timeit('g.vertex_cover_from_semi_ntd(T,rootNode)', number=iterations)
print("Vertex cover from semi-nice tree decomposition algorithm: "+ str(r))


T,rootNode = g.nice_tree_decomposition()
r=timeit('g.vertex_cover_from_ntd(T,rootNode)', number=iterations)
print("Vertex cover from nice tree decomposition algorithm: "+ str(r))




print("Results on Tree with n=1000 treewidth=1")
g = graphs.RandomTree(100)
g.treewidth()

r=timeit('g.vertex_cover(algorithm="Cliquer")', number=iterations)
print("Vertex cover from Cliquer algorithm: "+ str(r))

r=timeit('g.vertex_cover(algorithm="MILP")', number=iterations)
print("Vertex cover from MILP algorithm: "+ str(r))

T,rootNode = g.semi_nice_tree_decomposition()
r=timeit('g.vertex_cover_from_semi_ntd(T,rootNode)', number=iterations)
print("Vertex cover from semi-nice tree decomposition algorithm: "+ str(r))


T,rootNode = g.nice_tree_decomposition()
r=timeit('g.vertex_cover_from_ntd(T,rootNode)', number=iterations)
print("Vertex cover from nice tree decomposition algorithm: "+ str(r))

#ran with: load('perfTest.sage')
