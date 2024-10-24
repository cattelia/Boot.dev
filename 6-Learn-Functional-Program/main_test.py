from plugins import *
from decorators import *

run_cases = [
    (
        configure_backups,
        [
            ("path", "~/documents"),
            ("extension", ".md"),
        ],
        {
            "path": "~/documents",
            "prefix": "copy_",
            "extension": ".md",
        },
    ),
    (
        configure_login,
        [
            ("user", "goku_fanatic"),
            ("password", "kakarot1989"),
        ],
        {
            "user": "goku_fanatic",
            "password": "kakarot1989",
            "token": None,
        },
    ),
]

submit_cases = run_cases + [
    (
        configure_backups,
        [
            ("path", "~/workspace/backups"),
            ("prefix", "backup_"),
        ],
        {
            "path": "~/workspace/backups",
            "prefix": "backup_",
            "extension": ".txt",
        },
    ),
    (
        configure_login,
        [
            ("user", "john_q_sample"),
            ("password", "p@$$w0rd"),
            ("token", "a09adc-0914sf-012la9-fa3sa0-2342ra"),
        ],
        {
            "user": "john_q_sample",
            "password": "p@$$w0rd",
            "token": "a09adc-0914sf-012la9-fa3sa0-2342ra",
        },
    ),
]


def test(func, args, expected_output):
    print("---------------------------------")
    print(f"Function: {func.__name__}")
    print("Positional Arguments:")
    for arg in args:
        print(f" * {arg}")
    print(f"Expecting:")
    print(expected_output)
    result = func(*args)
    print(f"Actual:")
    print(result)
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