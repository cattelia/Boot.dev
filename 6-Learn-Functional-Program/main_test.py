from main import *

run_cases = [
    (0, 10, 3, 0, [9, 0, 0]),
    (0, 12, 0, 1, [12, 46, 0]),
    (1, 100, 33, 2, [100, 0, 2]),
]

submit_cases = run_cases + [
    (0, 0, 0, 0, [0, 0, 0]),
    (1000, 1000, 200, 5, [1000, 200, 5]),
    (0, 10, 0, 2, [10, 46, 1]),
    (5, 2000, 200, 3, [1055, 0, 0]),
]


def test(input1, input2, input3, input4, expected):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" *           mana: {input1}")
    print(f" *       max_mana: {input2}")
    print(f" *         energy: {input3}")
    print(f" * energy_potions: {input4}")
    print(
        f"Expecting: mana {expected[0]}, energy {expected[1]}, energy potions {expected[2]}"
    )
    result_mana, result_energy, result_potions = meditate(
        input1, input2, input3, input4
    )
    print(
        f"   Actual: mana {result_mana}, energy {result_energy}, energy potions {result_potions}"
    )
    if (
        result_mana == expected[0]
        and result_energy == expected[1]
        and result_potions == expected[2]
    ):
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
