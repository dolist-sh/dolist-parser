import re
import typing


PY_INLINE_COMMENT_PATTERN = "^//"


def _is_todo_comment(input: str) -> bool:
    result = False

    input = input.split()

    i = 0

    # Find trace of todo in first
    while i <= 3:
        if re.search("TODO", input[i], re.IGNORECASE) is not None:
            result = True
            break

        i += 1

    return result


with open("input/index.ts", "r") as file:
    for line in file.readlines():

        inline_comment = re.match(PY_INLINE_COMMENT_PATTERN, line)

        if inline_comment is not None:
            print("----------------------------------------")
            print(f"Original text input: {inline_comment.string}")

            result = _is_todo_comment(inline_comment.string)

            print(f"Result is {result}")
            print("----------------------------------------")

            if result is True:
                print("Create data object here")
