from pathlib import Path
import sys

# add base project path to PYTHONPATH
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

__version__ = "0.2.2"
name = "dolistparser"


from _internal.interfaces.api import js_parser, py_parser, py_gh_parser, js_gh_parser, run
from _internal.domain.comment import ParsedComment
