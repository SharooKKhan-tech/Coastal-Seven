t1 = (4, 5)
t2 = (7, 8)
res = []
for i in t1:
    for j in t2:
        res.append((i, j))
        res.append((j, i))
print("All possible pairs:", res)