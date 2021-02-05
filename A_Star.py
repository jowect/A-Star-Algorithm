import math
import sys

def shortest_path(M,start,goal):     # A* algorithm
    
    result = dict()    # closed dict where only the final results are stored (pure distance without heuristic values) 
    path = dict()      # !! open dict, where the f values (our 'Score') are stored 
                       # f = g + h; g=result(preNode), h=eucDist(neighbour,goal)
                       # each time a better path has been found the Score gets updated
    preNode = dict()   # open dict, where the preNodes are stored step by step, these change during processing
    result[start] = 0
    
    def eucDist(a,b):  # helper for finding the distance between two points
        d = math.sqrt(
            ((M.intersections[a][0] - M.intersections[b][0])**2) + 
            ((M.intersections[a][1] - M.intersections[b][1])**2)
        )
        
        return d
    
    for i in M.intersections:
        path[i] = sys.maxsize
        preNode[i] = ''

    path.pop(start)
    minNode = start
    preNode[minNode] = start
    
    while(minNode != goal):

        for neighbour in M.roads[minNode]:
            if neighbour in path:

                pathScore_New = (result[minNode]
                                 + eucDist(minNode, neighbour)
                                 + eucDist(neighbour, goal))
                pathScore_Yet = path[neighbour]

                if pathScore_New < pathScore_Yet:
                    path[neighbour] = pathScore_New
                    preNode[neighbour] = minNode

        minNode = min(path, key=path.get)    # define new minNode from the path dict
        result[minNode] = (result[preNode[minNode]] 
                           + eucDist(preNode[minNode], minNode))       
        path.pop(minNode)

    output = list()
    x = goal
    output.append(x)
    while(x!=start):
        output.append(preNode[x])
        x = preNode[x]
        
    print(result)
    return output[::-1]

