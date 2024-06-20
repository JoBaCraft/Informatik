def merge(list1, list2):
    list = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            list.append(list1[i])
            i-=-1
        else:
            list.append(list2[j])
            j-=-1
    while i < len(list1):
        list.append(list1[i])
        i-=-1
    while j < len(list2):
        list.append(list2[j])
        j-=-1
    return list

def mergesort(list, low, high):
    if low >= high:
        out = [list[low]]
        return out
    mid = (low + high) // 2
    return merge(mergesort(list, low, mid), mergesort(list, mid+1, high))

liste = [54,65,24,2,9]
print(mergesort(liste, 0, len(liste)-1))