
def consecutive_ones(arr):
    count = 0
    consecutive = 0
    for index,item in enumerate(arr):
        if item == 1:
            count +=1
        elif item !=1:
            count = 0
    return count

arr = [1,1,1,0,2,3,1,1,1,1]
print(consecutive_ones(arr))