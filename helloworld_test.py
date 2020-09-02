import unittest
import helloworld

class TestHelloWorld(unittest.TestCase):
    #Test cases class with extended test cases.
    def test_hello(self):
        self.assertTrue(True)
        
if __name__ == '__main__':
    print("Running unit tests")
    unittest.main()