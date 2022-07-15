import re
import json
from os import getcwd
from datetime import datetime
from time import time
from typing import Union, List, Tuple


JS_ONELINE_COMMENT_PATTERN = "//"
JS_MULTILINE_COMMENT_OPEN_PATTERN = "/\*"
JS_MULTILINE_COMMENT_CLOSE_PATTERN = "\*/"


def _get_filepath(path: str) -> str:
    directory = getcwd()
    filepath = path

    if path[0] != "/":
        filepath = f"/{filepath}"

    return f"{directory}{filepath}"


def _write_to_json(payload: str):
    now = datetime.now()
    unix_time = int(time())

    with open(
        f"output/output-{now.year}-{now.month}-{now.day}-{unix_time}.json", "w"
    ) as output_file:
        output_file.write(payload)
        output_file.close


def _find_comment_start_index(payload: List[str]):
    result = None

    for (index, value) in enumerate(payload):
        if re.match(f"^{JS_ONELINE_COMMENT_PATTERN}", value, re.IGNORECASE) is not None:
            result = index
            break

    return result


def _handle_oneline_comment(comment: List[str], line_num: int, file_path: str):
    conment = comment[_find_comment_start_index(comment) :]

    result = None

    i = 0

    # Find a trace of todo in the first three words
    while i <= 3:

        if re.search("TODO", comment[i], re.IGNORECASE) is not None:
            result = {
                "type": "todo",
                "commentStyle": "oneline",
                "title": " ".join(comment[i + 1 :]),
                "fullComment": [" ".join(comment)],
                "path": file_path,
                "lineNumber": line_num,
            }  # TODO: define the type for this dictionary
            break

        i += 1

    return result


def _handle_multiline_comment(comments, file_path: str):

    is_comment_to_parse = False
    title = ""
    comment_index = None

    for e in comments:
        content = e[0].split()

        i = 0

        while (i <= 3) and (i <= len(content) - 1):
            if re.search("TODO", content[i], re.IGNORECASE) is not None:
                # Consider it a todo comment
                # Define a title here

                is_comment_to_parse = True
                title = " ".join(content[i + 1 :])
                comment_index = e[1]
                break

            i += 1

    if is_comment_to_parse is True:

        full_comment = [e[0] for e in comments]

        result = {
            "type": "todo",
            "commentStyle": "multiline",
            "title": title,
            "fullComment": full_comment,
            "path": file_path,
            "lineNumber": comment_index + 1,
        }

        return result
    else:
        return None


def parse(path: str) -> int:
    full_path = _get_filepath(path)

    with open(full_path, "r") as file:
        output = []

        in_multiline_comment = False
        multiline_counter = 0
        is_comment_to_parse = False
        multiline_temp_holder = []
        multiline_index_holder = []

        for index, line in enumerate(file.readlines()):

            oneline_comment = re.search(JS_ONELINE_COMMENT_PATTERN, line)

            if oneline_comment is not None:
                content = oneline_comment.string.split()
                result = _handle_oneline_comment(content, index + 1, path)

                if result is not None:
                    output.append(result)

            else:
                multiline_comment_open = re.search(
                    JS_MULTILINE_COMMENT_OPEN_PATTERN, line
                )
                multiline_comment_close = re.search(
                    JS_MULTILINE_COMMENT_CLOSE_PATTERN, line
                )

                # Handle multiline comments
                if multiline_comment_open is not None:
                    print("------------------------------------------")
                    print("This is the opening of a multiline comment")
                    print(line)

                    in_multiline_comment = True
                    multiline_temp_holder.append((line, index))
                    

                elif in_multiline_comment and multiline_comment_close is None:
                    print("This is the body of the multiline comment")
                    print(line)

                    multiline_counter += 1
                    multiline_temp_holder.append((line, index))

                elif multiline_comment_close is not None:
                    print("This is the closing of a multiline comment")
                    print("------------------------------------------")
                    print(line)

                    # Handle multiline comment here
                    multiline_temp_holder.append((line, index))

                    result = _handle_multiline_comment(multiline_temp_holder, path)

                    print("Multiline parsing result:")
                    print(result)

                    if result is not None:
                        output.append(result)

                    # Reset all temp variables
                    in_multiline_comment = False
                    multiline_counter = 0
                    multiline_temp_holder = []

        _write_to_json(json.dumps(output))

        print("All done! ✨ 🍰 ✨")
        print(f"Found {len(output)} to-dos from comment")
        return len(output)
