import re
from definition import ParsedComment
from typing import List, Union, Tuple

PY_ONELINE_PATTERN = r"#"
PY_MULTILINE_PATTERN = r'(\""")'

# OPTIMIZE: Think about if this is necessary
def _find_oneline_comment_start_index(payload: List[str]) -> Union[int, None]:
    result = None

    for (index, value) in enumerate(payload):
        if re.match(f"^{PY_ONELINE_PATTERN}", value, re.IGNORECASE) is not None:
            result = index
            break

    return result


def _get_title(comment: List[str], index: int) -> str:
    # Remove the closing pattern if it's part of the title
    if re.search(PY_MULTILINE_PATTERN, comment[-1]) is not None:
        return " ".join(comment[index + 1 : -1]).capitalize()

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


def _handle_multiline_comment(
    comments: List[Tuple[str, int]], file_path: str
) -> Union[ParsedComment, None]:
    title = ""
    comment_at_index = None
    comment_to_parse = False

    for e in comments:
        comment = e[0].split()

        i = 0

        while (i <= 3) and (i <= len(comment) - 1):
            if re.search("TODO", comment[i], re.IGNORECASE) is not None:
                comment_to_parse = True  # flag for further processing
                title = _get_title(comment, i)
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


def parse(path: str) -> List[ParsedComment]:

    with open(path, "r") as file:
        output = []

        # Variables to hold temp data for checking multiline comments
        in_multiline_comment = False
        multiline_temp_holder = []

        for index, line in enumerate(file.readlines()):

            oneline_comment = re.search(PY_ONELINE_PATTERN, line)

            if oneline_comment is not None:
                """Handle one-line comments"""
                content = oneline_comment.string.split()
                result = _handle_oneline_comment(content, index + 1, path)

                if result is not None:
                    output.append(result)
            else:

                multiline_comment = re.search(PY_MULTILINE_PATTERN, line)

                if multiline_comment is not None:
                    """Handle multiline comments"""

                    content = multiline_comment.string.split()

                    pattern_in_first_word = re.search(PY_MULTILINE_PATTERN, content[0])
                    pattern_in_last_word = re.search(PY_MULTILINE_PATTERN, content[-1])

                    if (
                        (pattern_in_first_word is not None)
                        and (pattern_in_last_word is not None)
                        and (len(content) > 1)
                    ):

                        """Handle the oneline comment with docstring"""
                        result = _handle_oneline_comment(content, index + 1, path)

                        if result is not None:
                            output.append(result)
                    else:
                        """Handle the line that either start or end the multiline comment"""

                        multiline_temp_holder.append((line, index))

                        if in_multiline_comment is True:
                            """
                            When in_multiline_comment was set True in previous iteration,
                            This means the current line is the end of multiline comment
                            """
                            result = _handle_multiline_comment(
                                multiline_temp_holder, path
                            )

                            if result is not None:
                                output.append(result)

                            # Reset all temp variables
                            in_multiline_comment = False
                            multiline_temp_holder = []

                        else:
                            in_multiline_comment = not in_multiline_comment

                else:
                    """This section handles the regular comment lines without docstring"""

                    if in_multiline_comment is True:
                        """The current line is part of the multiline comment"""
                        multiline_temp_holder.append((line, index))

        print("-----------------------------")
        print(f"Parsed {path}! ✨ 🍰 ✨")
        print(f"Found {len(output)} to-dos")
        print("-----------------------------")
        return output
