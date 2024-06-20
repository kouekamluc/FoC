
def means():
    
    l = list(map(int , input("Enter the numbers seperated by space:").split()))    
    lists = []
    total_lists = 0
    
    for i in range(len(l)):
        total_lists += l[i]
        lists.append(total_lists/(i+1))
    return lists



print(means())

# time complexity of O(n) time complexity



def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

numbers = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(numbers))