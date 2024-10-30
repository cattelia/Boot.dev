from main import *

run_cases = [
    (
        "aibohphobia",
        True,
    ),
    (
        "eve",
        True,
    ),
    (
        "level",
        True,
    ),
    (
        "tat",
        True,
    ),
    (
        "rotator",
        True,
    ),
    (
        "potato",
        False,
    ),
]


submit_cases = run_cases + [
    (
        "",
        True,
    ),
    (
        "a",
        True,
    ),
    (
        "apple",
        False,
    ),
    (
        "redivider",
        True,
    ),
    (
        "divide",
        False,
    ),
    (
        "kayak",
        True,
    ),
]


def is_lru_cache_imported_from_functools():
    func_name = "lru_cache"
    module_name = "functools"
    return (
        func_name in globals()
        and callable(globals()[func_name])
        and globals()[func_name].__module__ == module_name
    ) or module_name in globals()


def test(input, expected_output):
    print("---------------------------------")
    print(f"Input: '{input}'")
    print(f"Expecting: {expected_output}")
    result = is_palindrome(input)
    print(f"   Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    print("---------------------------------")
    if is_lru_cache_imported_from_functools():
        print("lru_cache was imported from functools")
        print("Pass")
        passed = 1
    else:
        failed = 1
        print("lru_cache was not imported from functools")
        print("Fail")
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
