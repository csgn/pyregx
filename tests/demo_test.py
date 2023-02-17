import unittest

from pyregx.demo import demo

class TestDemo(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(demo(), "WORKING")

unittest.main()
