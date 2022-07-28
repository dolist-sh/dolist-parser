import re
from parsers.base import BaseParser
from domain.comment import ParsedComment
from typing import List


class JSParserGitHub(BaseParser):
    def parse(self, content: List[str], path: str) -> List[ParsedComment]:

        output = []

        # Variables to hold temp data for checking multiline comments
        in_multiline_comment = False
        multiline_temp_holder = []

        for index, line in enumerate(content):

            # fmt: off
            oneline_comment = re.search(self.oneline_pattern, line)
            multiline_comment_open = re.search(self.multiline_pattern, line)
            multiline_comment_close = re.search(self.multiline_close_pattern, line)
            # fmt: on

            if oneline_comment is not None:
                """Handle one-line comments"""
                content = oneline_comment.string.split()
                result = self._handle_oneline_comment(content, index + 1, path)

                if result is not None:
                    output.append(result)
            # fmt: off
            elif (multiline_comment_open is not None) and (multiline_comment_close is not None):
            # fmt: on
                """Handle one-line comment with multiple comment noation"""
                content = line.split()
                result = self._handle_oneline_comment(content, index + 1, path)

                if result is not None:
                    output.append(result)

            else:
                """Handle multi-line comments"""
                if multiline_comment_open is not None:
                    in_multiline_comment = True
                    multiline_temp_holder.append((line, index))

                elif in_multiline_comment and multiline_comment_close is None:
                    multiline_temp_holder.append((line, index))

                elif multiline_comment_close is not None:
                    multiline_temp_holder.append((line, index))
                    result = self._handle_multiline_comment(multiline_temp_holder, path)

                    if result is not None:
                        output.append(result)

                    # Reset all temp variables
                    in_multiline_comment = False
                    multiline_temp_holder = []

        print("-----------------------------")
        print(f"Parsed {path}! ✨ 🍰 ✨")
        print(f"Found {len(output)} to-dos")
        print("-----------------------------")
        return output
