"""Demonstrates the unittest module in action."""
import unittest

def title(s):
    "Returns same string with first character capitalized."
    return s[0].upper()+s[1:]

class TestTitle(unittest.TestCase):
    def test_one_letter(self):
        self.assertEqual(title("a"), "a".title(), "a should be capitialized.")        
 
    def test_one_word(self):
        self.assertEqual(title("test"), "test".title(), "tile(test) == \"Test\"")
    
    def test_sentence(self):
        self.assertEqual(title("hooray For Python."), "hooray For Python.".title(), "First letter should be capitialized.")        

    def test_edge(self):
        self.assertEqual(title("hi, how are you doing?"), "hi, how are you doing?".title(), "First letter should be capitialized.")        

if __name__ == "__main__":
    unittest.main()