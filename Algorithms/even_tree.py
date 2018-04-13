from collections import defaultdict

edges = []
cnt = 0

config =  raw_input().split(' ')

for j in range(int(config[1])):
	i = raw_input().split(' ')
	edges.append((i[0],i[1]))

#edges = [(2,1),(3,1),(4,3),(5,2),(6,1),(7,2),(8,6),(9,8),(10,8)]
#print edges

adj_list = defaultdict(list)

for start, end in edges:
	adj_list[end].append(start)
#print adj_list

def dfs_iter(graph, root):
	visited = []
	stack = [root, ]
	
	while stack:
		node = stack.pop()
		
		if node not in visited:
			visited.append(node)
			stack.extend([x for x in graph[node] if x not in visited])
	return visited

b = []
for a in adj_list:
	b.append(a)
for a in b:
	if  len(dfs_iter(adj_list, a)) % 2 == 0:
		cnt += 1

print cnt-1
