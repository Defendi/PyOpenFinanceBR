
from setuptools import setup, find_packages

PACKAGE = "pyopenfinancebr"
DESCRIPTION = "Integração Python com API Open Finance do bancos brasileiros"
NAME = PACKAGE
AUTHOR = "Alexandre Defendi"
AUTHOR_EMAIL = "alexandre_defendi@hotmail.com"
URL = "https://github.com/tiagocordeiro/pybling.git"
VERSION = __import__(PACKAGE).__version__

setup(
    name="PyOpenFinanceBR",
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    keywords=['Open finance', 'open bank'],
    classifiers=[
        'Development Status :: 1 - Start',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (AGPL-3.0)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=find_packages(exclude=['*test*']),
    package_data={PACKAGE: []},
    url='https://github.com/Defendi/PyOpenFinanceBR.git',
    license='AGPL-3.0',
    description='PyOpenFinanceBR é uma biblioteca para acesso ao Open Finance Brasil',
    long_description=open('README.md', 'r').read(),
    install_requires=[
    ],
    tests_require=[
        'pytest',
    ],
)
