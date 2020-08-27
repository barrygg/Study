import unittest
from nose.tools import assert_equals, raises
from convert_to_roman import convert_to_roman, NonValidInput


class TestWithNose:
    def test_convert_to_roman(self):
        assert_equals(convert_to_roman(4444), 'MMMMCDCLIV')
    @raises(NonValidInput)
    def test_nonvalidinput_type(self):
        convert_to_roman('aaaa')
    @raises(NonValidInput)
    def test_nonvalidinput_value(self):
        convert_to_roman(-1)


if __name__ == '__main__':
    unittest.main()

