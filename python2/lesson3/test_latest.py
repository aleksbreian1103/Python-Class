import unittest
import latest
import time
import os

PATHSTEM = "v:\\workspace\\Python2_Homework03\\src\\testdir\\"

class TestLatest(unittest.TestCase):

    def setUp(self):
        self.path = PATHSTEM
        self.file_names = ["file.old", "file.bak", "file.new", "test.old"]
        for fn in self.file_names:
            f = open(self.path+fn, "w")
            f.close()
            time.sleep(1)
            
    def test_latest_no_extension(self):
        """
        Ensure that calling the function with no arguments returns
        the extensions with their counts.
        """
        expected = {".old":2, ".bak":1, ".new":1}
        ext_num = latest.print_extension(self.path)
        self.assertEqual(ext_num, expected)

    def tearDown(self):
        for fn in self.file_names:
            os.remove(self.path + fn)

if __name__ == "__main__":
    unittest.main()

