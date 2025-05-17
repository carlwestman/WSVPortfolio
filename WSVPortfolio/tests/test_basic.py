import unittest

class TestWSVPortfolio(unittest.TestCase):
    def test_import(self):
        import WSVPortfolio
        self.assertIsNotNone(WSVPortfolio)

if __name__ == "__main__":
    unittest.main()
