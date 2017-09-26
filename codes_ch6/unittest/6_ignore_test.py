import unittest
import sys


class IgnoreTests(unittest.TestCase):

    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(False, True)

    @unittest.skip("Useless test")
    def test_ignore(self):
        self.assertEqual(False, True)

    @unittest.skipIf(sys.version_info.minor == 5, "does not work on 3.5")
    def test_ignore_if(self):
        self.assertEqual(False, True)

    @unittest.skipUnless(sys.platform.startswith("linux"),
                         "does not work on linux")
    def test_ignore_unless(self):
        self.assertEqual(False, True)


if __name__ == "__main__":
    unittest.main()
