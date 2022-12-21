from os.path import abspath, dirname, join, normpath

from setuptools import setup

setup(

    # Basic package information:
    name='basicauth',
    version='0.4.1',
    py_modules=('basicauth',),

    # Packaging options:
    zip_safe=False,
    include_package_data=True,

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

    # Metadata for PyPI:
    author='Randall Degges',
    author_email='r@rdegges.com',
    license='UNLICENSE',
    url='https://github.com/rdegges/python-basicauth',
    keywords='python security basicauth http',
    description='An incredibly simple HTTP basic auth implementation.',
    long_description=open(normpath(join(dirname(abspath(__file__)), 'README.md'))).read()

)
