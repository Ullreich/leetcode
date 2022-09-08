class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # do it in > O(n^2) time

        # sort list in O(n log n)
        sortlist = nums.copy()
        sortlist.sort()

        #go through sorted list > O(n)
        while sortlist:
            current = sortlist.pop(0)
            # find if complimentary value in list > O(log n) -> O(n log n)
            res = pivotcheck(sortlist, target-current)
            if not res==None:
                # print(current, res)
                ind1 = nums.index(current)
                nums[ind1] = None
                ind2 = nums.index(res)
                return sorted([ind1, ind2])



def pivotcheck(arr, numb):
    middle = int(len(arr)/2)

    if arr==[]:
        return None
    if arr[middle] == numb:
        return arr[middle]
    elif arr[middle] > numb:
        return pivotcheck(arr[:middle], numb)
    else:
        if len(arr)%2==0:
            return pivotcheck(arr[middle:], numb)
        else:
            return pivotcheck(arr[middle+1:], numb)