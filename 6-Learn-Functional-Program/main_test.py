from main import *

run_cases = [
    (
        "*Don't* panic.\n",
        "Don't panic.\n",
    ),
    (
        "The **answer to the ultimate question** of life, the universe and everything is *42*\n",
        "The answer to the ultimate question of life, the universe and everything is 42\n",
    ),
]

submit_cases = run_cases + [
    (
        "",
        "",
    ),
    (
        "In the beginning the *universe* was created.\nThis has made a lot of people very *angry* and been widely regarded as a bad move.\n",
        "In the beginning the universe was created.\nThis has made a lot of people very angry and been widely regarded as a bad move.\n",
    ),
    (
        "Ford, you're turning into a *penguin*\n",
        "Ford, you're turning into a penguin\n",
    ),
    (
        "*Space* is big.\nYou just won't **believe** how vastly, hugely, mind-bogglingly big it is.\n",
        "Space is big.\nYou just won't believe how vastly, hugely, mind-bogglingly big it is.\n",
    ),
]


def test(input_doc, expected_output):
    print("---------------------------------")
    print(f"Input document:\n{input_doc}")
    print(f"Expected output:\n{expected_output}")
    result = remove_emphasis(input_doc)
    print(f"Actual output:\n{result}")
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