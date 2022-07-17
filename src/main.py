import os
from parsers.js import parse
from definition import ParsedComment
from typing import List


def run(path: str) -> List[ParsedComment]:
    output = []

    def inspect_source(path: str) -> List[ParsedComment]:
        result = []
        dir_list = os.listdir(path)

        # print("-------------------")
        # print(f"Start inspecting")
        # print(dir_list)

        for content in dir_list:
            current_path = f"{path}/{content}"
            # print(f"Current path: {current_path}")

            if (os.path.isdir(current_path)) is True:
                # print(f"Calling itself again for a folder: {current_path}")
                inspect_source(current_path)
            else:
                # print(f"Calling parse for a file: {current_path}")
                result = result + parse(current_path)

        # print("--------------------------------------------")
        # print("inspect_func call being returned")
        # print(f"Output length being returned: {len(result)}")
        # print("--------------------------------------------")

        return output.extend(result)

    inspect_source(path)

    return output
