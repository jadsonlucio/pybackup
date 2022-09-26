from typing import Any, Dict, List, TypedDict


class BackupFilter(TypedDict):
    name: str
    type: str
    description: str
    params: Dict[str, Any]


class BackupConfig(TypedDict):
    type: str
    origin: str
    destination: str
    schedule: str
    include_filters: List[BackupFilter]
    exclude_filters: List[BackupFilter]
    config: Dict[str, Any]
