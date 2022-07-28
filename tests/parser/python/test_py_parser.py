import pytest
from os import getcwd
from dolistparser import py_parser

pwd = getcwd()

def test_py_parser():
    """Should parse 6 to-dos from the file"""
    result = py_parser.parse(f"{pwd}/tests/parser/python/src/python.py")

    assert len(result) == 6
