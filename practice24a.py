from collections import deque

n = 5
T = [
    [(1, 1), (2, 3)],        
    [(0, 1), (3, 2)],        
    [(0, 3), (4, 4)],          
    [(1, 2)],               
    [(2, 4)],                  
]

v = 3
w = 4
c = 5

parent = [None] * n
parent[v] = (v, 0)
queue = deque([v])

while queue:
    u = queue.popleft()
    if u == w:
        break
    for neighbor, weight in T[u]:
        if parent[neighbor] is None:
            parent[neighbor] = (u, weight)
            queue.append(neighbor)

max_weight_on_path = 0
cur = w
while cur != v:
    prev, weight = parent[cur]
    if weight > max_weight_on_path:
        max_weight_on_path = weight
    cur = prev

print(f"ребро: ({v}, {w}), вес = {c}")
print(f"Максимальный вес ребра на пути {v} {w} в T: {max_weight_on_path}")

if c >= max_weight_on_path:
    print("T остаётся минимальным остовным деревом.")
else:
    print("T больше не является MST, его можно улучшить заменой ребра.")