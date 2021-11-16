package com.lc.medium;

import java.util.ArrayList;
import java.util.List;

/**
 * <a href="https://leetcode.com/problems/add-two-numbers/">2. Add Two Numbers</a>
 * */
public class AddTwoNumbers {

    public static void main(String[] args) {
        ListNode l1 =
                new ListNode(2,
                    new ListNode(4,
                        new ListNode(3)
                    )
                );

        ListNode l2 =
                new ListNode(5,
                        new ListNode(6,
                                new ListNode(4)
                        )
                );


        ListNode listNode = new Solution().addTwoNumbers(l1, l2);
        System.out.println(listNode.toList()); // [7,0,8]
    }

     static class Solution {
        public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
            ListNode dummyNode = new ListNode();

            ListNode res = dummyNode;
            ListNode p = l1;
            ListNode q = l2;
            int carry = 0;
            while (p != null || q != null) {
                int sum = carry;

                if (p != null) {
                    sum += p.val;
                    p = p.next;
                }

                if (q != null) {
                    sum += q.val;
                    q = q.next;
                }

                if (sum >= 10) {
                    sum -= 10;
                    carry = 1;
                } else {
                    carry = 0;
                }

                res.next = new ListNode(sum);
                res = res.next;
            }

            if (carry > 0) {
                res.next = new ListNode(carry);
            }

            return dummyNode.next;
        }
    }
}

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }

    public List<Integer> toList() {
        List<Integer> lst = new ArrayList<>();

        lst.add(val);
        ListNode cur = next;

        while (cur != null) {
            lst.add(cur.val);
            cur = cur.next;
        }

        return lst;
    }
}

