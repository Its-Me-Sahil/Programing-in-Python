# Aim to implement  Goal Search
tree ={'A':['B','C'],'B':['D'],'C':['E'],'D':['F'],'E':['F'],'F':[]}
start =input("Enter the start node")
goal =input("Enter the goal node")

def bfs_connected_components(tree):
    visited =[]
    queue = [start]
    visited.append(start)
    if start==goal:
        print("your start node is goal node")
        return visited
    else:
      
      while queue:
         node=queue.pop(0)
         for neighbor in tree[node]:
            if neighbor not in visited:
               visited.append(neighbor)
               queue.append(neighbor)
            if neighbor==goal:
               return visited
      return "so sorry but a connecting path doesn't exist" 
        
    
print("\n BFS",bfs_connected_components(tree))
