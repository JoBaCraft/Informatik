def quicksort(list) -> list[int]:
    if len(list) <= 1:
        return list  # Wenn Liste nur 1 Element oder weniger hat wird sie ausgegeben, da sie schon sortiert ist
    else:
        pivot = list[0] # Erste Stelle der Liste wird als Mittelpunkt genommen
        left = [x for x in list[1:] if x < pivot]  # Elemente < pivot werden in neue Liste (left) eingefuegt
        right = [x for x in list[1:] if x >= pivot] # Elemente >= pivot werden in neue Liste (right) eingefuegt
        return quicksort(left) + [pivot] + quicksort(right) # Rekursive wdh. mit Teil-Listen bis alles sortiert ist

list = [1,6,3,5,8,9,2,4,7,10]
sorted_list = quicksort(list)
print(sorted_list)