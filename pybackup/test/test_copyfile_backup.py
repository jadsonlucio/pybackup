import os

from pyfakefs import fake_filesystem_unittest

from pybackup.core.backup import FileCopyBackup


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

    def test_copyfile(self):
        backup = FileCopyBackup("/test", "/backup", "test")
        backup.create()

        backup_files = os.listdir("/backup")
        alpha_files = os.listdir("/backup/alpha")
        beta_files = os.listdir("/backup/beta")
        self.assertIn("p.txt", backup_files)
        self.assertIn("p.exe", backup_files)
        self.assertIn("alpha", backup_files)
        self.assertIn("beta", backup_files)
        self.assertIn("a.txt", alpha_files)
        self.assertIn("a.exe", alpha_files)
        self.assertIn("b.txt", beta_files)
        self.assertIn("b.exe", beta_files)
