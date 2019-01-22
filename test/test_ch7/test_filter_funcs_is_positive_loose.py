from unittest import TestCase
from nose.tools import assert_equal
from chap7.filter_funcs import is_positive
class FilterIntsTestCase(TestCase):
    def test_is_positive(self):
        assert_equal(False, is_positive(-2)) # before boundary
        assert_equal(False, is_positive(0)) # on the boundary
        assert_equal(True, is_positive(2)) # after the boundary
