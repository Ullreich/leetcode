def strStr(haystack: str, needle: str) -> int:
    # check for empty needle
    if len(needle) == 0:
        return 0
    # assert that haystack is at least as long as needle
    if len(haystack) < len(needle):
        return -1
    # index over haystack to see if haystack contains needle
    for i in range(0, len(haystack)-len(needle)+1):
        if needle == haystack[i:i+len(needle)]:
            return i
    # base case
    return -1

def strStr(haystack: str, needle: str) -> int:
    #if len(needle) == 0:
    #    return 0
    return haystack.find(needle)

print(strStr('ll', ''))