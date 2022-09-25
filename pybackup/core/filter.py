import re
from abc import ABC, abstractmethod
from typing import Literal


FilterType = Literal["file", "folder"]


class Filter(ABC):
    """Abstract class for path filters"""

    def __init__(self, type: FilterType):
        self.type = type

    @abstractmethod
    def match(self, path: str) -> bool:
        pass


class RegexFilter(Filter):
    def __init__(self, regex: str, type: FilterType):
        self.regex = regex
        super().__init__(type)

    def match(self, path: str) -> bool:
        return re.match(self.regex, path) is not None


class FolderRegexFilter(RegexFilter):
    def __init__(self, regex: str):
        super().__init__(regex, "folder")


class FileRegexFilter(RegexFilter):
    def __init__(self, regex: str):
        super().__init__(regex, "file")
