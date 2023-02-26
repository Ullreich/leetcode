class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        list_of_strings = [str(i) for i in range(1,10)]
        foo_list = list()

        for i in range(n-1):
            for i in list_of_strings:
                if int(i[-1])-k>=0:
                    foo_list.append(i+str(int(i[-1])-k))
                if int(i[-1])+k<=9:
                    foo_list.append(i+str(int(i[-1])+k))
            list_of_strings = foo_list
            foo_list = list()
        return set([int(i) for i in list_of_strings])