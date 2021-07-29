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


objs = list()
node=int(input("Enter Number of Node "))
edges=int(input("Enter Number of Edges "))

for i in range(edges):
    V,E,W = [int(x) for x in input("Enter Egde Source Destination Weight :  ").split()]
    objs.append(Edge(V,E,W))

objs.sort(key=lambda x: x.weight, reverse=False)

parent={}
for i in range(node):
    parent[i]=i

cost=0
Edge_count=0
print("{} {} {}".format("Source","Destination","Weight"))

for obj in objs:
  if find_parent(obj.point_one)!=find_parent(obj.point_two):
        parent=update_parent(obj.point_two,obj.point_one,parent)
        cost=cost+obj.weight
        print("{} {} {}".format(obj.point_one,obj.point_two,obj.weight))
        Edge_count=Edge_count+1
  if Edge_count==node-1:
      break

print("Total Cost {}".format(cost))
for key,value in parent.items():
    print("node : {} and it's parent {}".format(key,value))
