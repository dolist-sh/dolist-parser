import pytest
from os import getcwd
from dolistparser import py_gh_parser

pwd = getcwd()


def test_py_parser():
    """Should parse 6 to-dos from the file"""
    path = f"{pwd}/tests/parser/py_gh/src/python.py"

    with open(path, "r") as file:
        content = file.readlines()
        result = py_gh_parser.parse(content, "/py_gh/src/python.py")

        assert len(result) == 6
