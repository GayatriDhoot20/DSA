array = [10, 50, 30, 20, 40]


def bubble_sort(a):
    for i in range(0, len(a)):
        for j in range(1, len(a)-1):
            if a[j] >= a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    return a


print(bubble_sort(array))
