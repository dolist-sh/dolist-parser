import pytest
from os import getcwd
from src.parser import parse

pwd = getcwd()


def test_parser_typescript():
    """Should parse 11 to-dos from input file"""
    result = parse(f"{pwd}/tests/parser/data/typescript.ts")

    assert len(result) == 11


def test_parser_javascript():
    """Should parse 7 to-dos from input file"""
    result = parse(f"{pwd}/tests/parser/data/javascript.js")

    assert len(result) == 7


# TODO:Add tests for_find_todo_comment call: check if the correct output is returned
# TODO: Add tests for the _find_comment_start_index call
