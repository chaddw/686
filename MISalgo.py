import networkx as nx
import numpy as np
import time

def intersection(l1, l2):
    l3 = [value for value in l1 if value in l2]
    return l3

def calc_clique(neighbors, graph):
    print("normal")
    r = []
    p = list(neighbors.keys())
    x = []
    start_time = time.time()
    bron(r, p, x, neighbors)
    print("%s seconds" % (time.time() - start_time))

    print("pivot")
    r = []
    p = list(neighbors.keys())
    x = []
    start_time = time.time()
    bronpivot(r, p, x, neighbors)
    print("%s seconds" % (time.time() - start_time))


    print("ordering")
    r = []
    p = list(neighbors.keys())
    x = []
    start_time = time.time()
    bronorder(r, p, x, d, neighbors)
    print("%s seconds" % (time.time() - start_time))


def bron(r,p,x, neighbors):
    if len(p) == 0 and len(x) == 0:
        print(r)
        return
    for vertex in p[:]:
        r_new = r[::]
        r_new.append(vertex)
        p_new = intersection(p, neighbors[vertex]) # p intersects N(vertex)
        x_new = intersection(x, neighbors[vertex]) # x intersects N(vertex)
        bron(r_new,p_new,x_new, neighbors)
        p.remove(vertex)
        x.append(vertex)

def bronpivot(r,p,x, neighbors):
    if len(p) == 0 and len(x) == 0:
        print(r)
        return
    pivot = p.copy()
    pivot.extend(x)
    pivotList = [x for x in p if x not in neighbors[pivot[0]]]
    for vertex in pivotList:
        r_new = r[::]
        r_new.append(vertex)
        p_new = intersection(p, neighbors[vertex]) # p intersects N(vertex)
        x_new = intersection(x, neighbors[vertex]) # x intersects N(vertex)
        bronpivot(r_new,p_new,x_new, neighbors)
        p.remove(vertex)
        x.append(vertex)

def bronorder(r, p, x, d, neighbors):
    nodes = len(d)
    for i in range(nodes):
        vertex = min(d, key=d.get)
        del d[vertex]
        p_new = intersection(p, neighbors[vertex]) # p intersects N(vertex)
        x_new = intersection(x, neighbors[vertex]) # x intersects N(vertex)
        bronpivot([vertex], p_new, x_new, neighbors)
        p.remove(vertex)
        x.append(vertex)
      
# Driver code 
if __name__ == '__main__':
    
    n = 5
    val = input("how many nodes?: ")
    n = int(val)

    for i in range(4):
        d = {}
        neighbors = {}
        for j in range(n):
            d.update({j: 0})
            neighbors.update({j: []})

        if i == 0:
            G = nx.wheel_graph(n)
        #elif i == 1:
        #    G = nx.star_graph(n)
        elif i == 1:
            G = nx.complete_graph(n)
        elif i == 2:
            G = nx.complete_graph(n)
        else:
            G = nx.cycle_graph(n)

        npGraph = nx.adjacency_matrix(G).todense()
        graph = []
        for x in range(n):
            graph.append(list(np.array(npGraph[i]).reshape(-1,)))

        
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    d[i] += 1
                    if i != j:
                        neighbors[i].append(j)
                else:
                    graph[i][j] = 0
        
        calc_clique(neighbors, d)


