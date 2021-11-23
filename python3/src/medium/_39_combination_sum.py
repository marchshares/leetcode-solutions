from typing import List


class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
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
            # print(f"{str(candidates[curr:]):<25}, {candidates[i]:<3}({i}), {str(path):<10}, {target}, {res}")

            if target-candidates[i] < 0:
                # print(f"Stop: next_target={target-candidates[i]}")
                break

            path.append(candidates[i])
            self.rec_func(candidates, i, target-candidates[i], path, res)
            path.pop()


res = Solution().combinationSum(candidates = [2,3,6,7], target = 7)
assert res == [[2,2,3],[7]], res

res = Solution().combinationSum(candidates = [2,3,5], target = 8)
assert res == [[2,2,2,2],[2,3,3],[3,5]], res

res = Solution().combinationSum(candidates = [2], target = 1)
assert res == [], res

res = Solution().combinationSum(candidates = [1], target = 1)
assert res == [[1]], res

res = Solution().combinationSum(candidates = [1], target = 2)
assert res == [[1,1]], res
