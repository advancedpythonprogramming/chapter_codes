import unittest


class CheckNumbers(unittest.TestCase):

    # This test has to be ok
    def test_int_float(self):
        self.assertEquals(1, 1.0)

    # This test fails
    def test_str_float(self):
        self.assertEquals(1, "1")

if __name__ == "__main__":
    unittest.main()
