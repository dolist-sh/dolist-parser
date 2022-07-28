from pathlib import Path
import sys

# add base project path to PYTHONPATH
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

__version__ = "0.2.0"
name = "dolistparser"

from main import js_parser, py_parser, py_gh_parser, js_gh_parser, run
from definition import ParsedComment
