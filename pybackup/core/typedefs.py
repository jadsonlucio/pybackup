from typing import List, TypedDict


class BackupConfig(TypedDict):
    origin_path: str
    destination_path: str
    ignore_patterns: List[str]
    include_patterns: List[str]
