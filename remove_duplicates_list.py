duplicate = [ 1, 2, 3, 4, 3, 4, 3, 5, 3]
res = []

for i in duplicate:
    if i not in res:
        res.append(i)
    
print(res)

res1[]
[res.append(i) for i in duplicate if i not in res ]


res2 = [i for n, i in enumerate(duplicate) if i not in duplicate[:n]]
print(res2)


