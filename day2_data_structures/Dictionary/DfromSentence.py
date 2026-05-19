s1 = "Geeks for Geeks"
s2 = s1.split()  
print(s2)
res = []  

for word in s2:
    if word not in res:
        res.append(word)
        
s3 = ' '.join(res)
print(s3) 