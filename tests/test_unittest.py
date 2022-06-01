# testunittest.py
from ..server import getStringContainingTheWordAdminLowercase
from unittest import TestCase
class testunitcase(TestCase):
    def test_always_passes(self):
        self.assertTrue(getStringContainingTheWordAdminLowercase()=="admin")