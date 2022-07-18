import os
from src.parsers.javascript import parse
from src.definition import ParsedComment
from typing import List

# TODO: This should be parsed


def run(path: str) -> List[ParsedComment]:
    output = []  # This should not be parsed

    def inspect_source(path: str) -> List[ParsedComment]:
        """inspect_source is a recursive function"""
        result = []
        dir_list = os.listdir(path)

        for content in dir_list:
            current_path = f"{path}/{content}"

            if (os.path.isdir(current_path)) is True:
                inspect_source(current_path)  # TODO: This should be parsed
            else:
                result = result + parse(current_path)
                """TODO: This should be parsed"""

        return output.extend(result)

    """ TODO:
    This is multiline comment
    This should be parsed
    """

    inspect_source(path)

    """
    This is multiline comment
    This should not be parsed
    """

    return output


"""
This is multiline comment
TODO: This should be parsed
"""

"""
This is multiline comment
TODO: This should be parsed"""

"""
This is multiline comment
This should not be parsed"""

# This file should parse 6 to-do comments
