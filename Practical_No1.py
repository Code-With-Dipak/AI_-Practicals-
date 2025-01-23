#Breadth First Search(BFS)
graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}
visited=[]
queue=[]
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        s=queue.pop(0)
        print(s,end="")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                # Driver Code
bfs(visited,graph,'A')

******OUTPUT****:-ABCDEF


#Depth-First Search 
graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}
visited=set()

def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour) 
        
#Driver Code
print("Following is the path using Depth-Firstt Search")
dfs(visited,graph,'A')

*******OUTPUT*****:-
Following is the path using Depth-Firstt Search
A
B
D
E
F
C














