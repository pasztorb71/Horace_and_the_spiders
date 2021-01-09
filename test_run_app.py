import unittest
from unittest import TestCase

from ground import Ground
from horace import Horace
from spider import Spider


class TestApp(TestCase):

	def test_connect_database(self):
		g = Ground()
		self.assertTrue(g != None)
		s = Spider()
		self.assertTrue(s != None)
		h = Horace()
		self.assertTrue(h != None)

if __name__ == '__main__':
    unittest.main()