import unittest
import relativezip
import os, shutil

class TestRelativezip(unittest.TestCase):
    filenames = ["groucho", "harpo", "chico"]
    path = "v:\\workspace\\Python2_Homework05\\src\\archive_me"

    def setUp(self):
        # Make test files to compress
        os.mkdir(self.path)
        for fn in self.filenames:
            f = open(os.path.join(self.path, fn), "w")
            f.close()
        # Make test subdirectory and subdirectory files
        os.mkdir(self.path + "\\subdir")
        for fn in self.filenames:
            f = open(os.path.join(self.path + "\\subdir", fn), "w")
            f.close()
        
    def test_relativezip(self):    
        relativezip.dirArchive(self.path)

    def tearDown(self):
        shutil.rmtree(self.path)
        os.remove(self.path + ".zip")
    
if __name__ == "__main__":
    unittest.main()