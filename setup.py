from os.path import abspath, dirname, join, normpath

from setuptools import setup

setup(

    # Basic package information:
    name='basicauth',
    version='1.0.0',
    py_modules=['basicauth'],

    # Metadata for PyPI:
    author='Randall Degges',
    author_email='r@rdegges.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
    ],
    description='An incredibly simple HTTP basic auth implementation.',
    keywords=['security', 'basicauth', 'http'],
    license='UNLICENSE',
    license_files=['UNLICENSE'],
    long_description=open(normpath(join(dirname(abspath(__file__)), 'README.md'))).read(),
    long_description_content_type='text/markdown',
    url='https://github.com/rdegges/python-basicauth',

)