graph = {'A':['B','C'],'B':['D','E'],'C':['F','G'],'D':[],'E':[],'F':[],'G':[]}

start = input("enter the start node \n ")
goal = input("enter the goal node \n ")

def dfs_shortest_path(graph):
    visited = []
    stack=[[start]]
    while stack:
        path = stack.pop()
        node=path[-1]
        if node not in visited:
            visited.append(node)
            neighbor=graph[node]
            for i in neighbor:
                new_path=list(path)
                new_path.append(i)
                stack.append(new_path)
                if i==goal:
                    return new_path
print("path is :",dfs_shortest_path(graph))