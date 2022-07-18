import pytest
from os import getcwd
from src.parsers.py import parse

pwd = getcwd()


def test_py_parser():
    """Should parse 6 to-dos from the file"""
    result = parse(f"{pwd}/tests/parser/python/src/python.py")

    assert len(result) == 6
