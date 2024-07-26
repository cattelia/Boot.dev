from main import *

run_cases = [
    (
        capitalize_content,
        "sample.txt",
        "I really don't feel like screaming today.",
        ["txt", "md", "doc"],
        "I REALLY DON'T FEEL LIKE SCREAMING TODAY.",
    ),
    (
        reverse_content,
        "testing.doc",
        "This is probably how they write in the red room in Twin Peaks...",
        ["txt", "md", "doc"],
        "...skaeP niwT ni moor der eht ni etirw yeht woh ylbaborp si sihT",
    ),
]

submit_cases = run_cases + [
    (
        capitalize_content,
        "test.docx",
        "Okay actually I do feel like screaming today.",
        ["txt", "md", "doc"],
        "Invalid file format",
    ),
    (
        reverse_content,
        "end.ppt",
        "Cherry pie and coffee anyone?",
        ["txt", "md", "doc"],
        "Invalid file format",
    ),
    (
        capitalize_content,
        "sample.doc",
        "I really do feel like eating today.",
        ["txt", "md", "doc"],
        "I REALLY DO FEEL LIKE EATING TODAY.",
    ),
    (
        reverse_content,
        "testing.md",
        "The owls are not what they seem.",
        ["txt", "md", "doc"],
        ".mees yeht tahw ton era slwo ehT",
    ),
]


def test(conversion_func, filename, doc_content, valid_formats, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * conversion_func: {conversion_func.__name__}")
    print(f" * filename: {filename}")
    print(f" * doc_content: {doc_content}")
    print(f" * valid_formats: {valid_formats}")
    print(f"Expecting: {expected_output}")
    try:
        result = doc_format_checker_and_converter(conversion_func, valid_formats)(
            filename, doc_content
        )
    except Exception as e:
        result = str(e)
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
