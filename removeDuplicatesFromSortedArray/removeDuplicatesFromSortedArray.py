
def remove_duplicate(arr):
    k = 1

    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            arr[k] = arr[i]
            k +=1
    return k

arr1 = [0,1,1,2,2,2,3,3,4,5]
arr2 = [1,1,2,3,4,5]
print(remove_duplicate(arr1))
print(remove_duplicate(arr2))