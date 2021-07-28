class Edge:
  def __init__(self,point_one,point_two,weight):
    self.point_one=point_one
    self.point_two=point_two
    self.weight=weight

def min_index(weight):
  ind=999
  for i in range(len(weight)):
    if weight[i]!=0 and weight[i]<ind:
      ind=weight[i]
  return weight.index(ind)
objs = list()
node=int(input("Enter Number of Node: "))
edges=int(input("Enter Number of Edges: "))
for i in range(edges):
    V,E,W = [int(x) for x in input("Enter Egde Source Destination Weight :  ").split()]
    objs.append(Edge(V,E,W))

weight=[]
path=[]
parent={}
cost=0
for i in range(0,node):
    weight.append(99999)

s=0
path.append(s)
parent[s]=s
weight[s]=0
for i in range(node):
  for j in range(0,len(objs)):
    if objs[j].point_one==s:
      if weight[objs[j].point_two]>objs[j].weight:
          weight[objs[j].point_two]=objs[j].weight

  weight[s]=0
  temp_parent=s
  if i<node-1:
      s= min_index(weight)
      path.append(s)
      parent[s]=temp_parent

  cost=cost+weight[s]
print("Path",end=" ")  
for i in path:
    print(i, end =" ")

print()
print("cost {}".format(cost))

for key,value in parent.items():
    print("node : {} and it's parent {}".format(key,value))
