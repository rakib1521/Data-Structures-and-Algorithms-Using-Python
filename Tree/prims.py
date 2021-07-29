class Edge:
  def __init__(self,point_one,point_two,weight):
    self.point_one=point_one
    self.point_two=point_two
    self.weight=weight
def find_parent(node):
  if node==parent[node]:
    return node
  else:
    return find_parent(parent[node])
def update_parent(node_name,parent_name,parent):
  parent[node_name]=parent_name
  return parent
def insert_queue(current_node,objs,queue):
  for obj in objs:
    if (obj.point_one==current_node) and (obj not in queue):
        queue.append(obj)

  return queue


objs = list()
node=int(input("Enter Number of Node: "))
edges=int(input("Enter Number of Edges: "))

for i in range(edges):
    V,E,W = [int(x) for x in input("Enter Egde Source Destination Weight :  ").split()]
    objs.append(Edge(V,E,W))
    objs.append(Edge(E,V,W))



queue=list()
parent={}
for i in range(node):
    parent[i]=i
queue=insert_queue(0,objs,queue)
cost=0
print("{} {} {}".format("Source","Destination","Weight"))
while(len(queue)!=0):
  queue.sort(key=lambda x: x.weight, reverse=False)
  current_node=queue.pop(0)
  if find_parent(current_node.point_one)!=find_parent(current_node.point_two):
    print("{}\t {}\t    {}\t".format(current_node.point_one,current_node.point_two,current_node.weight))
    cost=cost+current_node.weight
    parent=update_parent(current_node.point_two,current_node.point_one,parent)
    current_node=current_node.point_two
    queue=insert_queue(current_node,objs,queue)


print("cost {}".format(cost))

for key,value in parent.items():
    print("node : {} and it's parent {}".format(key,value))
