import os
from pybackup.core.file_manager import filter_files
from pybackup.core.filter import FileRegexFilter

from pyfakefs import fake_filesystem_unittest


class TestFilter(fake_filesystem_unittest.TestCase):
    def setUp(self) -> None:
        self.setUpPyfakefs()
        self.create_file_structure()

    def create_file_structure(self):
        os.makedirs("/test/alpha")
        os.makedirs("/test/beta")
        open("/test/p.txt", "w").close()
        open("/test/p.exe", "w").close()
        open("/test/alpha/a.txt", "w").close()
        open("/test/alpha/a.exe", "w").close()
        open("/test/beta/b.txt", "w").close()
        open("/test/beta/b.exe", "w").close()

    def test_simple_filter(self):

        include_filters = []
        exclude_filters = []
        self.assertEqual(
            list(filter_files("/test", include_filters, exclude_filters)),
            [
                "/test/p.txt",
                "/test/p.exe",
                "/test/alpha/a.txt",
                "/test/alpha/a.exe",
                "/test/beta/b.txt",
                "/test/beta/b.exe",
            ],
        )

    def test_txt_filefilter(self):
        include_filters = [FileRegexFilter(r".*\.txt")]
        exclude_filters = []
        self.assertEqual(
            list(filter_files("/test", include_filters, exclude_filters)),
            [
                "/test/p.txt",
                "/test/alpha/a.txt",
                "/test/beta/b.txt",
            ],
        )

    def test_folder_filter(self):
        include_filters = [FileRegexFilter(r".*beta")]
        exclude_filters = []
        self.assertEqual(
            list(filter_files("/test", include_filters, exclude_filters)),
            [
                "/test/beta/b.txt",
                "/test/beta/b.exe",
            ],
        )
