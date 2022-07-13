
def longest_common_prefix(arr):
    prefix = arr[0]
    prefixlen = len(prefix)

    for pref in arr[1:]:
        while prefix != pref[0:prefixlen]:
            prefix = prefix[0:(prefixlen - 1)]
            prefixlen -= 1

        if prefixlen == 0:
            return ("''")
    return (prefix)

string_list = ["please", "place","plates"]
string_list1 = ["teeth", "tiger", "tour"]
string_list2= ["look", "pop", "out"]

print(longest_common_prefix(string_list))
print(longest_common_prefix(string_list1))
print(longest_common_prefix(string_list2))