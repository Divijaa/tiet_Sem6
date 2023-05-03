from sys import maxsize
from itertools import permutations
v=4
def travelling(graph,s):
	vertex=[]
	for i in range(v):
		vertex.append(i)
		min_size=maxsize 
	per=permutations(vertex)
	
	for i in per:
		min_weight=0
		k=s
		for j in i:
			min_weight=min_weight+graph[k][j]
			k=j
		min_weight=min_weight+graph[k][s]
		min_size=min(min_size,min_weight)
	return min_size

graph=[[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
s=int(input("enter the source point"))
print(travelling(graph,s))