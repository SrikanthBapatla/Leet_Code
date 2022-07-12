str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) == len(str2):
    sorted_str1 = sorted(str1.lower())
    sorted_str2 = sorted(str2.lower())
    if sorted_str1 == sorted_str2:
        print("They are Anagrams")
    else:
        print("They are not anagrams")
else:
    print("They are not Anagrams")

