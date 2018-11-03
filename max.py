def findMinAndMax(L):
    if len(L)>=1:
        max = L[0]
        min = L[0]
        for x in L:
            if max<x:
                max = x
            if min>x:
                min = x
        return (min, max)
    else:
        return (None, None)

# 测试
if findMinAndMax([]) != (None, None):
    print(findMinAndMax([]), 1)
elif findMinAndMax([7]) != (7, 7):
    print(findMinAndMax([7]), 2)
elif findMinAndMax([7, 1]) != (1, 7):
    print(findMinAndMax([7, 1]), 3)
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print(findMinAndMax([7, 1, 3, 9, 5]), 4)
else:
    print('测试成功!')