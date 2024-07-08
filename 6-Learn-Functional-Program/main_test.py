from main import *

run_cases = [
    (
        "You can't spell America without Erica",
        "YOU CAN'T SPELL AMERICA WITHOUT ERICA...",
    ),
    ("Friends don't lie.", "FRIENDS DON'T LIE..."),
    (" She's our friend and she's crazy!", "SHE'S OUR FRIEND AND SHE'S CRAZY!..."),
]

submit_cases = run_cases + [
    (" You're gonna slay 'em dead, Nance. ", "YOU'RE GONNA SLAY 'EM DEAD, NANCE..."),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Input: {input}")
    print(f"Expected: {expected_output}")
    result = format_line(input)
    print(f"Actual: {result}")
    if result != expected_output:
        print("Fail")
        return False
    print("Pass")
    return True


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