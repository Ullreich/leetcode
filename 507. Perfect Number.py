class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        return num in [6, 28, 496, 8128, 33550336]


"""
def isperfect(number):
    return number==sum([i for i in range(1,int(number/2)+1) if number%i==0])

for i in range(1, 10**8):
    if i%10**7==0:
        print(i)
    if isperfect(i):
        print(i)
"""