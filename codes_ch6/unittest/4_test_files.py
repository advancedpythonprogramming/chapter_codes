import os
import unittest


class TestFiles(unittest.TestCase):

    def setUp(self):
        self.file = open("test_file.txt", 'w')
        self.dictionary = {1: "Hello", 2: "Bye"}

    def tearDown(self):
        self.file.close()
        print("Removing temporary files...")
        os.remove("test_file.txt")

    def test_str(self):
        print("Writing temporary files...")
        self.file.write(self.dictionary[1])
        self.file.close()
        self.file = open("test_file.txt", 'r')
        d = self.file.readlines()[0]
        print(d)
        self.assertEqual(self.dictionary[1], d)


if __name__ == "__main__":
    unittest.main()
