from os.path import abspath, dirname, join, normpath

from setuptools import setup


setup(

    # Basic package information:
    name = 'basicauth',
    version = '0.1',
    packages = ('basicauth',),

    # Packaging options:
    zip_safe = False,
    include_package_data = True,

    # Package dependencies:
    install_requires = [],

    # Metadata for PyPI:
    author = 'Randall Degges',
    author_email = 'rdegges@gmail.com',
    license = 'UNLICENSE',
    url = 'https://github.com/rdegges/python-basicauth',
    keywords = 'python security basicauth http',
    description = 'An incredibly simple HTTP basic auth implementation.',
    long_description = open(normpath(join(dirname(abspath(__file__)),
        'README.md'))).read()

)
