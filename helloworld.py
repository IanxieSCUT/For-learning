"""A = {1: 16, 2: 12, 3: 21, 4: 22, 5: 17, 6: 12}
B = sorted(A.items(),key=lambda d:d[1],reverse=True)
C = B[:3]

print (C)"""

"""A = ['123','123','123']
B = A.count('123')
print (B)"""

'''A = ''
for num in range(3):
	A = A+'1'
print (A)'''

"""print(int(10e10))"""

def bubble_sort(lists):
    # 冒泡排序
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists
print(bubble_sort([2,31,23,4,]))