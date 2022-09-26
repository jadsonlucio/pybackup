from pybackup.core.backup import BackupManager, FileCopyBackup
from pybackup.core.filter import FileRegexFilter, Filter, FolderRegexFilter

from pybackup.core.typedefs import BackupConfig, BackupFilter


def create_filter(backup_filter: BackupFilter) -> Filter:
    if backup_filter["type"] == "folder_regex":
        return FolderRegexFilter(
            backup_filter["name"],
            backup_filter["params"]["regex"],
            description=backup_filter["description"],
        )
    elif backup_filter["type"] == "file_regex":
        return FileRegexFilter(
            backup_filter["name"],
            backup_filter["params"]["regex"],
            description=backup_filter["description"],
        )
    else:
        raise Exception("filter type not valid")


def create_backup(config: BackupConfig) -> BackupManager:
    include_filters = [
        create_filter(include_filter) for include_filter in config["include_filters"]
    ]
    exclude_filters = [
        create_filter(exclude_filter) for exclude_filter in config["exclude_filters"]
    ]

    if config["type"] == "file_copy":
        return FileCopyBackup(
            origin=config["origin"],
            destination=config["destination"],
            schedule=config["schedule"],
            include_filters=include_filters,
            exclude_filters=exclude_filters,
        )
    else:
        raise Exception("Invalid backup type")
