arr = [1,2,3,4,5,6,7,8,9,10]
d = 2
arr[:] = arr[d:] + arr[:d]
print("Rotated list:", arr)