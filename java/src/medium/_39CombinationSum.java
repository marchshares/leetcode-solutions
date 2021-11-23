package com.lc;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * <a href=""></a>
 * */
public class _SolutionTemplate {

    public static void main(String[] args) {
        new Solution();
        System.out.println();
    }

    static class Solution {
        public List<List<Integer>> combinationSum(int[] candidates, int target) {
            return f(target, candidates, 0);
        }

        public List<List<Integer>> f(int partOfSum, int[] candidates, int start) {
            List<List<Integer>> res = new ArrayList<List<Integer>>();

            for (int i = start; i < candidates.length; i++) {
                if (partOfSum-candidates[i] > 0) {
                    List<List<Integer>> lsts = f(partOfSum-candidates[i], candidates, i);

                    for(List<Integer> lst : lsts) {
                        lst.add(candidates[i]);
                    }

                    res.addAll(lsts);
                } else if (partOfSum == candidates[i]) {
                    List<Integer> lst = new ArrayList<Integer>();

                    lst.add(candidates[i]);

                    res.add(lst);
                }
            }

            return res;
        }
    }
}



