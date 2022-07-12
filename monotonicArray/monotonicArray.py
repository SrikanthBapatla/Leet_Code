arr = [1,2,3]

inc = True
dec = True

for i in range(1, len(arr)):
    if arr[i] > arr[i-1]:
        dec = False
    if arr[i] < arr[i-1]:
        inc = False
        
print(dec or inc)