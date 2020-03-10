def common_elements(lst1, lst2):
    p1 = 0
    p2 = 0
    result = [ ]
    while p1 < len(lst1) and p2 < len(lst2):
        if lst1[p1] == lst2[p2]:
            result.append(lst1[p1])
            p1 += 1
            p2 += 1
        elif lst1[p1] > lst2[p2]:
            p2 += 1
        else:
            p1 += 1
    return result

print(common_elements([1, 2, 4, 6, 9], [1, 3, 4, 5, 9, 10]))