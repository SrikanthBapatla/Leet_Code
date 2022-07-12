
n = int(input("Enter the range for list: "))
a = list(map(int,input("Enter the items in list: ").strip().split()))[:n]

for index, value in enumerate(a):
    print("The index is: ", index , "The value is: ", value)
