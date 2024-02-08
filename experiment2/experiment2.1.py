#to implement depth first search
graph = {'A':['B','C'],'B':['D','E'],'C':['F','G'],'D':[],'E':[],'F':[],'G':[]}

start = input("enter the start node \n ")
def dfs_components(graph):
    visited=[]
    stack=[start]
    while stack:
        node=stack.pop()
        if node not in visited:
            visited.append(node)
            neighbours=graph[node]
            for neighbour in neighbours:
                stack.append (neighbour)
    return visited
print("Traversal  by depth first search:\n",dfs_components(graph))