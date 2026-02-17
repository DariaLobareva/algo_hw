hos = {
    "H1": ["S2", "S1", "S3"],
    "H2": ["S1", "S3", "S2"],
    "H3": ["S3", "S1", "S2"]
}

student = {
    "S1": ["H2", "H1", "H3"],
    "S2": ["H1", "H2", "H3"],
    "S3": ["H1", "H3", "H2"]
}

match = {"H1": "S1", "H2": "S2", "H3": "S3"}

reverse_match = dict(zip(match.values(), match.keys()))
is_stable = True

for i, j in match.items():
    preferences = hos[i]
    index_current = preferences.index(j)
    better_student = preferences[:index_current]
    for s in better_student:
        if student[s].index(i) < student[s].index(reverse_match[s]):
            is_stable = False
            break

if is_stable:
    print("Устойчивое")
else:
    print("Неустойчивое")
