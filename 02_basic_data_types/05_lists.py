N = int(input())
l = []

for i in range(N):
    entry = input().split(" ")
    if entry[0] == "insert":
        l.insert(int(entry[1]),int(entry[2]))
    if entry[0] == "print":
        print(l)
    if entry[0] == "remove":
        l.remove(int(entry[1]))
    if entry[0] == "append":
        l.append(int(entry[1]))
    if entry[0] == "sort":
        l.sort()
    if entry[0] == "pop":
        l.pop()
    if entry[0] == "reverse":
        l.reverse()