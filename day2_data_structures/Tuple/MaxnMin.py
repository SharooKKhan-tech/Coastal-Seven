tup = (5, 20, 3, 7, 6, 8)
K = 2
m1 = []
m2 = []
for ele in tup:
    if len(m1) < K:
        m1.append(ele)
    else:
        if ele < max(m1):
            m1.remove(max(m1))
            m1.append(ele)
    if len(m2) < K:
        m2.append(ele)
    else:
        if ele > min(m2):
            m2.remove(min(m2))
            m2.append(ele)

m1.sort()          
m2.sort(reverse=True) 

print(m1)
print( m2)