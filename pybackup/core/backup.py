from abc import ABC


class BackupManager(ABC):
    def run(self):
        pass


def create_backup(
    backup_manager: BackupManager,
    origin: str,
    destination: str,
    include_filters: List[Filter],
    exclude_filters: List[Filter],
):
    pass
