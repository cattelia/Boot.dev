from main import *

run_cases = [
    (
        ["The Grand Budapest Hotel", "Fantastic Mr. Fox", "Moonrise Kingdom"],
        [8.1, 7.9, 7.8],
        {
            "The Grand Budapest Hotel": 8.1,
            "Fantastic Mr. Fox": 7.9,
            "Moonrise Kingdom": 7.8,
        },
    ),
    (
        ["The Royal Tenenbaums", "The Life Aquatic with Steve Zissou", "Isle of Dogs"],
        [7.6, 7.3, 7.9],
        {
            "The Royal Tenenbaums": 7.6,
            "The Life Aquatic with Steve Zissou": 7.3,
            "Isle of Dogs": 7.9,
        },
    ),
]

submit_cases = run_cases + [
    ([], [], {}),
    ([""], [], {}),
    ([], [0.0], {}),
    (
        [
            "Rushmore",
            "The Darjeeling Limited",
            "The French Dispatch",
            "The Wonderful Story of Henry Sugar and Three More",
        ],
        [7.7, 7.2, 7.4],
        {
            "Rushmore": 7.7,
            "The Darjeeling Limited": 7.2,
            "The French Dispatch": 7.4,
        },
    ),
    (
        ["Bottle Rocket", "Asteroid City", "The Grand Budapest Hotel"],
        [7.0, 7.6, 8.1, 0.0],
        {
            "Bottle Rocket": 7.0,
            "Asteroid City": 7.6,
            "The Grand Budapest Hotel": 8.1,
        },
    ),
]


def print_dict(d):
    for key, value in d.items():
        print(f" * {key}: {value}")


def test(keys, values, expected_output):
    print("---------------------------------")
    print(f"Inputs: {keys}, {values}")
    print("Expecting:")
    print_dict(expected_output)
    result = zipmap(keys, values)
    print("Actual:")
    print_dict(result)
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
