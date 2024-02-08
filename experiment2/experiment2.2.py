# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
graph ={'A':['B','C'],'B':['D','E'],'C':['F','G'],'D':[],'E':[],'F':[],'G':[]}
visited =[]
start =input("Enter the start node")
goal =input("Enter the goal node")
def DFS(graph,start):
    if start not in visited:
        print(start)
        visited.append(start)
        neighbour = graph[start]
        for i in neighbour:
            if goal in visited:
                break
            else:
                DFS(graph,i)
DFS(graph,start)