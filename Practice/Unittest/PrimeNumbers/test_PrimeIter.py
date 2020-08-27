import unittest
from nose.tools import assert_equals, raises
from PrimeIter import PrimeIter, NonValidInput


class TestWithNose:
    def test_PrimeIter(self):
        assert_equals(list(PrimeIter(5)), [2, 3, 5, 7, 11])
    @raises(NonValidInput)
    def test_nonvalidinput_type(self):
        PrimeIter('aaaa')
    @raises(NonValidInput)
    def test_nonvalidinput_value(self):
        PrimeIter(-1)


if __name__ == '__main__':
    unittest.main()
