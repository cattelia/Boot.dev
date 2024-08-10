from main import *

run_cases = [
    (
        [
            "Welcome to the jungle",
            "We've got fun and games",
            "We've got everything you want honey",
        ],
        15,
    )
]

submit_cases = run_cases + [
    (
        [
            "We are the champions my friends",
            "And we'll keep on fighting till the end",
        ],
        14,
    ),
    (
        [
            "I've got another confession to make",
            "I'm your fool",
            "Everyone's got their chains to break",
            "Holdin' you",
        ],
        17,
    ),
]


def test(inputs, expected_output):
    print("---------------------------------")
    print(f"Input:")
    for x in inputs:
        print(f" * {x}")
    print(f"Expecting: {expected_output}")
    aggregator = word_count_aggregator()

    try:
        for input in inputs:
            result = aggregator(input)
    except Exception as e:
        result = e
    print(f"Actual: {result}")
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
