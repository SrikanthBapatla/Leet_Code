#this is basic of the search insert position leet code program
#this only returns the idex of items which are present in the array



def search_insert_position(arr, target):
    for index,item in enumerate(arr):
        if item == target:
            return index
        

arr = [1,3,5,6]
target = 5
print(search_insert_position(arr,target))