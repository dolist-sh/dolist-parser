import pytest
from src.parser import parse


def test_parser_typescript():
    """Should parse 8 to-dos from input file"""
    result = parse("/tests/parser/data/typescript.ts")

    assert result == 11


def test_parser_javascript():
    """Should parse 3 to-dos from input file"""
    result = parse("/tests/parser/data/javascript.js")

    assert result == 7


# TODO:Add tests for_find_todo_comment call: check if the correct output is returned
# TODO: Add tests for the _find_comment_start_index call
