
def means(l):
    sum = 0
    for i in range(len(l)):
        sum += l[i]
        l[i] = sum/(i+1)
    return l


l = [1,2,3,4]
print(means(l))