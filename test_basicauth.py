from base64 import b64encode

from pytest import raises

from basicauth import decode, DecodeError, encode


def test_prepends_basic_auth():
    assert encode(b'', b'').lower().startswith(b'basic')


def test_adds_space_after_basic():
    assert encode(b'', b'').lower().startswith(b'basic ')


def test_encodes_short_username():
    assert encode(b'', b'password')


def test_encodes_short_password():
    assert encode(b'username', b'')


def test_encodes_long_username():
    assert encode(b'username'*1000000, b'')


def test_encodes_long_password():
    assert encode(b'', b'password'*1000000)


def test_decodes_empty_username():
    assert b'' == decode(encode(b'', b'password'))[0]


def test_decodes_empty_password():
    assert b'' == decode(encode(b'username', b''))[1]


def test_decodes_hashes_only():
    username, password = b'username', b'omgawesome!'
    encoded_str = encode(username, password)
    encoded_hash = encoded_str.split(b' ')[1]
    assert (username, password) == decode(encoded_hash)


def test_decodes_fully_encoded_strings():
    username, password = b'username', b'password'
    encoded_str = encode(username, password)
    assert (username, password) == decode(encoded_str)


def test_doesnt_decode_invalid_auth_types():
    encoded_str = b'error woot'
    with raises(DecodeError):
        decode(encoded_str)


def test_doesnt_decode_invalid_hashes():
    encoded_str = b'basic omg hacks what'
    with raises(DecodeError):
        decode(encoded_str)

    encoded_str = b'basic omg hacks'
    with raises(DecodeError):
        decode(encoded_str)


def test_properly_escapes_colons():
    username, password = b'username', b'pass:word:'

    encoded_str = encode(username, password)
    assert (username, password) == decode(encoded_str)

    # This test ensures things work even if the client doesn't properly URL
    # encode the username / password fields.
    encoded_str = b'Basic %s' % b64encode(b'%s:%s' % (username, password))
    assert (username, password) == decode(encoded_str)
