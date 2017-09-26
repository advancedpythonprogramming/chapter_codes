import unittest


class ShowAsserts(unittest.TestCase):

    def test_assertions(self):
        a = 2
        b = a
        c = 1. + 1.
        self.assertEqual([1, 2, 3], [1, 2, 3])  # Fails if a != b
        self.assertNotEqual("hello", "bye")  # Fails if a == b
        self.assertTrue("Hello" == "Hello")  # Fails if bool(x) is False
        self.assertFalse("Hello" == "Bye")  # Fails if bool(x) is True
        self.assertIs(a, b)  # Fails if a is not b

        # Fails if a is b. Pay attention that "is" implies
        # equality (==) but not upside. Two differents objects
        # can have the same value.
        self.assertIsNot(a, c)

        self.assertIsNone(None)  # Fails if x is not None
        self.assertIsNotNone(2)  # Fails if x is None
        self.assertIn(2, [2, 3, 4])  # Fails if a is not in b
        self.assertNotIn(1, [2, 3, 4])  # Fails if a is in b

        # Fails if isinstance(a, b) is False
        self.assertIsInstance("Hello", str)
        # Fail if isinstance(a, b) is True
        self.assertNotIsInstance("1", int)  

if __name__ == "__main__":
    unittest.main()
