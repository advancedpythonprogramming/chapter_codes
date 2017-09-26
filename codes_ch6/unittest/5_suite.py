import unittest


class ArithmeticTest(unittest.TestCase):

    def test_arit(self):
        self.assertEqual(1+1, 2)


if __name__ == "__main__":
    Tsuite = unittest.TestSuite()
    Tsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(ArithmeticTest))
    unittest.TextTestRunner().run(Tsuite)
