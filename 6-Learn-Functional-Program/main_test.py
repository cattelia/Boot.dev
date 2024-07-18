from main import sum_nested_list

run_cases = [
    ([1, 2, [3, 4]], 10),
    ([5, [6, 7], [[8, 9], 10]], 45),
]

submit_cases = run_cases + [
    ([], 0),
    ([1, [2], [3, [4, [5, [6, [7, [8, [9, [10]]]]]]]]], 55),
]


def test(input_list, expected_output):
    print("---------------------------------")
    print(f"Input list: {input_list}")
    print(f"Expected output: {expected_output}")
    result = sum_nested_list(input_list)
    print(f"Actual output: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()