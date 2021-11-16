package com.lc.easy;

import java.util.*;

/**
 * <a href="https://leetcode.com/problems/two-sum/">1. Two Sum</a>
 * */
public class TwoSum {

    public static void main(String[] args) {
        int[] nums = new int[]{2,7,11,15};

        int[] res = new Solution().twoSum(nums, 9);
        System.out.println(Arrays.toString(res));
    }

    static class Solution {
        public int[] twoSum(int[] nums, int target) {
            Map<Integer, Integer> map = new HashMap<>();
            for (int i = 0; i < nums.length; i++) {
                map.put(nums[i], i);
            }

            for (int i = 0; i < nums.length; i++) {
                int diff = target - nums[i];
                if (map.containsKey(diff) && map.get(diff) != i) {
                    return new int[] {map.get(diff), i};
                }
            }

            throw new IllegalArgumentException();
        }
    }
}



