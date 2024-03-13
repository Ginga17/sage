import os
import csv

import tracemalloc


def testMemory(g,iterations):
    
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


import timeit


def testTime(g,iterations):

    T1, rootNode1 = g.semi_nice_tree_decomposition()
    T2, rootNode2 = g.nice_tree_decomposition()

    def vertex_cover_cliquer():
        return g.vertex_cover(algorithm="Cliquer")
    def vertex_cover_milp():
        return g.vertex_cover(algorithm="MILP")
    def vertex_cover_sntd():
        return g.vertex_cover_from_semi_ntd(T1,rootNode=rootNode1)
    def vertex_cover_ntd():
        return g.vertex_cover_from_ntd(T2,rootNode=rootNode2)
        
    cliquerTime = timeit.timeit(vertex_cover_cliquer, number=iterations)

    milpTime = timeit.timeit(vertex_cover_milp, number=iterations)

    sntdTime = timeit.timeit(vertex_cover_sntd, number=iterations)

    ntdTime = timeit.timeit(vertex_cover_ntd, number=iterations)

    return [sntdTime,ntdTime,milpTime,cliquerTime]



def buildGraph(filename):
    # Read data from file
    with open(filename, 'r') as file:
        #skip header
        #header looks like `p tw {degree} {edges}`
        header = file.readline()
        
        data = file.readlines()

    # Create a graph
    G = Graph()

    # Add vertices and edges to the graph
    for line in data:
        if line.strip():  # Ignore empty lines
            vertices = line.strip().split()
            vertex1 = int(vertices[0])
            vertex2 = int(vertices[1])
            G.add_edge(vertex1, vertex2)

    # Plot the graph
    # G.show()
    return G


def loopThroughFiles(path, tw):
    # Loop through files in the directory
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)):
            print(filename)
            buildGraph



def testInstancesMemory(filename, outputFilename, maxtw):
    with open(filename, 'r') as file:
        # skip header
        file.readline()

        data = file.readlines()


    with open(outputFilename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["graph", "treewidth", "semi-ntd", "ntd", "MILP", "Cliquer"])


        
        for line in data:
            params = line.split(';')
            filename = params[0]
            tw = int(params[1])
            if (tw <=maxtw):
                print(filename)
                print(tw)

                g = buildGraph('graphs/100/'+filename)
                x=g.treewidth()
                print(x)
                res = testMemory(g,5)


                writer = csv.writer(file)
                writer.writerow([filename[:-3], tw]+ res)

                # return



def testInstancesTime(filename, outputFilename, maxtw):
    with open(filename, 'r') as file:
        # skip header
        file.readline()

        data = file.readlines()


    with open(outputFilename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["graph", "treewidth", "semi-ntd", "ntd", "MILP", "Cliquer"])


        
        for line in data:
            params = line.split(';')
            filename = params[0]
            tw = int(params[1])
            if (tw <=maxtw+1):
                print(filename)
                print(tw)

                g = buildGraph('graphs/100/'+filename)
                x=g.treewidth()
                print(x)
                res = testMemory(g,5)


                writer = csv.writer(file)
                writer.writerow([filename[:-3], tw+1]+ res)

                # return


def testNTDalgoOnKTrees(n,x,seed=1,iterations=5, max=8):

    
    data = []
    data.append(["k", "edges","vertex_cover_cliquer","vertex_cover_milp","vertex_cover_sntd","vertex_cover_ntd"])

    for k in range(2,max):
        print("treewidth: " + str(k))
        g= graphs.RandomPartialKTree(n,k,x,seed)
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


# Written to paramaterise on k tree, with edges being a set value
def testNTDalgoOnKTrees2(n,seed=1,iterations=5, max=6, edges=180):

    
    data = []
    data.append(["k", "edges","vertex_cover_cliquer","vertex_cover_milp","vertex_cover_sntd","vertex_cover_ntd"])

    for k in range(2,max):
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

# tests the 4 algorithms on k trees of varied k, and set edges
def testTimePartialKTreeSetEdges(outputFilename):
    with open(outputFilename, mode='w', newline='') as file:
        writer = csv.writer(file)

        results = testNTDalgoOnKTrees2(100)
        writer.writerows(results)

testTimePartialKTreeSetEdges("kTreesSetEdges.csv")

# tests the 4 algorithms on k
#  trees of various time lengths
def testTimePartialKTree(outputFilename):
    with open(outputFilename, mode='w', newline='') as file:
        writer = csv.writer(file)

        results = testNTDalgoOnKTrees(120,20,seed=1)
        writer.writerows(results)

# testTimePartialKTree("kTreeOut.csv")

def testInstancesTime(filename, outputFilename, maxtw):
    with open(filename, 'r') as file:
        # skip header
        file.readline()

        data = file.readlines()


    with open(outputFilename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["graph", "treewidth", "semi-ntd", "ntd", "MILP", "Cliquer"])


        
        for line in data:
            params = line.split(';')
            filename = params[0]
            tw = int(params[1])
            if (tw <=maxtw+1):
                print(filename)
                print(tw)

                g = buildGraph('graphs/100/'+filename)
                x=g.treewidth()
                print(x)
                # It looks like the graphs from Pace give bag size, not bag size -1 


                res = testTime(g,5)


                writer = csv.writer(file)
                writer.writerow([filename[:-3], tw+1]+ res)



                

# testInstancesMemory('graphs/instances.csv', "memoryInstances.csv", 4)
# testInstancesTime('graphs/instances.csv', "time.csv", 4)
# loopThroughFiles('graphs/100', 5)
# g=buildGraph("graphs/100/AhrensSzekeresGeneralizedQuadrangleGraph_3.gr")


# 5,3,2,1