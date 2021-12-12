from yandex_contest import SolutionScriptAbs, TestCaseRunner
from unittest import TestCase


class SolutionScript(SolutionScriptAbs):
    '''
    Дано N отрезков (3 <= N <= 100 000). Необходимо выбрать среди них такие (от 3 до N), чтобы
    сумма их длин получилась максимальной, но при этом из трех любых среди них можно было составить треугольник.
    В ответе выведите получившуюся сумму длин выбранных отрезков или 0, если таковых не существует.

    Пример входного файла input.txt

    3 2 5 4 1

    Пример выходного файла output.txt

    12
    '''
    def run(self):
        with open('input.txt') as f, open('output.txt', 'w') as g:
            l = f.readline().rstrip()
            ss = [int(x) for x in l.split(' ')]

            ss.sort(reverse=True)

            max_sum = 0
            cur_sum = ss[0]+ss[1]
            last_idx = 0
            for cur_idx in range(2, len(ss)):
                cur_sum += ss[cur_idx]

                i = cur_idx-2
                while (i >= last_idx) and (ss[cur_idx]+ss[cur_idx-1] > ss[i]):
                    i -= 1

                j = i
                while j >= last_idx:
                    cur_sum -= ss[j]
                    j -= 1

                last_idx = i+1

                if cur_idx-last_idx > 1:
                    max_sum = max(max_sum, cur_sum)
                # print(f"cur_idx: {cur_idx}, cur_sum: {cur_sum}, last_idx: {last_idx}, max_sum: {max_sum}")

            g.write(str(max_sum)+"\n")


class TestCases(TestCase):

    def test0(self):
        test_case_data = {
            "input": \
                "3 2 5 4 1\n",
            "output": \
                "12\n"
        }

        TestCaseRunner.run_test_case(self, SolutionScript(), test_case_data)



