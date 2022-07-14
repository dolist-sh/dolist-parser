import re
import json
from typing import Union, List


JS_ONELINE_COMMENT_PATTERN = "//"


def _write_to_json(payload: str):
    # TODO: add timestamp to the file name
    with open("output/output.json", "w") as output_file:
        output_file.write(payload)
        output_file.close


def _find_comment_start_index(payload: List[str]):
    result = None

    for (index, value) in enumerate(payload):
        if re.match(f"^{JS_ONELINE_COMMENT_PATTERN}", value, re.IGNORECASE) is not None:
            result = index
            break

    return result


def _find_todo_comment(payload: List[str]):
    output = None

    i = 0

    # Find a trace of todo in the first three words
    while i <= 3:

        if re.search("TODO", payload[i], re.IGNORECASE) is not None:
            output = {
                "type": "todo",
                "title": " ".join(payload[i + 1 :]),
            }  # TODO: define the type for this dictionary
            break

        i += 1

    return output


def parse(path: str) -> int:  # TODO: Make this function take the path to file
    with open(path, "r") as file:
        output = []

        for line in file.readlines():

            oneline_comment = re.search(JS_ONELINE_COMMENT_PATTERN, line)

            if oneline_comment is not None:
                content = oneline_comment.string.split()
                content = content[_find_comment_start_index(content):]

                todo_comment = _find_todo_comment(content)

                if todo_comment is not None:
                    output.append(todo_comment)

        _write_to_json(json.dumps(output))

        print("All done! ✨ 🍰 ✨")
        print(f"Found {len(output)} to-dos from comment")
        return len(output)
