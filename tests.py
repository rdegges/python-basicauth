from base64 import b64encode
from unittest import TestCase

from basicauth import decode, DecodeError, encode, EncodeError


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

    def test_prevent_colon_char(self):
        self.assertRaises(EncodeError, lambda: encode(':', 'password'))


class Decode(TestCase):

    def test_decodes_empty_username(self):
        self.assertEqual('', decode(encode('', 'password'))[0])

    def test_decodes_empty_password(self):
        self.assertEqual('', decode(encode('username', ''))[1])

    def test_decodes_hashes_only(self):
        username, password = 'username', 'omgawesome!'
        encoded_str = encode(username, password)
        encoded_hash = encoded_str.split(' ')[1]
        self.assertEqual((username, password), decode(encoded_hash))

    def test_decodes_fully_encoded_strings(self):
        username, password = 'username', 'password'
        encoded_str = encode(username, password)
        self.assertEqual((username, password), decode(encoded_str))

    def test_doesnt_decode_invalid_auth_types(self):
        encoded_str = 'error woot'
        self.assertRaises(DecodeError, decode, encoded_str)

    def test_doesnt_decode_invalid_hashes(self):
        encoded_str = 'basic omg hacks what'
        self.assertRaises(DecodeError, decode, encoded_str)

        encoded_str = 'basic omg hacks'
        self.assertRaises(DecodeError, decode, encoded_str)

    def test_properly_escapes_colons(self):
        username, password = 'username', 'pass:word:'

        encoded_str = encode(username, password)
        self.assertEqual((username, password), decode(encoded_str))

        # This test ensures things work even if the client doesn't properly URL
        # encode the username / password fields.
        username_password = f'{username}:{password}'
        encoded_str = f'Basic {b64encode(username_password.encode()).decode()}'
        self.assertEqual((username, password), decode(encoded_str))