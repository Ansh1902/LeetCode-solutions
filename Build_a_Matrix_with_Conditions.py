# Graph Construction:

# Construct a graph for row conditions and another graph for column conditions.
# Nodes represent the numbers from 1 to k.
# Directed edges represent the conditions, e.g., rowConditions[i] = [a, b] implies an edge from a to b.
# Topological Sorting:

# Perform topological sorting on both graphs to determine the order of rows and columns.
# Use Depth First Search (DFS) for topological sorting and detect any cycles which would make it impossible to satisfy the conditions.
# Matrix Construction:

# Using the order obtained from the topological sort, place each number from 1 to k in the corresponding position in the k x k matrix.
# Validation:

# If any cycle is detected during the topological sorting, return an empty matrix as it indicates that it is impossible to satisfy all conditions.

class Solution(object):
    def buildMatrix(self, k, rowConditions, colConditions):
        """
        :type k: int
        :type rowConditions: List[List[int]]
        :type colConditions: List[List[int]]
        :rtype: List[List[int]]
        """
        rowGraph = defaultdict(list)
        for u,v in rowConditions:
            rowGraph[u].append(v)
        
        colGraph = defaultdict(list)
        for u,v in colConditions:
            colGraph[u].append(v)
        
        def topoSort(graph):
            inDegree = {i:0 for i in  range(1,k+1)}
            for u in graph:
                for v in graph[u]:
                    inDegree[v]+=1
            queue = deque([i for i in inDegree if inDegree[i]==0])
            order=[]
            while queue:
                node = queue.popleft()
                order.append(node)
                for v in graph[node]:
                    inDegree[v]-=1
                    if inDegree[v]==0:
                        queue.append(v)
            return order if len(order)==k else []
        rowOrder = topoSort(rowGraph)
        colOrder = topoSort(colGraph)
        if not rowOrder or not colOrder:
            return []
        rowMap = {num:i for i,num in enumerate(rowOrder)}
        colMap = {num:i for i,num in enumerate(colOrder)}
        result = [[0]*k for _ in range(k)]
        for i in range(1,k+1):
            result[rowMap[i]][colMap[i]]=i
        return result
