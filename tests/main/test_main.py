import pytest
from os import getcwd
from src.main import run

pwd = getcwd()


def test_source_parsing():
    """Should parse the 53 to-do comments from source"""

    result = run(f"{pwd}/tests/main/data")

    assert len(result) == 53
