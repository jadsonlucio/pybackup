import re
from abc import ABC, abstractmethod
from typing import Literal


FilterType = Literal["file", "folder"]


class Filter(ABC):
    """Abstract class for path filters"""

    def __init__(self, name: str, type: FilterType, description: str):
        self.type = type
        self.name = name

    @abstractmethod
    def match(self, path: str) -> bool:
        pass


class RegexFilter(Filter):
    def __init__(self, name: str, regex: str, type: FilterType, description: str):
        self.regex = regex
        super().__init__(name, type, description)

    def match(self, path: str) -> bool:
        return re.match(self.regex, path) is not None


class FolderRegexFilter(RegexFilter):
    def __init__(self, name: str, regex: str, description: str = ""):
        super().__init__(name, regex, "folder", description)


class FileRegexFilter(RegexFilter):
    def __init__(self, name: str, regex: str, description: str = ""):
        super().__init__(name, regex, "file", description)
