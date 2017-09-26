def setup_module(module):
    print("Setting up module {0}".format(module.__name__))


def teardown_module(module):
    print("Tearing down module {0}".format(module.__name__))


def test_a_function():
    print("Running test function")


class BaseTest:

    def setup_class(cls):
        print("Setting up Class {0}".format(cls.__name__))

    def teardown_class(cls):
        print("Tearing down Class {0}\n".format(cls.__name__))

    def setup_method(self, method):
        print("Setting up method {0}".format(method.__name__))

    def teardown_method(self, method):
        print("Tearing down  method {0}".format(method.__name__))


class TestClass1(BaseTest):

    def test_method_1(self):
        print("Running Method 1-1")

    def test_method_2(self):
        print("Running Method 2-1")


class TestClass2(BaseTest):

    def test_method_1(self):
        print("Running Method 1-2")

    def test_method_2(self):
        print("Running Method 2-2")

# Running by console "py.test PyTest.py -s",
# -s disables the deletion of "print" outputs.
