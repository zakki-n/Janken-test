import unittest
import sys
import os
project_root = (os.path.dirname(os.path.dirname(__file__)))
sys.path.append(project_root)
from source import computer_pon 

class TestComputerPon(unittest.TestCase):
    def test_computer_pon(self):
        hands = ["グー", "チョキ", "パー"] 
        result = computer_pon()
        self.assertIn(result, hands)

if __name__ == "__main__":
    unittest.main()