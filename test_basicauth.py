from base64 import b64encode
from unittest import TestCase

from basicauth import decode, DecodeError, encode


class Encode(TestCase):

    def test_prepends_basic_auth(self):
        self.assertTrue(encode(b'', b'').lower().startswith(b'basic'))

    def test_adds_space_after_basic(self):
        self.assertTrue(encode(b'', b'').lower().startswith(b'basic '))

    def test_encodes_short_username(self):
        self.assertTrue(encode(b'', b'password'))

    def test_encodes_short_password(self):
        self.assertTrue(encode(b'username', b''))

    def test_encodes_long_username(self):
        self.assertTrue(encode(b'username'*1000000, b''))

    def test_encodes_long_password(self):
        self.assertTrue(encode(b'', b'password'*1000000))


class Decode(TestCase):

    def test_decodes_empty_username(self):
        self.assertEqual(b'', decode(encode(b'', b'password'))[0])

    def test_decodes_empty_password(self):
        self.assertEqual(b'', decode(encode(b'username', b''))[1])

    def test_decodes_hashes_only(self):
        username, password = b'username', b'omgawesome!'
        encoded_str = encode(username, password)
        encoded_hash = encoded_str.split(b' ')[1]
        self.assertEqual((username, password), decode(encoded_hash))

    def test_decodes_fully_encoded_strings(self):
        username, password = b'username', b'password'
        encoded_str = encode(username, password)
        self.assertEqual((username, password), decode(encoded_str))

    def test_doesnt_decode_invalid_auth_types(self):
        encoded_str = b'error woot'
        self.assertRaises(DecodeError, decode, encoded_str)

    def test_doesnt_decode_invalid_hashes(self):
        encoded_str = b'basic omg hacks what'
        self.assertRaises(DecodeError, decode, encoded_str)

        encoded_str = b'basic omg hacks'
        self.assertRaises(DecodeError, decode, encoded_str)

    def test_properly_escapes_colons(self):
        username, password = b'username', b'pass:word:'

        encoded_str = encode(username, password)
        self.assertEqual((username, password), decode(encoded_str))

        # This test ensures things work even if the client doesn't properly URL
        # encode the username / password fields.
        encoded_str = b'Basic %s' % b64encode(b'%s:%s' % (username, password))
        self.assertEqual((username, password), decode(encoded_str))
