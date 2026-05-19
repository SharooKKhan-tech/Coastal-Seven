a = [1, 2, 3, 1, 2, 4, 5, 6, 5]
dup = []
for i in a:
    for j in range(i + 1, len(a)):
        if a[i] == a[j] and a[i] not in dup:
            dup.append(a[i])
print("Duplicates in the list are:", dup)