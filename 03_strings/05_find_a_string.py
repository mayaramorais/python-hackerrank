def count_substring(string, sub_string):
    l=[]
    for i in range(0,len(string)):
        for j in range(1,len(string)+1):
            l.append(string[i:j])
    if sub_string in l:
        return l.count(sub_string)
    else: return 0