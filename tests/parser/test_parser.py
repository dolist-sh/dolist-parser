import pytest
from os import getcwd

from src.parser import parse



def test_parser_typescript():
    """Should parse 8 to-dos from input file"""
    pwd = getcwd()
    result = parse(f"{pwd}/tests/parser/data/typescript.ts")
    
    assert result == 8


# Test the parse call: check if the correct output is returned


# Test the _find_comment_start_index call
