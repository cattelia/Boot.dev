from main import *


run_cases = [
    (
        "#",
        3,
        """###
@##
$$$
###""",
        2,
    ),
    (
        "$",
        2,
        """$$$
$
***
@@@
$$
$$$""",
        3,
    ),
]

submit_cases = run_cases + [
    ("%", 1, "", 0),
    (
        "*",
        3,
        """***
*
$$$$$$
xxx
****
***
***""",
        4,
    ),
]


def test(char, length, doc, expected_output):
    print("---------------------------------")
    print(f"Input char: {char}")
    print(f"Input length: {length}")
    print(f"Input doc:")
    print(doc)
    print(f"Expecting: {expected_output}")
    num_lines = lines_with_sequence(char)(length)(doc)
    print(f"Actual: {num_lines}")
    if num_lines == expected_output:
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
