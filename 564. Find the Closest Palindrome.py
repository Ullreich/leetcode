def findpalindrome(n: str):
    asint = int(n)

    i=1
    while not (ispalindrome(asint-i) or ispalindrome(asint+i)):
        i+=1

    if ispalindrome(asint-i):
        return str(asint-i)
    return str(asint+i)

def ispalindrome(number):
    return not int(str(number))-int(str(number)[::-1])


print(findpalindrome(1223168221))
#print(ispalindrome(22))