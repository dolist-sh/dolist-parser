import re
from utils import trim_path
from definition import ParsedComment
from typing import List, Union, Tuple


class BaseParser:
    def __init__(
        self, oneline_pattern, multiline_pattern, multiline_close_pattern=None
    ) -> None:
        self.oneline_pattern: str = oneline_pattern
        self.multiline_pattern: str = multiline_pattern
        self.multiline_close_pattern: str = multiline_close_pattern

    # OPTIMIZE: Think about if this is necessary
    def _find_oneline_comment_start_index(self, comment: List[str]) -> Union[int, None]:
        result = None

        for (index, value) in enumerate(comment):
            if re.match(f"^{self.oneline_pattern}", value, re.IGNORECASE) is not None:
                result = index
                break

        return result

    def _get_title(self, comment: List[str], index: int) -> str:

        pattern_to_check = (
            self.multiline_close_pattern
            if (self.multiline_close_pattern is not None)
            else self.multiline_pattern
        )

        # Remove the closing pattern if it's part of the title
        if re.search(pattern_to_check, comment[-1]) is not None:
            return " ".join(comment[index + 1 : -1]).capitalize()

        return " ".join(comment[index + 1 :]).capitalize()

    def _handle_oneline_comment(
        self, comment: List[str], line_num: int, file_path: str
    ) -> Union[ParsedComment, None]:
        comment = comment[self._find_oneline_comment_start_index(comment) :]
        result = None

        comment_length = len(comment)
        counter = 3 if (comment_length >= 3) else comment_length

        # Find a trace of todo in the first three words
        i = 0

        while i < counter:

            if re.search("TODO", comment[i], re.IGNORECASE) is not None:
                result = ParsedComment(
                    type="TODO",
                    commentStyle="oneline",
                    title=self._get_title(comment, i),
                    fullComment=[" ".join(comment)],
                    path=file_path,  # TODO: trim_path should be called when running on fs
                    lineNumber=line_num,
                )
                break

            i += 1

        return result

    def _handle_multiline_comment(
        self, comments: List[Tuple[str, int]], file_path: str
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
                    title = self._get_title(comment, i)
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
        pass
