import os
from typing import List, Union
from pybackup.core.filter import Filter


def is_valid_path(
    path: str,
    include_filters: Union[List[Filter], None] = None,
    exclude_filters: Union[List[Filter], None] = None,
):
    """Validade an path based on an list of include and exclude filters"""
    is_valid = True
    if include_filters:
        is_valid = any(map(lambda filter: filter.match(path), include_filters))

    if exclude_filters:
        is_valid = not any(map(lambda filter: filter.match(path), exclude_filters))

    return is_valid


def filter_files(
    path: str,
    include_filters: Union[List[Filter], None] = None,
    exclude_filters: Union[List[Filter], None] = None,
):
    """Filter files in a path based on an list of include and exclude filters

    Args:
        path (str): path of the file
        include_filters (List[PathFilter]): List of filters that will validade if the path is valid
        exclude_filters (List[PathFilter]): List of filters that will validade if the path is invalid
    """
    if include_filters is None:
        include_filters = []
    if exclude_filters is None:
        exclude_filters = []

    folder_include_filters = list(
        filter(lambda filter: filter.type == "folder", include_filters)
    )
    folder_exclude_filters = list(
        filter(lambda filter: filter.type == "folder", exclude_filters)
    )

    for root, folders, files in os.walk(path):
        if is_valid_path(root, folder_include_filters, folder_exclude_filters):
            for file in files:
                file_path = os.path.join(root, file)
                if is_valid_path(file_path, include_filters, exclude_filters):
                    yield file_path
            for folder in folders:
                folder_path = os.path.join(root, folder)
                if not is_valid_path(
                    folder_path, folder_include_filters, folder_exclude_filters
                ):
                    folders.remove(folder)


def create_backup():
    pass