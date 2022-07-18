#logic is to only check if the last digit is 9 or not and then add 1 to the last digit in array and print result

def plus_one(arr):
    n = len(arr)
    if arr[n-1] != 9:
        arr[n-1] += 1
        return arr
    return arr

arr = [1,2,3]
print(plus_one(arr)) 