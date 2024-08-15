from main import *


run_cases = [
    [
        ("Boots", "The Lover of Salmon"),
        ("Superman", "The Big Blue Boyscout"),
        ("Batman", "The Caped Crusader"),
        ("Woman Wonder", ""),
    ],
]


submit_cases = run_cases + [
    [
        ("Green Lantern", "The Man Without Fear"),
        ("AquaMan", "Dweller in the Depths"),
        ("The Flash", "The Crimson Comet"),
        ("The Martian Manhunter", "Mars' Sole Survivor"),
        ("Cyborg", "Tech Titan"),
    ],
]


def test(input_list):
    print("---------------------------------")
    copy_to_clipboard, paste_from_clipboard = new_clipboard({})
    failed = False
    for item in input_list:
        print("Copying to Clipboard:")
        print(f"*   Key: {item[0]}")
        print(f"* Value: {item[1]}")
        copy_to_clipboard(*item)

        print("Pasting From Clipboard:")
        print(f"*      Key: {item[0]}")
        result = paste_from_clipboard(item[0])
        expected_output = item[1]
        print(f"* Expected: {expected_output}")
        print(f"*   Actual: {result}")
        if result != expected_output:
            print("Fail")
            failed = True
        else:
            print("Pass")
        print("---------------------------------")

    # check pasting missing key
    missing_key = "Joker"
    print("Pasting:")
    print(f"* Key: {missing_key}")
    result = paste_from_clipboard(missing_key)
    expected_output = ""
    print(f"* Expected: '{expected_output}'")
    print(f"*   Actual: '{result}'")
    if result != expected_output:
        print("Fail: missing key should return an empty string")
        failed = True
    else:
        print("Pass")

    passed = not failed
    return passed


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(test_case)
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
