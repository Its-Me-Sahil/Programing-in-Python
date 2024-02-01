# Aim to implement BFS and Goal Search
tree ={'A':['B','C'],'B':['D'],'C':['E'],'D':['F'],'E':['F'],'F':[]}
start =input("Enter the start node")

def bfs_connected_components(tree):
    visited =[]
    queue = [start]
    while queue:
        node=queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbors= tree[node]
            for neighbor in neighbors:
                queue.append(neighbor)
    return visited
print("\n these are the node of the graph visited by BFS",bfs_connected_components(tree))
