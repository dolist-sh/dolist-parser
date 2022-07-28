import pytest
from os import getcwd
from dolistparser import js_gh_parser

pwd = getcwd()


def test_parser_typescript():
    """Should parse 11 to-dos from input file"""
    path = f"{pwd}/tests/parser/js_gh/src/typescript.ts"

    with open(path, "r") as file:
        content = file.readlines()
        result = js_gh_parser.parse(content, "/js_gh/src/typescript.ts")

        assert len(result) == 11


def test_parser_javascript():
    """Should parse 7 to-dos from input file"""
    path = f"{pwd}/tests/parser/js_gh/src/javascript.js"

    with open(path, "r") as file:
        content = file.readlines()
        result = js_gh_parser.parse(content, "/js_gh/src/javascript.js")

        print(result)

        assert len(result) == 7


# TODO:Add tests for_find_todo_comment call: check if the correct output is returned
# TODO: Add tests for the _find_comment_start_index call
