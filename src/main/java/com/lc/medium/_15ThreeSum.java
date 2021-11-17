package com.lc.medium;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * <a href="https://leetcode.com/problems/3sum/">15. 3Sum</a>
 * */
public class _15ThreeSum {

    public static void main(String[] args) {
        List<List<Integer>> res = new Solution().threeSum(new int[]{-1, 0, 1, 2, -1, -4});
        System.out.println(res); // [[-1,-1,2],[-1,0,1]]
    }

    static class Solution {
        public List<List<Integer>> threeSum(int[] nums) {
            Arrays.sort(nums);
            List<List<Integer>> res = new ArrayList<>();
            for (int i = 0; i < nums.length && nums[i] <= 0; ++i)
                if (i == 0 || nums[i - 1] != nums[i]) {
                    twoSumII(nums, i, res);
                }
            return res;
        }
        void twoSumII(int[] nums, int i, List<List<Integer>> res) {
            int lo = i + 1, hi = nums.length - 1;
            while (lo < hi) {
                int sum = nums[i] + nums[lo] + nums[hi];
                if (sum < 0) {
                    ++lo;
                } else if (sum > 0) {
                    --hi;
                } else {
                    res.add(Arrays.asList(nums[i], nums[lo++], nums[hi--]));
                    while (lo < hi && nums[lo] == nums[lo - 1])
                        ++lo;
                }
            }
        }
    }
}



