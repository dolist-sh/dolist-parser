import os
from parsers.js import parse
from definition import ParsedComment
from typing import List


def run(path: str) -> List[ParsedComment]:
    output = []

    def inspect_source(path: str) -> List[ParsedComment]:
        result = []
        dir_list = os.listdir(path)

        for content in dir_list:
            current_path = f"{path}/{content}"

            if (os.path.isdir(current_path)) is True:
                inspect_source(current_path)
            else:
                result = result + parse(current_path)

        return output.extend(result)

    inspect_source(path)

    return output
