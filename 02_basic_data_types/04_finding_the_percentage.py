n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

marks = student_marks[query_name]
percent_marks = sum(marks)/len(marks)
print("%.2f"%(percent_marks))