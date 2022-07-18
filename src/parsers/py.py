import re
import json
from utils import write_to_json
from definition import ParsedComment
from typing import List, Union

PY_ONELINE_PATTERN = r"#"

PY_MULTILINE_OPEN_PATTERN = r"(^\"" ")"  # TODO: double check if this is right
PY_MULTILINE_CLOSE_PATTERN = r"(\"" ")&"  # TODO: double check if this is right

# OPTIMIZE: Think about if this is necessary
def _find_oneline_comment_start_index(payload: List[str]) -> Union[int, None]:
    result = None

    for (index, value) in enumerate(payload):
        if re.match(f"^{PY_ONELINE_PATTERN}", value, re.IGNORECASE) is not None:
            result = index
            break

    return result


def _get_title(comment: List[str], index: int) -> str:
    print("TODO is at the index: " + str(index))
    # Remove the closing pattern if it's part of the title
    # if re.search(JS_MULTILINE_CLOSE_PATTERN, comment[-1]) is not None:
    #    return " ".join(comment[index + 1 : -1]).capitalize()

    return " ".join(comment[index + 1 :]).capitalize()


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
                title=_get_title(comment, i),
                fullComment=[" ".join(comment)],
                path=file_path,
                lineNumber=line_num,
            )
            break

        i += 1

    return result


def parse(path: str) -> List[ParsedComment]:

    with open(path, "r") as file:
        output = []

        for index, line in enumerate(file.readlines()):
            oneline_comment = re.search(PY_ONELINE_PATTERN, line)

            if oneline_comment is not None:
                """Handle one-line comments"""
                content = oneline_comment.string.split()
                result = _handle_oneline_comment(content, index + 1, path)

                if result is not None:
                    output.append(result)

        print("-----------------------------")
        print(f"Parsed {path}! ✨ 🍰 ✨")
        print(f"Found {len(output)} to-dos")
        print("-----------------------------")
        write_to_json(json.dumps(output))
        return output
