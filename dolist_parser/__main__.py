import re
import os
import json

from dolist_parser import js_parser, py_parser
from utils import write_to_json

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
                parsed = []

                if re.search(r"(\.js$|\.ts$)", content, re.IGNORECASE):
                    parsed = js_parser.parse(current_path)

                if re.search(r"(\.py$)", content, re.IGNORECASE):
                    parsed = py_parser.parse(current_path)

                result = result + parsed

        return output.extend(result)

    inspect_source(path)

    return output


if __name__ == "__main__":

    path = f"{os.getcwd()}/input"
    final_output = run(path)
    write_to_json(json.dumps(final_output))

    print("All done! ✨ 🍰 ✨")
    print(f"Found {len(final_output)} to-dos from the project")
