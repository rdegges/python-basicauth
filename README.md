# python-basicauth

[![Build Status](https://github.com/rdegges/python-basicauth/actions/workflows/test.yml/badge.svg)](https://github.com/rdegges/python-basicauth/actions)
[![Known Vulnerabilities](https://snyk.io/test/github/rdegges/python-basicauth/badge.svg)]

A dead simple HTTP basic auth encoder and decoder. Why? Because HTTP should be
drop dead easy. That's why.


![HTTP Basic Auth?!](https://github.com/rdegges/python-basicauth/raw/master/http_basic_auth.jpg)


## Install

To install ``python-basicauth``, simply run ``pip install basicauth`` and
you'll get the latest version installed automatically.


## Usage

To generate an encoded basic auth string:

``` python
>>> from basicauth import encode
>>> username, password = 'rdegges', 'omghax!!!'
>>> encoded_str = encode(username, password)
>>> print encoded_str
'Basic cmRlZ2dlczpvbWdoYXglMjElMjElMjE='
```

To decode an encoded basic auth string:

``` python
>>> from basicauth import decode
>>> encoded_str = 'Basic cmRlZ2dlczpvbWdoYXglMjElMjElMjE='  # From the example above.
>>> username, password = decode(encoded_str)
>>> print (username, password)
('rdegges', 'omghax!!!')
```

We can also decode the hash directly:

``` python
>>> from basicauth import decode
>>> encoded_str = 'cmRlZ2dlczpvbWdoYXglMjElMjElMjE='  # From the example above.
>>> username, password = decode(encoded_str)
>>> print (username, password)
('rdegges', 'omghax!!!')
```

And if there are errors:

``` python
>>> from basicauth import decode, DecodeError
>>> encoded_str = 'lol omg cmRlZ2dlczpvbWdoYXglMjElMjElMjE='  # Invalid hash.
>>> username, password = decode(encoded_str)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "basicauth/__init__.py", line 49, in decode
    raise DecodeError
basicauth.DecodeError
```

**NOTE**: The [HTTP Basic Authentication spec](http://www.ietf.org/rfc/rfc2617.txt)
doesn **NOT** allow you to include any colon characters (`:`) in the username
field.  Colons are allowed in the password field -- but that's it.


## Tests

Want to run the tests? No problem:

``` bash
$ git clone https://github.com/rdegges/python-basicauth.git
$ cd python-basicauth
$ pip install -e .
...
$ python -m unittest
..............
----------------------------------------------------------------------
Ran 14 tests in 0.103s

OK
```
