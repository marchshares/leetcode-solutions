from yandex_contest import SolutionScriptAbs, TestCaseRunner
from unittest import TestCase


class SolutionScript(SolutionScriptAbs):

    def run(self):
        with open('input.txt') as f, open('output.txt', 'w') as g:
            w1 = f.readline().rstrip()
            w2 = f.readline().rstrip()

            if len(w1) != len(w2):
                g.write("0\n")
            else:
                l = len(w1)
                m = {}
                for i in range(l):
                    v = m.get(w1[i], 0)
                    m[w1[i]] = v + 1

                    v = m.get(w2[i], 0)
                    m[w2[i]] = v - 1

                all_found = True
                for v in m.values():
                    if v != 0:
                        all_found = False
                        break

                if all_found:
                    g.write("1\n")
                else:
                    g.write("0\n")


class TestCases(TestCase):

    def test0(self):
        test_case_data = {
            "input":
                "qiu\n" +
                "iuq\n"
            ,
            "output": "1\n"
        }

        TestCaseRunner.run_test_case(self, SolutionScript(), test_case_data)

