from itertools import permutations

n = int(input())
items = [input().split() for _ in range(n)]

best_score = -1.0
best = []

for perm in permutations(items):
    score = 0
    for t, (name, r) in enumerate(perm):
        score += 100 * float(r) ** t
    if score > best_score:
        best_score = score
        best = perm

print("Оптимальный порядок:")
for t, (name, r) in enumerate(best):
    print(f"  Месяц {t}: {name} r={r} выручка={round(100 * float(r)**t, 2)}")

print("итог:", round(best_score, 2))
print()
print("коэф в оптимальном порядке:", [r for name, r in best])