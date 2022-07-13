def two_sum(arr, target):

    value = {}

    for i,elem in enumerate(arr):
        comp = target - elem
        if comp in value:
            return [value[comp],i]
        value[elem]=i #we are adding element as key and its index as value so that if we use the element and call the dict it returns index
    return[]

list1 = [1,2,4,5]
list2 = [9, 10, 11, 12]
target = 7
print(two_sum(list1,target))
print(two_sum(list2,target))