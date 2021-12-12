from yandex_contest import SolutionScriptAbs, TestCaseRunner
from unittest import TestCase


class SolutionScript(SolutionScriptAbs):
    '''
    D. Генерация скобочных последовательностей

    Дано целое число n. Требуется вывести все правильные скобочные последовательности длины 2 ⋅ n, упорядоченные лексикографически (см. https://ru.wikipedia.org/wiki/Лексикографический_порядок).

    В задаче используются только круглые скобки.

    Желательно получить решение, которое работает за время, пропорциональное общему количеству правильных скобочных последовательностей в ответе, и при этом использует объём памяти, пропорциональный n.

    Формат ввода
    Единственная строка входного файла содержит целое число n, 0 ≤ n ≤ 11

    Формат вывода
    Выходной файл содержит сгенерированные правильные скобочные последовательности, упорядоченные лексикографически.
    '''
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





