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
c = 2   

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

max_weight = -1
max_edge = None     
cur = w
while cur != v:
    prev, weight = parent[cur]
    if weight > max_weight:
        max_weight = weight
        max_edge = (prev, cur)
    cur = prev

if c < max_weight:
    u1, u2 = max_edge
    T[u1] = [(x, ww) for (x, ww) in T[u1] if x != u2]
    T[u2] = [(x, ww) for (x, ww) in T[u2] if x != u1]
    T[v].append((w, c))
    T[w].append((v, c))
    print(f"Удалили ребро {max_edge}: вес {max_weight}, добавили {v};{w}, вес {c}")
else:
    print(f"T остаётся MST: новое ребро вес {c} не легче самого тяжёлого на пути вес {max_weight}")

print("Новое MST:")
for u in range(n):
    print(f"  {u}: {T[u]}")