hospitals = {
    "H1": ["S2", "S1", "S3"],
    "H2": ["S1", "S3", "S2"],
    "H3": ["S3", "S1", "S2"]
}

students = {
    "S1": ["H2", "H1", "H3"],
    "S2": ["H1", "H2", "H3"],
    "S3": ["H1", "H3", "H2"]
}

capacities = {"H1": 1, "H2": 2, "H3": 1}

assignment = {"H1": ["S1"], "H2": ["S2"], "H3": ["S3"]}

student_to_hospital = {}
for h, students_list in assignment.items():
    for s in students_list:
        student_to_hospital[s] = h

all_students = set(students.keys())
assigned_students = set(student_to_hospital.keys())
unassigned_students = all_students - assigned_students

is_stable = True

for h in hospitals:
    for current_s in assignment.get(h, []):
        h_prefs = hospitals[h]
        current_index = h_prefs.index(current_s)
        better_students = h_prefs[:current_index]
        
        for better_s in better_students:
            if better_s in unassigned_students:
                is_stable = False
                break
            
            if better_s in assigned_students:
                current_h_for_better = student_to_hospital[better_s]
                if students[better_s].index(h) < students[better_s].index(current_h_for_better):
                    is_stable = False
                    break
        
        if not is_stable:
            break
    if not is_stable:
        break

if is_stable:
    print("Распределение устойчивое")
else:
    print("Распределение неустойчивое")