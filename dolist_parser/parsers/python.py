import re
from parsers.base import BaseParser
from definition import ParsedComment
from typing import List


class PYParser(BaseParser):
    def parse(self, path: str) -> List[ParsedComment]:

        with open(path, "r") as file:
            output = []

            # Variables to hold temp data for checking multiline comments
            in_multiline_comment = False
            multiline_temp_holder = []

            for index, line in enumerate(file.readlines()):

                oneline_comment = re.search(self.oneline_pattern, line)

                if oneline_comment is not None:
                    """Handle one-line comments"""
                    content = oneline_comment.string.split()
                    result = self._handle_oneline_comment(content, index + 1, path)

                    if result is not None:
                        output.append(result)
                else:

                    multiline_comment = re.search(self.multiline_pattern, line)

                    if multiline_comment is not None:
                        """Handle multiline comments"""

                        content = multiline_comment.string.split()

                        pattern_in_first_word = re.search(
                            self.multiline_pattern, content[0]
                        )
                        pattern_in_last_word = re.search(
                            self.multiline_pattern, content[-1]
                        )

                        if (
                            (pattern_in_first_word is not None)
                            and (pattern_in_last_word is not None)
                            and (len(content) > 1)
                        ):

                            """Handle the oneline comment with docstring"""
                            result = self._handle_oneline_comment(
                                content, index + 1, path
                            )

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
                                result = self._handle_multiline_comment(
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
