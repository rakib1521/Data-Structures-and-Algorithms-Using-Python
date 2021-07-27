
def dfsvisit(current_node,visited,edges_list):
    visited[current_node]=True
    print(current_node,end=" ")
    for i in edges_list[current_node]:
        if visited[i]==False:
            dfsvisit(i,visited,edges_list)



def dfs(node,edges_list):
    visited=[]
    for i in range(node):
        visited.append(False)
    for i in range(node):
        if visited[i]==False:
            dfsvisit(i,visited,edges_list)


def bfs(node,edges_list,start):
    visited=[]
    for i in range(node):
        visited.append(False)
    queue = []
    visited[start]=True
    queue.append(start)
    while(queue!=[]):
        current_node=queue.pop(0)
        print(current_node,end=" ")
        for i in edges_list[current_node]:
            if visited[i]==False:
                visited[i]=True
                queue.append(i)

def addedge(node,edge):
    edges_list=[]
    for i in range(node):
        edges_list.append([])
    for i in range(edge):
        V,E = [int(x) for x in input("Enter Egde: ").split()]
        edges_list[V].append(E)
        edges_list[E].append(V)

    return edges_list

node=int(input("Enter Number of Node: "))
edge=int(input("Enter Number of Edge: "))
edges_list=[]
edges_list=addedge(node,edge)
start=int(input("Enter Number of start node: "))
print("BFS")
bfs(node,edges_list,start)
print()
print("DFS")
dfs(node,edges_list)
