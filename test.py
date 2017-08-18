example = [4, 6, 2, 7, 3, 5, 1, 9, 8, 10]
def bubble_sort(list):
    for i in range(0, len(list) - 1):                 # 记录冒泡的次数
        for j in range(0, len(list)-1-i):             # 记录每轮冒泡排序比较的次数
            if list[j] > list[j + 1]:
                list[j + 1], list[j] = list[j], list[j+ 1]
                j = j + 1
            else:
                continue
    return list
print(bubble_sort(example))