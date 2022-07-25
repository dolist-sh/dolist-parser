""" Export language parsers """

from parsers.javascript import JSParser
from parsers.python import PYParser

JS_ONELINE_PATTERN = r"//"
JS_MULTILINE_OPEN_PATTERN = r"/\*"
JS_MULTILINE_CLOSE_PATTERN = r"\*/"

PY_ONELINE_PATTERN = r"#"
PY_MULTILINE_PATTERN = r'(\""")'

js_parser = JSParser(
    JS_ONELINE_PATTERN, JS_MULTILINE_OPEN_PATTERN, JS_MULTILINE_CLOSE_PATTERN
)
py_parser = PYParser(PY_ONELINE_PATTERN, PY_MULTILINE_PATTERN)
