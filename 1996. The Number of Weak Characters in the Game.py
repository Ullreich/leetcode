class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:

        # had to look at solutions for this one :(

        properties.sort(key=lambda x: [-x[0], x[1]])

        ret = 0
        m = 0

        for _, val in properties:
            if val < m:
                ret += 1
            else:
                m = val

        return ret