
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

l = [64, 34, 25, 12,12, 22,11, 11, 90]
print(bubble_sort(l))

def duplicates(l):
    b = []
    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            b.append(l[i])
    return b

print(duplicates(l))