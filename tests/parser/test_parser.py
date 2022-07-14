import pytest
from os import getcwd

from src.parser import parse


def test_parser_typescript():
    """Should parse 8 to-dos from input file"""
    pwd = getcwd()
    result = parse(f"{pwd}/tests/parser/data/typescript.ts")

    assert result == 8


def test_parser_javascript():
    """Should parse 3 to-dos from input file"""
    pwd = getcwd()
    result = parse(f"{pwd}/tests/parser/data/javascript.js")

    assert result == 3


# TODO:Add tests for_find_todo_comment call: check if the correct output is returned
# TODO: Add tests for the _find_comment_start_index call
