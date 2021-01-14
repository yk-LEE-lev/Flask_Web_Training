import unittest
from unittest import makeSuite

from test_app import TestApp


def make_test_suite():
    suite = unittest.TestSuite()
    suite.addTest(makeSuite(TestApp))
    return suite


if __name__ == '__main__':
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_suite = make_test_suite()
    test_runner.run(test_suite)
