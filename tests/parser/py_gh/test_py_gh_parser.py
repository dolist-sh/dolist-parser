import pytest
from os import getcwd
from dolistparser.parsers.python_gh import PYParserGithub

pwd = getcwd()

PY_ONELINE_PATTERN = r"#"
PY_MULTILINE_PATTERN = r'(\""")'

py_parser = PYParserGithub(PY_ONELINE_PATTERN, PY_MULTILINE_PATTERN)


def test_py_parser():
    """Should parse 6 to-dos from the file"""
    path = f"{pwd}/tests/parser/py_gh/src/python.py"

    with open(path, "r") as file:
        content = file.readlines()
        result = py_parser.parse(content, "/py_gh/src/python.py")

        assert len(result) == 6
