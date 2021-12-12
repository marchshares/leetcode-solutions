from yandex_contest import SolutionScriptAbs, TestCaseRunner
from unittest import TestCase


class SolutionScript(SolutionScriptAbs):

    def run(self):
        def rec_func(n, s, left, right):
            if left == n and right == n:
                g.write(s+'\n')

            if left < n:
                rec_func(n, s + '(', left + 1, right)
            if right < left:
                rec_func(n, s + ')', left, right + 1)

        with open('input.txt') as f, open('output.txt', 'w') as g:

            n = int(f.readline().rstrip())

            if n > 0:
                rec_func(n, '', 0, 0)


class TestCases(TestCase):

    def test0(self):
        test_case_data = {
            "input": "2\n",
            "output": "(())\n" +
                      "()()\n"
        }

        TestCaseRunner.run_test_case(self, SolutionScript(), test_case_data)

    def test1(self):
        test_case_data = {
            "input": "3\n",
            "output": \
                "((()))\n" +
                "(()())\n" +
                "(())()\n" +
                "()(())\n" +
                "()()()\n"

        }

        TestCaseRunner.run_test_case(self, SolutionScript(), test_case_data)





