# python-basicauth

A dead simple HTTP basic auth encoder and decoder. Why? Because HTTP should be
drop dead easy. That's why.


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


## Tests

[![Build Status](https://secure.travis-ci.org/rdegges/python-basicauth.png?branch=master)](http://travis-ci.org/rdegges/python-basicauth)

Want to run the tests? No problem:

``` bash
$ git clone git://github.com/rdegges/python-basicauth.git
$ cd python-basicauth
$ python setup.py develop
...
$ pip install -r requirements.txt  # Install test dependencies.
$ nosetests
.............
----------------------------------------------------------------------
Ran 13 tests in 0.166s

OK
```
