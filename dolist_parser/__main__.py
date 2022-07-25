import os
import json

from dolist_parser import run
from utils import write_to_json


if __name__ == "__main__":

    path = f"{os.getcwd()}/input"
    final_output = run(path)
    write_to_json(json.dumps(final_output))

    print("All done! ✨ 🍰 ✨")
    print(f"Found {len(final_output)} to-dos from the project")
