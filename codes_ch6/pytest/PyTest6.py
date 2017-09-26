import sys
import py.test


@py.test.mark.skipif("sys.platform != \"Linows\"")
def test_simple_skip():
    fakeos.do_something_fake()
    assert fakeos.did_not_happen
