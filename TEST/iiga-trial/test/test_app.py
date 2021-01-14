import unittest
from unittest.mock import patch, Mock, MagicMock

from app import index


class TestApp(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_index(self):
        actual = index()
        expect = "Hello, World!'Hello from nested_script''Hello from root_script'"
        self.assertEqual(actual, expect)

    def test_index_mock(self):
        with patch("root_script.say_hello") as root_mock,\
                patch("nested.script.say_hello") as nest_mock:

            root_mock.return_value = "root"
            nest_mock.return_value = "nest"

            actual = index()
            expect = "Hello, World!nestroot"
            self.assertEqual(actual, expect)


if __name__ == "__main__":
    unittest.main(verbosity=2)
