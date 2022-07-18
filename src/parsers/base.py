from definition import ParsedComment
from typing import List


class BaseParser:
    def parse(path: str) -> List[ParsedComment]:
        pass
