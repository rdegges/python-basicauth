from unittest import TestCase

from basicauth import decode, DecodeError, encode


class Encode(TestCase):

    def test_prepends_basic_auth(self):
        self.assertTrue(encode('', '').lower().startswith('basic'))

    def test_adds_space_after_basic(self):
        self.assertTrue(encode('', '').lower().startswith('basic '))

    def test_encodes_short_username(self):
        self.assertTrue(encode('', 'password'))

    def test_encodes_short_password(self):
        self.assertTrue(encode('username', ''))

    def test_encodes_long_username(self):
        self.assertTrue(encode('username'*1000000, ''))

    def test_encodes_long_password(self):
        self.assertTrue(encode('', 'password'*1000000))
