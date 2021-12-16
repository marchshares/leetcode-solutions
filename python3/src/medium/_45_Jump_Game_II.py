from typing import List
from math import trunc

class Solution:
    def jump(self, nums: List[int]) -> int:
        i=0
        last_index = len(nums)-1

        jumps_count = 0
        while i < last_index:
            jumps_count += 1

            # print(i)
            num_i = nums[i]

            if i+num_i >= last_index:
                return jumps_count

            max_idx_for_range = -1
            i_max = -1
            for j in range(i+1, i+num_i+1):
                max_jump_len = nums[j]
                max_idx_from_j = j+max_jump_len
                # print(f" - {j}, {max_idx_from_j}")

                if max_idx_from_j > last_index:
                    return jumps_count+1

                if max_idx_from_j >= max_idx_for_range:
                    max_idx_for_range = max_idx_from_j
                    i_max = j
                    # print(f" - max: {i_max}, {max_idx_for_range}")

            i = i_max

        return jumps_count


nums = [1, 2]
res = Solution().jump(nums)
assert res == 1, res

nums = [2, 3, 1, 1, 4]
res = Solution().jump(nums)
assert res == 2, res

nums = [2,3,0,1,4]
res = Solution().jump(nums)
assert res == 2, res

nums = [1,1,1,1,1,1,1,1,1,9]
res = Solution().jump(nums)
assert res == 9, res

nums = [2,0,3,0,4,0,0,0,1,9]
res = Solution().jump(nums)
assert res == 4, res