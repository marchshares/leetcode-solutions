from yandex_contest import SolutionScriptAbs, TestCaseRunner
from unittest import TestCase


class SolutionScript(SolutionScriptAbs):
    '''
    D. Задача 4.

    Условие Дан массив, состоящий из букв 'X', 'Y' и 'O'. Необходимо найти кратчайшее расстояние между буквами 'X' и 'Y', либо вывести 0, если 'X' либо 'Y' отсутствуют. Примечания дистанция между двумя рядом стоящими буквами считается как 1 (одно межбуквенное расстояние) дистанция может считаться в обе стороны

    Пример входного файла input.txt

    "OOOXOOYOXO"

    Пример выходного файла output.txt

    2
    '''
    def run(self):
        with open('input.txt') as f, open('output.txt', 'w') as g:
            l = f.readline().rstrip()

            x_i = -1
            y_i = -1
            min_s = len(l)
            for i in range(len(l)):
                if l[i] == 'O':
                    continue

                if l[i] == 'X':
                    x_i = i
                    if y_i != -1:
                        min_s = min(min_s, x_i-y_i)

                if l[i] == 'Y':
                    y_i = i
                    if x_i != -1:
                        min_s = min(min_s, y_i-x_i)

            if min_s == len(l):
                min_s = 0

            g.write(str(min_s)+"\n")


class TestCases(TestCase):

    def test0(self):
        test_case_data = {
            "input": \
                "OOOXOOYOXO\n",
            "output": \
                "2\n"
        }

        TestCaseRunner.run_test_case(self, SolutionScript(), test_case_data)

    def test1(self):
        test_case_data = {
            "input": \
                "XOOOOOY\n",
            "output": \
                "6\n"
        }

        TestCaseRunner.run_test_case(self, SolutionScript(), test_case_data)

    def test2(self):
        test_case_data = {
            "input": \
                "XOOOOO\n",
            "output": \
                "0\n"
        }

        TestCaseRunner.run_test_case(self, SolutionScript(), test_case_data)

    def test3(self):
        test_case_data = {
            "input": \
                "XOYYXO\n",
            "output": \
                "1\n"
        }

        TestCaseRunner.run_test_case(self, SolutionScript(), test_case_data)



