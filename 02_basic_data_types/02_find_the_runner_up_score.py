n = int(input())
arr = map(int, input().split())

arr_sort = sorted(set(arr))

print(arr_sort[-2])