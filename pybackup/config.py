from typing import List
from pydantic import BaseModel

DEFAULT_EXCLUDE_FOLDERS = [
    "*node_modules",
    "*__pycache__",
    "*venv",
]


class BackupConfigModel(BaseModel):
    origin_path: str
    destination_path: str
    ignore_patterns: List[str]
    include_patterns: List[str]

