from yandex_contest import SolutionScriptAbs, TestCaseRunner
from unittest import TestCase


class SolutionScript(SolutionScriptAbs):

    def run(self):
        with open('input.txt') as f, open('output.txt', 'w') as g:
            l = int(f.readline().rstrip())

            if l > 0:
                cur_num = int(f.readline().rstrip())
                g.write(str(cur_num)+'\n')

                for i in range(1, l):
                    num = int(f.readline().rstrip())

                    if num == cur_num:
                        continue
                    else:
                        cur_num = num
                        g.write(str(cur_num)+'\n')


class TestCases(TestCase):

    def test0(self):
        test_case_data = {
            "input": \
                "5\n" +
                "-1\n" +
                "0\n" +
                "0\n" +
                "0\n" +
                "1\n",
            "output": \
                "-1\n" +
                "0\n" +
                "1\n"
        }

        TestCaseRunner.run_test_case(self, SolutionScript(), test_case_data)

    def test1(self):
        test_case_data = {
            "input": \
                "5\n" +
                "2\n" +
                "4\n" +
                "8\n" +
                "8\n" +
                "8\n",
            "output": \
                "2\n" +
                "4\n" +
                "8\n"
        }

        TestCaseRunner.run_test_case(self, SolutionScript(), test_case_data)





