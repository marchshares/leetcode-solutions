from typing import List


class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        self.rec_func(candidates, 0, target, [], res)

        return res

    def rec_func(self, candidates, curr, target, path, res):

        if target == 0:
            res.append(path.copy())
            # print("Added: " + str(res))
            return

        for i in range(curr, len(candidates)):
            if target-candidates[i] < 0:
                break

            # print(f"{str(candidates[curr:]):<25}, {candidates[i]:<3}({i}), {str(path):<10}, {target}, {res}")
            if i > curr and candidates[i] == candidates[i-1]:
                continue

            path.append(candidates[i])
            self.rec_func(candidates, i+1, target-candidates[i], path, res)
            path.pop()


res = Solution().combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8)
assert res == [
    [1, 1, 6],
    [1, 2, 5],
    [1, 7],
    [2, 6]
], res

res = Solution().combinationSum2(candidates = [2,5,2,1,2], target = 5)
assert res == [
    [1, 2, 2],
    [5]
], res
