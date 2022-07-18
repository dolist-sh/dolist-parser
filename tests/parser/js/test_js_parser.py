import pytest
from os import getcwd
from src.parsers.javascript import JSParser

pwd = getcwd()

JS_ONELINE_PATTERN = r"//"
JS_MULTILINE_OPEN_PATTERN = r"/\*"
JS_MULTILINE_CLOSE_PATTERN = r"\*/"

js_parser = JSParser(
    JS_ONELINE_PATTERN, JS_MULTILINE_OPEN_PATTERN, JS_MULTILINE_CLOSE_PATTERN
)


def test_parser_typescript():
    """Should parse 11 to-dos from input file"""
    result = js_parser.parse(f"{pwd}/tests/parser/js/src/typescript.ts")

    assert len(result) == 11


def test_parser_javascript():
    """Should parse 7 to-dos from input file"""
    result = js_parser.parse(f"{pwd}/tests/parser/js/src/javascript.js")

    assert len(result) == 7


# TODO:Add tests for_find_todo_comment call: check if the correct output is returned
# TODO: Add tests for the _find_comment_start_index call
