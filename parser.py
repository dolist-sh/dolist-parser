import re
import json
from typing import Union, List


JS_ONELINE_COMMENT_PATTERN = "//"


def write_to_json(payload: str):
    # TODO: add timestamp to the file name
    with open("output/output.json", "w") as output_file:
        output_file.write(payload)
        output_file.close


def find_todo_comment(comment: str):
    pass


def find_comment_start_index(payload: List[str]):
    result = None

    for (index, value) in enumerate(payload):
        if re.match(f"^{JS_ONELINE_COMMENT_PATTERN}", value, re.IGNORECASE) is not None:
            result = index
            break

    return result


with open("input/index.ts", "r") as file:

    output = []

    for line in file.readlines():

        oneline_comment = re.search(JS_ONELINE_COMMENT_PATTERN, line)

        if oneline_comment is not None:
            content = oneline_comment.string.split()
            comment_start_index = find_comment_start_index(content)

            content = content[comment_start_index:]

            i = 0

            # Find a trace of todo in the first three words
            while i <= 3:
                if re.search("TODO", content[i], re.IGNORECASE) is not None:
                    todo_comment = {
                        "type": "todo",
                        "title": " ".join(content[i + 1 :]),
                    }  # TODO: define the type for this dictionary
                    output.append(todo_comment)
                    break

                i += 1

    write_to_json(json.dumps(output))
