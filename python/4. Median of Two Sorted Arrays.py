class Solution:
    #this is not O(log(n+m))
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        counter = 0

        """
        #this could be done faster by just appending the rest of the nonempty list but imo this is elegant
        while nums1 != [] or nums2 != []:
            if nums2 == [] or (nums1 != [] and nums1[0] < nums2[0]):
                combinedlist.append(nums1.pop(0))
            else:
                combinedlist.append(nums2.pop(0))
            counter+=1

        if counter%2==1:
            return combinedlist[int(counter/2)]
        else:
            return (combinedlist[int((counter/2)-1)] + combinedlist[int(counter/2)])/2
        """

def

    def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
        pass

    def pivot(arr: list[int], m) -> list[int]:
        if m <= mean(arr):
            if len(arr) % 2 == 0:
                return arr[:int(len(arr) / 2)]
            else:
                return arr[:int(len(arr) / 2) + 1]
        else:
            if len(arr) % 2 == 0:
                return arr[int(len(arr) / 2):]
            else:
                return arr[int(len(arr) / 2):]

    def mean(arr: list[int]) -> float:
        if len(arr) % 2 == 1:
            return arr[int(len(arr) / 2)]
        else:
            return (arr[int(len(arr) / 2 - 1)] + arr[int(len(arr) / 2)]) / 2

    test2 = [1, 7, 8]
    test = [3, 4, 5, 6]
    bigtest = (test + test2)
    bigtest.sort()
    print(bigtest)
    print(mean(bigtest))
    print("---------")

    if len(test) != 0:
        mean1 = mean(test)
    if len(test2) != 0:
        mean2 = mean(test2)

    while (len(test) > 1 or len(test2) > 1):
        mean1 = mean(test)
        mean2 = mean(test2)

        if mean1 == mean2:
            break

        print(f"arr {test} and arr2 {test2}")
        print(f"mean1 {mean1} and mean2 {mean2}")
        test = pivot(test, mean2)
        test2 = pivot(test2, mean1)

    mean1 = mean(test)
    mean2 = mean(test2)

    print(f"arr {test} and arr2 {test2}")
    print(f"mean1 {mean1} and mean2 {mean2}")