val = 3
arr = [3,2,2,3]

def remove_element(arr):

    k = 0
    for i in range(len(arr)):
        if arr[i] != val:
            arr[k] = arr[i]
            k += 1
    return k


print(remove_element(arr))

