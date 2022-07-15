import re
import json
from utils import get_filepath, write_to_json

from definition import ParsedComment
from typing import Union, List, Tuple


JS_ONELINE_PATTERN = "//"
JS_MULTILINE_OPEN_PATTERN = "/\*"
JS_MULTILINE_CLOSE_PATTERN = "\*/"

# Think about if this is necessary
def _find_oneline_comment_start_index(payload: List[str]) -> Union[int, None]:
    result = None

    for (index, value) in enumerate(payload):
        if re.match(f"^{JS_ONELINE_PATTERN}", value, re.IGNORECASE) is not None:
            result = index
            break

    return result


def _handle_oneline_comment(
    comment: List[str], line_num: int, file_path: str
) -> Union[ParsedComment, None]:
    conment = comment[_find_oneline_comment_start_index(comment) :]
    result = None

    # Find a trace of todo in the first three words
    i = 0

    while i <= 3:

        if re.search("TODO", comment[i], re.IGNORECASE) is not None:
            result = ParsedComment(
                type="TODO",
                commentStyle="oneline",
                title=" ".join(comment[i + 1 :]),
                fullComment=[" ".join(comment)],
                path=file_path,
                lineNumber=line_num,
            )
            break

        i += 1

    return result


def _handle_multiline_comment(comments, file_path: str) -> Union[ParsedComment, None]:
    title = ""
    comment_at_index = None
    comment_to_parse = False

    for e in comments:
        content = e[0].split()

        i = 0

        while (i <= 3) and (i <= len(content) - 1):

            if re.search("TODO", content[i], re.IGNORECASE) is not None:
                comment_to_parse = (
                    True  # Flag that this multiline comment is a TODO comment
                )
                title = " ".join(content[i + 1 :])
                comment_at_index = e[1]
                break

            i += 1

    # Interprete the result from the above loop

    result = None

    if comment_to_parse is True:

        full_comment = [e[0] for e in comments]

        result = ParsedComment(
            type="TODO",
            commentStyle="multiline",
            title=title,
            fullComment=full_comment,
            path=file_path,
            lineNumber=comment_at_index + 1,
        )

    return result


def parse(path: str) -> int:
    full_path = get_filepath(path)

    with open(full_path, "r") as file:
        output = []

        # Variables to hold temp data for checking multiline comments
        in_multiline_comment = False
        multiline_temp_holder = []

        for index, line in enumerate(file.readlines()):

            """Looking for one-line comments"""
            oneline_comment = re.search(JS_ONELINE_PATTERN, line)

            if oneline_comment is not None:
                content = oneline_comment.string.split()
                result = _handle_oneline_comment(content, index + 1, path)

                if result is not None:
                    output.append(result)

            else:
                """Looking for multi-line comments"""

                # fmt: off
                multiline_comment_open = re.search(JS_MULTILINE_OPEN_PATTERN, line)
                multiline_comment_close = re.search(JS_MULTILINE_CLOSE_PATTERN, line)
                # fmt: on

                if multiline_comment_open is not None:
                    in_multiline_comment = True
                    multiline_temp_holder.append((line, index))

                elif (in_multiline_comment and multiline_comment_close is None):
                    multiline_temp_holder.append((line, index))

                elif multiline_comment_close is not None:
                    multiline_temp_holder.append((line, index))
                    result = _handle_multiline_comment(multiline_temp_holder, path)

                    if result is not None:
                        output.append(result)

                    # Reset all temp variables
                    in_multiline_comment = False
                    multiline_temp_holder = []

        write_to_json(json.dumps(output))

        print("All done! ✨ 🍰 ✨")
        print(f"Found {len(output)} to-dos from comment")
        return len(output)
