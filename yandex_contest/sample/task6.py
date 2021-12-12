from yandex_contest import SolutionScriptAbs, TestCaseRunner
from unittest import TestCase


class SolutionScript(SolutionScriptAbs):
    '''
    G. Интересное путешествие

    Не секрет, что некоторые программисты очень любят путешествовать. Хорошо всем известный программист Петя тоже очень любит путешествовать, посещать музеи и осматривать достопримечательности других городов.
    Для перемещений между из города в город он предпочитает использовать машину. При этом он заправляется только на станциях в городах, но не на станциях по пути. Поэтому он очень аккуратно выбирает маршруты, чтобы машина не заглохла в дороге. А ещё Петя очень важный член команды, поэтому он не может себе позволить путешествовать слишком долго. Он решил написать программу, которая поможет ему с выбором очередного путешествия. Но так как сейчас у него слишком много других задач, он попросил вас помочь ему.
    Расстояние между двумя городами считается как сумма модулей разности по каждой из координат. Дороги есть между всеми парами городов.

    Формат ввода
    В первой строке входных данных записано количество городов
    n
     (
    2
    ≤
    n
    ≤
    1
    0
    0
    0
    ). В следующих
    n
     строках даны два целых числа: координаты каждого города, не превосходящие по модулю миллиарда. Все города пронумерованы числами от 1 до
    n
     в порядке записи во входных данных.
    В следующей строке записано целое положительное число
    k
    , не превосходящее двух миллиардов, — максимальное расстояние между городами, которое Петя может преодолеть без дозаправки машины.
    В последней строке записаны два различных числа — номер города, откуда едет Петя, и номер города, куда он едет.

    Формат вывода
    Если существуют пути, удовлетворяющие описанным выше условиям, то выведите минимальное количество дорог, которое нужно проехать, чтобы попасть из начальной точки маршрута в конечную. Если пути не существует, выведите -1.

    '''
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

