import os
import shutil

from typing import List, Union
from abc import ABC, abstractmethod
from pybackup.core.file_manager import filter_files

from pybackup.core.filter import Filter


class BackupManager(ABC):
    def __init__(
        self,
        type: str,
        origin: str,
        destination: str,
        schedule: str,
        include_filters: List[Filter],
        exclude_filters: List[Filter],
    ):
        self.type = type
        self.origin = origin
        self.destination = destination
        self.schedule = schedule
        self.include_filters = include_filters
        self.exclude_filters = exclude_filters

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def restore(self):
        pass


class FileCopyBackup(BackupManager):
    def __init__(
        self,
        origin: str,
        destination: str,
        schedule: str,
        include_filters: Union[List[Filter], None] = None,
        exclude_filters: Union[List[Filter], None] = None,
    ):
        if include_filters is None:
            include_filters = []
        if exclude_filters is None:
            exclude_filters = []

        super().__init__(
            "FileCopyBackup",
            origin=origin,
            destination=destination,
            schedule=schedule,
            include_filters=include_filters,
            exclude_filters=exclude_filters,
        )

    def create(self):
        files = filter_files(self.origin, self.include_filters, self.exclude_filters)
        for file_path in files:
            file_dest_path = file_path.replace(self.origin, self.destination)
            folder_path, _ = os.path.split(file_dest_path)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            shutil.copy(file_path, file_dest_path)

    def restore(self):
        pass
