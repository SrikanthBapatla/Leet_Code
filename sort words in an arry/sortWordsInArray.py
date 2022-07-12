unsorted_string = input("Enter a string: ")
words = unsorted_string.lower().split()
words.sort()

for word in words:
    print(word)