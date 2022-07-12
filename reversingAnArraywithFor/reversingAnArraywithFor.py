n = int(input("Enter range: "))
arr = list(map(int,input("Enter array items with spaces in between: ").strip().split()))[:n]
reversed_arr = []

for i in arr:
    reversed_arr.insert(0,i)
print(reversed_arr)
