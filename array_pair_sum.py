#Given an integer array , output all the unique pairs that sum up to a specific value k
def pair_sum(array, k):
    if len(array) < 2:
        return print("Too small")

    seen = ()
    output = ()

    for num in array:
        target = num - k

        if target not in seen:
            seen.add(num)

        else:
            output.add((min(num, target), max(num, target)))
            
    print("\n".join(map(str, list(output))))

pair_sum([1, 2, 3, 2], 4)