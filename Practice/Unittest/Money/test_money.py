import unittest
from nose.tools import assert_equals, assert_false, assert_less, assert_greater, \
    assert_greater_equal, assert_less_equal, assert_equal, assert_not_equal
from money import Money


class TestWithNose:

    def test_money(self):
        m = Money(51, 60)
        n = Money(33, 50)
        assert_equals(m + n, Money(85, 10))
        assert_equals(m - n, Money(18, 10))
        assert_equals(m / 2, Money(25, 80))
        assert_greater(m, n)
        assert_less(n, m)
        assert_less_equal(n, m)
        assert_greater_equal(m, n)
        assert_equals(m.getcourse(59), '0 rub, 87 kop')
        assert_equals(n.getmoney(), '33,50')
        assert_equal(n, Money(33, 50))
        assert_not_equal(m, n)
        assert_false(n > m)
        assert_false(m < n)
        assert_false(m <= n)
        assert_false(n >= m)
        assert_false(m == n)
        assert_false(Money(33, 50) != n)


if __name__ == '__main__':
    unittest.main()

