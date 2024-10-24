import ast
import inspect
import re


def run_test_cases(test_obj, test_cases):
    for idx, case in enumerate(test_cases, 1):
        input = case['Input']
        output = case['Output']

        test_method = get_test_method(test_obj=test_obj)

        res = test_method(**input)
        assert res == output, f"Test {idx} failed: {res} != {output}"

    print("All tests passed!")

def get_test_method(test_obj):
    test_func_name = inspect.getmembers(test_obj.__class__, predicate=inspect.isfunction)[0][0]
    return getattr(test_obj, test_func_name)

def gen_test_cases(*ss: str) -> list[dict]:
    return [gen_test_case(s) for s in ss]


def gen_test_case(s: str) -> dict:
    # Парсим строку, извлекая части Input и Output
    pattern = r'Input:\s*(.*)\s*Output:\s*(.*)'
    match = re.match(pattern, s.strip())

    if not match:
        raise ValueError("Некорректный формат строки")

    input_str, output_str = match.groups()

    # Парсим часть Input
    input_items = input_str.split(',')
    input_dict = {}

    for item in input_items:
        key, value = item.split('=')
        key = key.strip()
        value = ast.literal_eval(value.strip())  # Преобразуем значение в соответствующий тип
        input_dict[key] = value

    # Преобразуем Output в соответствующий тип
    output_value = ast.literal_eval(output_str.strip())

    return {'Input': input_dict, 'Output': output_value}

