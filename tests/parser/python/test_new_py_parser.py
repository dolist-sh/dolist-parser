import pytest
from os import getcwd
from src.parsers.new_py import PYParser

pwd = getcwd()

PY_ONELINE_PATTERN = r"#"
PY_MULTILINE_PATTERN = r'(\""")'

py_parser = PYParser(PY_ONELINE_PATTERN, PY_MULTILINE_PATTERN)


def test_py_parser():
    """Should parse 6 to-dos from the file"""
    result = py_parser.parse(f"{pwd}/tests/parser/python/src/python.py")

    assert len(result) == 6
