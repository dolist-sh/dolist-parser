"""A Module to run parser locally"""

import os
import re

from parsers.javascript import JSParser
from parsers.python import PYParser

from definition import ParsedComment
from typing import List


JS_ONELINE_PATTERN = r"//"
JS_MULTILINE_OPEN_PATTERN = r"/\*"
JS_MULTILINE_CLOSE_PATTERN = r"\*/"

PY_ONELINE_PATTERN = r"#"
PY_MULTILINE_PATTERN = r'(\""")'


js_parser = JSParser(
    JS_ONELINE_PATTERN, JS_MULTILINE_OPEN_PATTERN, JS_MULTILINE_CLOSE_PATTERN
)
py_parser = PYParser(PY_ONELINE_PATTERN, PY_MULTILINE_PATTERN)


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
