import sys
import py.test


def test_simple_skip():
    if sys.platform != "Linows":
        py.test.skip("This test only works on Linows OS")
    fakeos.do_something_fake()
    assert fakeos.did_not_happen
