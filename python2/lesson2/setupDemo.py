"""
Demonstration of setUp and tearDown.
The tests do not actually test anything - this is a demo.
"""
import unittest
import tempfile
import shutil
import glob
import os

class FileTest(unittest.TestCase):
    
    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp("testdir")
        os.chdir(self.dirname)
    
    def test_1(self):
        "Verify creation of files is possible"
        "The test_1() method includes code to verify that the test directory contains only the files created by the for loop."
        "Hint: You might create a set containing the list of three filenames, and then create a set from the os.listdir() method."
        filelist = []
        for filename in ("this.txt", "that.txt", "the_other.txt"):
            f = open(filename, "w")
            f.write("Some text\n")
            filelist.append(filename)
            f.close()
            self.assertTrue(f.closed)
            
        self.assertEqual(os.listdir(self.dirname).sort(), filelist.sort(), "Files created are not the same as specified.")
        
    
    def test_2(self):
        "Verify that the current directory is empty"
        self.assertEqual(glob.glob("*"), [], "Directory not empty")

    def test_3(self):
        "Creates a binary file that contains exactly a million bytes."
        "A test_3() method creates a binary file that contains exactly a million bytes, closes it"
        "and then uses os.stat to verify that the file on disk is of the correct length (with os.stat, statinfo.st_size"
        "returns the size in bytes)."

        f = open("one_milli.bin", "w")
        for i in range(1000000):
            f.write("1")
        f.close()
        self.assertTrue(f.closed)
        
        statinfo = os.stat("one_milli.bin")
        self.assertEqual(1000000, statinfo.st_size, "File length is not exactly one million bytes.")

    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)


