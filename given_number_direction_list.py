def shift_number(k, my_list, direction=""):
    count = 0
    for  item in my_list[:]:
        if k == item:
            count += 1
            my_list.remove(item)

    for _ in range(count):     
        if direction == "l":
             my_list.append(k)
        elif direction == "r":
            my_list.insert(0, k)
    print(count)
    return my_list
    

    
print(shift_number(4, [1, 2, 3, 4, 5, 3, 4, 4, 3, 2, 4], "l"))