"""
Testing utilities
"""

import unittest
import api

class BaseTestCase(unittest.TestCase):
    """
    The base unit test class implementation
    """
    def setUp(self):
        """Run before each test"""
        api.app.config['TESTING'] = True
        self.app = api.app.test_client()

    def tearDown(self):
        """Run after test"""
        pass
