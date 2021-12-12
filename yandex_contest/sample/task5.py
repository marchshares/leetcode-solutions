from yandex_contest import SolutionScriptAbs, TestCaseRunner
from unittest import TestCase


class SolutionScript(SolutionScriptAbs):

    def run_v1(self):
        with open('input.txt') as f, open('output.txt', 'w') as g:
            w1 = f.readline().rstrip()
            w2 = f.readline().rstrip()
            if len(w1) != len(w2):
                g.write("0\n")
            else:
                marks2 = [False for i in range(len(w1))]
                found_all = True
                for c1 in w1:
                    found = False
                    for i in range(len(w2)):
                        c2 = w2[i]
                        if c1 == c2 and not marks2[i]:
                            marks2[i] = True
                            found = True
                            break
                    if not found:
                        found_all = False
                        break
                if found_all:
                    g.write("1\n")
                else:
                    g.write("0\n")

    def run_v2(self):
        def func(i, w1, marks1, w2, marks2):
            if marks1[i]:
                return True

            c1 = w1[i]
            for j in range(i, len(w2)):
                c2 = w2[j]
                if c1 == c2 and not marks2[j]:
                    marks1[i] = True
                    marks2[j] = True
                    return True

            return False

        with open('input.txt') as f, open('output.txt', 'w') as g:
            w1 = f.readline().rstrip()
            w2 = f.readline().rstrip()

            if len(w1) != len(w2):
                g.write("0\n")
            else:
                l = len(w1)
                marks1 = [False for i in range(l)]
                marks2 = [False for i in range(l)]

                found_all = True
                for i in range(l):
                    found = func(i, w1, marks1, w2, marks2)
                    if not found:
                        found_all = False
                        break

                    found = func(i, w2, marks2, w1, marks1)
                    if not found:
                        found_all = False
                        break

                if found_all:
                    g.write("1\n")
                else:
                    g.write("0\n")

    def run_v3(self):
        with open('input.txt') as f, open('output.txt', 'w') as g:
            w1 = f.readline().rstrip()
            w2 = f.readline().rstrip()

            if len(w1) != len(w2):
                g.write("0\n")
            else:
                l = len(w1)
                m1 = {}
                m2 = {}
                for i in range(l):
                    v1 = m1.get(w1[i], 0)
                    m1[w1[i]] = v1 + 1

                    v2 = m2.get(w2[i], 0)
                    m2[w2[i]] = v2 + 1

                if m1 == m2:
                    g.write("1\n")
                else:
                    g.write("0\n")

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

    def test1(self):
        test_case_data = {
            "input":
                "zprl\n" +
                "zprc\n"
            ,
            "output": "0\n"
        }

        TestCaseRunner.run_test_case(self, SolutionScript(), test_case_data)

    def test3(self):
        def rand_str(n):
            return ''.join([random.choice(string.ascii_lowercase) for i in range(n)])

        # Now to generate a random string of length 10
        s = rand_str(1000)
        test_case_data = {
            "input":
                s+"\n" +
                s+"\n"
            ,
            "output": "1\n"
        }

        TestCaseRunner.run_test_case(self, SolutionScript(), test_case_data)

    def test4(self):
        test_case_data = {
            "input":
                "evyfdfqopblkknapoffvngtzuzggquaasgxvsnluqueiobemsqlgzhkwoxohutycawlvipxdbupsbxfdnuflhtfbqvvtagjsbxbpecnmawacjcxyldwrgdqtejxmldstlfewwuajkqzelakiachndvwwuygxuxnjwayxykiinpnhpotavkulgqkoiuzqecvwhlsklbqiogdapqdxywzhewezvjbdgjcggadvnpojhrzqirmskxhqxpchibmwzufqsxwmnzgezfbpgferldtketjxbhkfqplkgtysgibxgfysrikyitnsqrsryxptabdippfwtxorltmvtwkmhxalkqzjrpnpgytiqsdyvolfndywwgpmojtisuyrbhdjdgqwvbwmiyjospfmufgduhjypvcueevpudjrnhxwggupffllltvjiiukfhxhkpnriiinjhgeflwfipshnlrhphuamvshsdktyzbtyufgzffuwuhggzgxphetzszerjccaqivoibiyshjubommtjpelfvjbgvfwajgqksndoyjikofolnveadsnbhyqtrlucgalbtghkrxhkwndmwvwoezeypwcbpchpapzatdwktteuknsnhrhpvmrzorjsqljhllskyhtwxsfnawbatuivxvnqznvlotnnymhjunetcgfynaghhdbtqgrqnhhmvkjfnailoaymtsoxpxbnsjturuzpndakoxygbjgczpffruiwjlbpiyolkokakrgdzumhxpqdmztwicdimkcnotqferuhegilbpypcashanlpryjwepamvqnucojkkmmxndwwtahromhzgddshbjpdjkbsoflpnfdkukuqelkocrzymwgjrijsbdunyvyzfmudfxyuqyqlchzqnuvgymrsrezndisbvhqernptrplmhqhzkxtiogjffqpomwtmbarrwsrephcapnrdizszohsaoopvxpkepyydwrzlhiyudkraeicm\n" +
                "flwfipshnlrhphuamvshsdktyzbtyufgzffuwuhggzgxphetzszerjccaqivoibiyshjubommtjpelfvjbgvfwajgqksndoyjikofolnveadsnbhyqtrlucgalbtghkrxhkwndmwvwoezeypwcbpchpapzatdwktteuknsnhrhpvmrzorjsqljhllskyhtwxsfnawbatuivxvnqznvlotnnymhjunetcgfynaghhdbtqgrqnhhmvkjfnailoaymtsoxpxbnsjturuzpndakoxygbjgczpffruiwjlbpiyolkokakrgdzumhxpqdmztwicdimkcnotqferuhegilbpypcashanlpryjwepamvqnucojkkmmxndwwtahromhzgddshbjpdjkbsoflpnfdkukuqelkocrzymwgjrijsbdunyvyzfmudfxyuqyqlchzqnuvgymrsrezndisbvhqernptrplmhqhzkxtiogjffqpomwtmbarrwsrephcapnrdizszohsaoopvxpkepyydwrzlhiyudkraeicmevyfdfqopblkknapoffvngtzuzggquaasgxvsnluqueiobemsqlgzhkwoxohutycawlvipxdbupsbxfdnuflhtfbqvvtagjsbxbpecnmawacjcxyldwrgdqtejxmldstlfewwuajkqzelakiachndvwwuygxuxnjwayxykiinpnhpotavkulgqkoiuzqecvwhlsklbqiogdapqdxywzhewezvjbdgjcggadvnpojhrzqirmskxhqxpchibmwzufqsxwmnzgezfbpgferldtketjxbhkfqplkgtysgibxgfysrikyitnsqrsryxptabdippfwtxorltmvtwkmhxalkqzjrpnpgytiqsdyvolfndywwgpmojtisuyrbhdjdgqwvbwmiyjospfmufgduhjypvcueevpudjrnhxwggupffllltvjiiukfhxhkpnriiinjhge\n"
            ,
            "output": "1\n"
        }

        TestCaseRunner.run_test_case(self, SolutionScript(), test_case_data)

