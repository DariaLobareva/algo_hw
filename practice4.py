from collections import deque


def is_consistent(n, same_pairs, diff_pairs):
    parent = list(range(n))
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for u, v in same_pairs:
        union(u, v)

    graph = {}
    for i in range(n):
        r = find(i)
        if r not in graph:
            graph[r] = []
    
    for u, v in diff_pairs:
        ru, rv = find(u), find(v)
        
        if ru == rv:
            return False
        
        graph[ru].append(rv)
        graph[rv].append(ru)

    color = {}
    
    for start in graph:
        if start not in color:
            queue = deque([start])
            color[start] = 0
            
            while queue:
                v = queue.popleft()
                for to in graph[v]:
                    if to not in color:
                        color[to] = 1 - color[v]
                        queue.append(to)
                    elif color[to] == color[v]:
                        return False
    
    return True


n = 5
same_pairs = [(0, 1), (2, 3)]
diff_pairs = [(1, 2), (3, 4)]

if is_consistent(n, same_pairs, diff_pairs):
    print('Yes')
else: 
    print('No')