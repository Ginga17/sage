import os
import csv
import timeit
import tracemalloc


# These tests were written quickly and aren't super readable
# The bottom of the file features the function calls to run the tests, wherein files will be opened and saved


# Tests the peak memory used by each MVC algorithm
def testMemory(g):
    
    tracemalloc.start()
    sntd,sntdRoot = g.semi_nice_tree_decomposition()
    tracemalloc.stop()

    tracemalloc.start()
    ntd,ntdRoot = g.nice_tree_decomposition()
    tracemalloc.stop()


    tracemalloc.start()
    g.vertex_cover_from_semi_ntd(sntd,sntdRoot)
    sntdMem= tracemalloc.get_traced_memory()[1]
    # print("Vertex cover from semi-nice tree decomposition algorithm: "+ str(tracemalloc.get_traced_memory()))
    # stopping the library
    tracemalloc.stop()


    tracemalloc.start()
    # function call
    # displaying the memory
    g.vertex_cover_from_ntd(ntd,ntdRoot)

    ntdMem= tracemalloc.get_traced_memory()[1]
    # print("Vertex cover from nice tree decomposition algorithm: "+ str(tracemalloc.get_traced_memory()))
    # stopping the library
    tracemalloc.stop()


    tracemalloc.start()
    # function call
    # displaying the memory
    g.vertex_cover(algorithm="Cliquer")
    
    cliquerMem= tracemalloc.get_traced_memory()[1]
    # print("Vertex cover from Cliquer algorithm: "+ str(tracemalloc.get_traced_memory()))
    # stopping the library
    tracemalloc.stop()


    tracemalloc.start()
    # function call
    # displaying the memory
    g.vertex_cover(algorithm="MILP")

    milpMem= tracemalloc.get_traced_memory()[1]
    # print("Vertex cover from MILP algorithm: "+ str(tracemalloc.get_traced_memory()))
    # stopping the library
    tracemalloc.stop()

    return [sntdMem,ntdMem,milpMem,cliquerMem]


# Written to paramaterise on k tree, with edges being a set value
def testNTDalgoOnKTreesSetEdges(n,seed=2,iterations=5, max=6, edges=180):

    
    data = []
    data.append(["k", "edges","vertex_cover_cliquer","vertex_cover_milp","vertex_cover_sntd","vertex_cover_ntd"])

    for k in range(2,max):
        print("treewidth: " + str(k))

        # Calculate how many edges will be in the complete K Tree
        edgesInKTree = (k ^ 2 + k) / 2 + (n - k - 1) * k

        g= graphs.RandomPartialKTree(n,k,int(edgesInKTree-edges),seed)
        
        T1, rootNode1 = g.semi_nice_tree_decomposition()
        T2, rootNode2 = g.nice_tree_decomposition()

        times = []
        times.append(k)

        times.append(g.size())
    

        def vertex_cover_cliquer():
            return g.vertex_cover(algorithm="Cliquer")
        def vertex_cover_milp():
            return g.vertex_cover(algorithm="MILP")
        def vertex_cover_sntd():
            return g.vertex_cover_from_semi_ntd(T1,rootNode=rootNode1)
        def vertex_cover_ntd():
            return g.vertex_cover_from_ntd(T2,rootNode=rootNode2)
        algos = [vertex_cover_cliquer,vertex_cover_milp,vertex_cover_sntd,vertex_cover_ntd]
        for algo in algos:

            t = timeit.timeit(algo, number=iterations)
            times.append(t)
        data.append(times)

    return data



# Tests the memory used by SNTD and NTD MVC algorithms, tests on random partial k trees
#  which are generated as k trees, with delEdgesRatio % of its edges deleted
def testMemoryOnKTreeDelEdges(n,seed=2, max=6, delEdgesRatio=0.2):

    data = []
    data.append(["k", "vertex_cover_sntd","vertex_cover_ntd"])

    for k in range(2,max):
        # Calculate how many edges will be in the complete K Tree
        edgesInKTree = (k ^ 2 + k) / 2 + (n - k - 1) * k

        deleteNum = int(edgesInKTree * delEdgesRatio)
        
        g= graphs.RandomPartialKTree(n,k,deleteNum,seed)
        times = []
        times.append(k)

        sntd,sntdRoot = g.semi_nice_tree_decomposition()
        ntd,ntdRoot = g.nice_tree_decomposition()

        tracemalloc.start()
        g.vertex_cover_from_semi_ntd(sntd,sntdRoot)
        times.append(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()

        tracemalloc.start()
        g.vertex_cover_from_ntd(ntd,ntdRoot)
        times.append(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()

        data.append(times)
        print(data)

    return data



def testMemoryOnKTreePercentageOfEdgesDeleted(n,seed=2, max=6, edgePercentageToDelete=0.2):

    data = []
    data.append(["k", "vertex_cover_sntd","vertex_cover_ntd"])

    for k in range(2,max):
        print("treewidth: " + str(k))

        # Calculate how many edges will be in the complete K Tree
        edgesInKTree = (k ^ 2 + k) / 2 + (n - k - 1) * k

        deleteNum = int(edgesInKTree * edgePercentageToDelete)
        
        g= graphs.RandomPartialKTree(n,k,deleteNum,seed)
        times = []
        times.append(k)

        tracemalloc.start()
        
        sntd,sntdRoot = g.semi_nice_tree_decomposition()


        g.vertex_cover_from_semi_ntd(sntd,sntdRoot)
        times.append(tracemalloc.get_traced_memory()[1])
        # print("Vertex cover from semi-nice tree decomposition algorithm: "+ str(tracemalloc.get_traced_memory()))
        # stopping the library
        tracemalloc.stop()


        data.append(times)
        print(data)

    return data

def runTestTimeSetEdges(nodes=1000, initialSeed=0, iterations=100, edges=200, max=6,subdirectory="setEdgesTime"):
    for seed in range (initialSeed,initialSeed+iterations,):
        print("seed is: " +str(seed))

        outputFilename = f"TimeTestEdges={edges}Nodes={nodes}Seed={seed}.csv"
        
        if not os.path.exists(subdirectory):
            os.makedirs(subdirectory)

        file_path = os.path.join(subdirectory, outputFilename)

        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)

            results = testNTDalgoOnKTreesSetEdges(nodes,seed=seed,iterations=3, max=max, edges=edges)
            writer.writerows(results)





# Written to test runtime of MVC algorithms on partial k trees for different values of k 
#  This algorithm generates k trees, and then removes a passed percentage of its edges, removes a pecentage of edges
def testTimeOnNTDalgoOnKTreesPercentageEdgesDeleted(n,seed=2,iterations=5, max=6, edgesToDelete=0.2):

    
    data = []
    # data.append(["k", "edges", "vertex_cover_cliquer","vertex_cover_milp","vertex_cover_sntd","vertex_cover_ntd"])
    data.append(["k", "vertex_cover_sntd","vertex_cover_ntd","vertex_cover_cliquer","vertex_cover_milp"])

    for k in range(2,max):

        # Calculate how many edges will be in the complete K Tree
        edgesInKTree = (k ^ 2 + k) / 2 + (n - k - 1) * k
        deleteNum = int(edgesInKTree * edgesToDelete)
                
        g= graphs.RandomPartialKTree(n,k,deleteNum,seed)

        T1, rootNode1 = g.semi_nice_tree_decomposition()
        T2, rootNode2 = g.nice_tree_decomposition()
        times = []
        times.append(k)    

        def vertex_cover_cliquer():
            return g.vertex_cover(algorithm="Cliquer")
        def vertex_cover_milp():
            return g.vertex_cover(algorithm="MILP")
        def vertex_cover_sntd():
            return g.vertex_cover_from_semi_ntd(T1,rootNode=rootNode1)
        def vertex_cover_ntd():
            return g.vertex_cover_from_ntd(T2,rootNode=rootNode2)
        algos = [vertex_cover_sntd,vertex_cover_ntd, vertex_cover_cliquer,vertex_cover_milp]
        for algo in algos:
            print(algo)
            t = timeit.timeit(algo, number=iterations)
            times.append(t)
        data.append(times)

    return data

# tests the 4 algorithms on k trees of varied k, and set edges
def testTimePartialKTreeSetEdges(outputFilename, edges,seed=1,nodes=100,max=6,subdirectory = "outputDir"):

    if not os.path.exists(subdirectory):
        os.makedirs(subdirectory)

    file_path = os.path.join(subdirectory, outputFilename)

    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)

        results = testTimeOnNTDalgoOnKTreesPercentageEdgesDeleted(nodes,seed=seed,iterations=3, max=max, edges=edges)
        writer.writerows(results)



# Quick test to see the difference in time taken for partial k trees with more vs less edges
def testTimeVaryEdgePercentageDeleted():
    nodes = 100
    seed=1
    edges=0.1
    testTimePartialKTreeSetEdges(f"TimeTestEdges={edges}Nodes={nodes}Seed={seed}.csv", edges=edges, nodes=nodes,max=6,seed=seed, subdirectory="varyEdges")
    edges=0.2
    testTimePartialKTreeSetEdges(f"TimeTestEdges={edges}Nodes={nodes}Seed={seed}.csv", edges=edges, nodes=nodes,max=6,seed=seed, subdirectory="varyEdges")
    edges=0.3
    testTimePartialKTreeSetEdges(f"TimeTestEdges={edges}Nodes={nodes}Seed={seed}.csv", edges=edges, nodes=nodes,max=6,seed=seed, subdirectory="varyEdges")
    

def runTestTimeVaryEdgePercentageDeleted(initialSeed=0,iterations=100):
    for seed in range (initialSeed,initialSeed+iterations):
        print("seed is: " +str(seed))
        testTimeVaryEdgePercentageDeleted()



# Written to paramaterise on k tree, with edges being a set value
def testNTDalgoOnKTreesForMemory(n,seed=5,iterations=5, max=6, edges=180):

    
    data = []
    data.append(["k", "edges","vertex_cover_cliquer","vertex_cover_milp","vertex_cover_sntd","vertex_cover_ntd"])

    for k in range(2,6):
        print("treewidth: " + str(k))

        # Calculate how many edges will be in the complete K Tree
        edgesInKTree = (k ^ 2 + k) / 2 + (n - k - 1) * k

        # print(edgesInKTree)
        # print(edgesInKTree-edges)

        g= graphs.RandomPartialKTree(n,k,int(edgesInKTree-edges),seed)
        print("edges in tree:")
        print(g.size())
        T1, rootNode1 = g.semi_nice_tree_decomposition()
        T2, rootNode2 = g.nice_tree_decomposition() 

        tracemalloc.start()
        g.vertex_cover_from_semi_ntd(T1,rootNode1)
        sntdMem= tracemalloc.get_traced_memory()[1]
        # print("Vertex cover from semi-nice tree decomposition algorithm: "+ str(tracemalloc.get_traced_memory()))
        # stopping the library
        tracemalloc.stop()


        tracemalloc.start()
        # function call
        # displaying the memory
        g.vertex_cover_from_ntd(T2,rootNode2)

        ntdMem= tracemalloc.get_traced_memory()[1]
        # print("Vertex cover from nice tree decomposition algorithm: "+ str(tracemalloc.get_traced_memory()))
        # stopping the library
        tracemalloc.stop()


        tracemalloc.start()
        # function call
        # displaying the memory
        g.vertex_cover(algorithm="Cliquer")
        
        cliquerMem= tracemalloc.get_traced_memory()[1]
        # print("Vertex cover from Cliquer algorithm: "+ str(tracemalloc.get_traced_memory()))
        # stopping the library
        tracemalloc.stop()


        tracemalloc.start()
        # function call
        # displaying the memory
        g.vertex_cover(algorithm="MILP")

        milpMem= tracemalloc.get_traced_memory()[1]
        # print("Vertex cover from MILP algorithm: "+ str(tracemalloc.get_traced_memory()))
        # stopping the library
        tracemalloc.stop()

        data.append([k,g.size(),sntdMem,ntdMem,milpMem,cliquerMem])
        print(data)

    return data


def testMemoryPartialKTree(outputFilename):
    with open(outputFilename, mode='w', newline='') as file:
        writer = csv.writer(file)

        results = testNTDalgoOnKTreesForMemory(100,seed=10)
        writer.writerows(results)

# Used to generate test data comparing the number of nodes in a SNTD and NTD generated from the same graph
def testOrderOfSNTDAndNTD(n,seed=2, max=6, deleteEdgesRatio=0.2):

    data = []
    data.append(["k", "vertex_cover_sntd_size","vertex_cover_sntd_size","vertex_cover_ntd"])

    for k in range(2,max):
        print("treewidth: " + str(k))

        # Calculate how many edges will be in the complete K Tree
        edgesInKTree = (k ^ 2 + k) / 2 + (n - k - 1) * k

        # Deletes a percentage of the edges in the tree
        deleteNum = int(edgesInKTree * deleteEdgesRatio)
        
        g= graphs.RandomPartialKTree(n,k,deleteNum,seed)
        
        new = []
        new.append(k)
        
        # Generate the tree decompositions
        ntd,ntdRoot = g.nice_tree_decomposition()
        sntd,sntdRoot = g.semi_nice_tree_decomposition()

        
        new.append(sntd.order())

        new.append(ntd.order())

        data.append(new)

    return data



# Generates the file, by running compareNTDandSNTD on different seeds
# subdirectory to store output csv data in, n is the number of iterations run, how many nodes to run it on
def generateDataForCompareNTDandSNTD(subdirectory = "nodesOrderEdges",n=100,nodes=1000,initialSeed=0,deleteEdgesRatio=0.2):
    
    for seed in range (initialSeed,initialSeed+n):
        if not os.path.exists(subdirectory):
            os.makedirs(subdirectory)

        file_path = os.path.join(subdirectory, f"{deleteEdgesRatio}Nodes={nodes}Seed={seed}.csv")

        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)

            results = testOrderOfSNTDAndNTD(nodes,seed,iterations=5, max=6, edges=deleteEdgesRatio)
            writer.writerows(results)
        print("seed is: " +str(seed))



# Test number of nodes
generateDataForCompareNTDandSNTD()

# Time tests
runTestTimeSetEdges()
runTestTimeVaryEdgePercentageDeleted()

# Memory Test
testMemoryPartialKTree()