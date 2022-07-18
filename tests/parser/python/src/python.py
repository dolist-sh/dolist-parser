import os
from src.parsers.js import parse
from src.definition import ParsedComment
from typing import List

# TODO: This should be parsed


def run(path: str) -> List[ParsedComment]:
    output = []  # This should not be parsed

    def inspect_source(path: str) -> List[ParsedComment]:
        result = []
        dir_list = os.listdir(path)

        for content in dir_list:
            current_path = f"{path}/{content}"

            if (os.path.isdir(current_path)) is True:
                inspect_source(current_path)  # TODO: This should be parsed
            else:
                result = result + parse(current_path)

        return output.extend(result)

    inspect_source(path)

    return output


# This file should parse 2 to-do comments
