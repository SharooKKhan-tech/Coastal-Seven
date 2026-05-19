arr = [4,2,5,7,2,6,8,1,9]
largest = arr[0]
for i in arr:
    if i > largest:
        largest = i 
print("Largest number in the list is:", largest)