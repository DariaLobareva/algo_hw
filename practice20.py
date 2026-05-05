n = int(input())
participants = []
for i in range(n):
    line = input().split()
    participants.append((line[0], int(line[1]), int(line[2]), int(line[3])))

participants.sort(key=lambda x: x[2] + x[3], reverse=True)

pool_time = 0
max_finish = 0
for name, s, b, r in participants:
    pool_time += s
    finish = pool_time + b + r
    if finish > max_finish:
        max_finish = finish
    print(name, finish)

print("ответ:", max_finish)