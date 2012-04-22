import unittest
import score
import os
import shelve

class TestScore(unittest.TestCase):
    
    def setUp(self):
        shelf = shelve.open('v:\workspace\Python2_Homework04\src\myshelf.shlf')
        shelf.close()
    
    def test_score(self):    
        score.high_score("Albert", 5)
        score.high_score("Bruce", 10)
        score.high_score("Charlie", 15)
        score.high_score("David", 20)
        
        score.high_score("Albert", 20)
        score.high_score("Bruce", 5)

        shelf = shelve.open('v:\workspace\python2_Homework04\src\myshelf.shlf')
        expected = {'Albert':20, 'Bruce':10, 'Charlie':15, 'David':20}
        self.assertEqual(shelf, expected)
        shelf.close()

    def tearDown(self):
        os.remove('v:\workspace\python2_Homework04\src\myshelf.shlf.bak')
        os.remove('v:\workspace\python2_Homework04\src\myshelf.shlf.dat')
        os.remove('v:\workspace\python2_Homework04\src\myshelf.shlf.dir')
    
if __name__ == "__main__":
    unittest.main()

