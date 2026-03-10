intervals = [
    (10, 12, 100),
    (9, 11, 50),
    (14, 16, 80),
    (11, 13, 70),
    (13, 14, 30),
    (15, 17, 90),
    (12, 15, 120)
]
n = len(intervals)
intervals.sort(key=lambda x: x[1])

ends = [intervals[i][1] for i in range(n)]
prev = [-1]*n
for i in range(n):
    left, right = 0, i-1
    start = intervals[i][0]
    result = -1
    while left <= right:
        mid = (left + right)//2
        if ends[mid] <= start:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    prev[i] = result

maximum = [0] * n
take_decision = [False] * n

for i in range(n):
    include_weight = intervals[i][2]
    if prev[i] != -1:
        include_weight += maximum[prev[i]]
    exclude_weight = maximum[i-1] if i > 0 else 0
    if include_weight > exclude_weight:
        maximum[i] = include_weight
        take_decision[i] = True
    else:
        maximum[i] = exclude_weight
        take_decision[i] = False

selected = []
i = n - 1
while i >= 0:
    if take_decision[i]:
        selected.append(intervals[i])
        i = prev[i]
    else:
        i -= 1

selected.reverse()
print(f'макс вес: {maximum[n-1]}')
print('интервалы')
for start, end, weight in selected:
    print(start, end, weight)