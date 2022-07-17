import os
from parser import parse
from definition import ParsedComment
import json
from utils import write_to_json
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


if __name__ == "__main__":

    path = f"{os.getcwd()}/input"
    final_output = run(path)
    write_to_json(json.dumps(final_output))

    print("All done! ✨ 🍰 ✨")
    print(f"Found {len(final_output)} to-dos from the project")
