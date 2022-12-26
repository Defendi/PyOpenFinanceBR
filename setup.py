# 0.0.0
from setuptools import setup, find_packages

VERSION = "0.0.0"

setup(
    name="PyOpenFinanceBR",
    version=VERSION,
    author="Alexandre Defendi",
    author_email='alexandre_defendi@hotmail.com',
    keywords=['Open finance', 'open bank'],
    classifiers=[
        'Development Status :: 1 - Start',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=find_packages(exclude=['*test*']),
    package_data={'pyopenfinance': [
    ]},
    url='https://github.com/Defendi/PyOpenFinanceBR',
    license='LGPL-v2.1+',
    description='PyOpenFinanceBR é uma biblioteca para acesso ao Open Finance Brasil',
    long_description=open('README.md', 'r').read(),
    install_requires=[
    ],
    tests_require=[
        'pytest',
    ],
)
