from typing import List
from typing_extensions import TypedDict, Literal


class ParsedComment(TypedDict):
    type: Literal["TODO"]
    commentStyle: Literal["oneline", "multiline"]
    title: str
    fullComment: List[str]
    path: str
    lineNumber: int
