import re
import json
import typing


PY_INLINE_COMMENT_PATTERN = "^//"


def write_to_json(payload: str):
    # TODO: add timestamp to the file name
    with open("output/output.json", "w") as output_file:
        output_file.write(payload)
        output_file.close


with open("input/index.ts", "r") as file:
    output = []

    for line in file.readlines():
        inline_comment = re.match(PY_INLINE_COMMENT_PATTERN, line)

        if inline_comment is not None:

            content = inline_comment.string.split()
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
