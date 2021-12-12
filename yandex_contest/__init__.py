import os
from abc import ABC, abstractmethod
import time


class SolutionScriptAbs(ABC):

    @abstractmethod
    def run(self):
        pass


class TestCaseRunner():

    @staticmethod
    def run_test_case(test_case, ss, test_case_data):
        print("input:\n" + test_case_data["input"])
        print("output:\n" + test_case_data["output"])

        with open("input.txt", 'w') as f:
            input_data = test_case_data['input']
            f.write(input_data)

        start_time = time.time()
        ss.run()
        print(f"Exec time: {(time.time() - start_time)*1000} ms")

        with open("output.txt") as g:
            output_expected = test_case_data['output']
            output_actual = g.read()

            test_case.assertEqual(output_expected, output_actual)

        os.remove("input.txt")
        os.remove("output.txt")