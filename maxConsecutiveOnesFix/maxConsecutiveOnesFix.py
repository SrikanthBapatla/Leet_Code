def consecutive_ones(arr):
    count = 0
    output = 0
    for index,item in enumerate(arr):
        if item == 1:
            count +=1
            output = max(output,count)
        elif item !=1:
            count = 0
    return output

arr = [1,0,1,1,0,1]
print(consecutive_ones(arr))