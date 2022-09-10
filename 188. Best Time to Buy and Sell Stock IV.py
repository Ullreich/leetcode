class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        sol = max_diff(prices, k)
        # max(sol)
        sol.sort(key=lambda x: -x)
        return sum(sol[:k])


def max_diff(arr, depth=1, sell=False):
    # does not work, new idea
    if depth == 0:
        return []
    l, r = 0, len(arr)
    max_d = 0
    b = None

    for i, val in enumerate(arr[:-1]):
        for j, it_val in enumerate(arr[i:]):
            if sell and (val - it_val) > max_d:
                l, r = i, i + j
                max_d = val - it_val
                b = True
            elif not sell and (it_val - val) > max_d:
                l, r = i, i + j
                max_d = it_val - val
                b = False
    if max_d == 0:
        return [0]
    return [max_d] + max_diff(arr[:l], depth - 1, b) + max_diff(arr[l:r], depth - 1, not b) + max_diff(arr[r:],
                                                                                                       depth - 1, b)