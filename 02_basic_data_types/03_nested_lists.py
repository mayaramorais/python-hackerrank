list_student = []
for i in range(int(input())):
    name = input()
    score = float(input())
    list_student.append([name,score])

sorted_list = sorted(list_student, key=lambda x: x[1])
get_score = [s[1] for s in sorted_list]
get_min = min(get_score)
second_grade = sorted_list[0][1]
for name, grade in sorted_list:
    if grade > get_min:
        second_grade = grade
        break
print('\n'.join([name for name, grade in sorted(sorted_list) if grade == second_grade]))