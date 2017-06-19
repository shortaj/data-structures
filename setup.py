"""The setup file for Deque, defining the required packages and console commands."""
from setuptools import setup, find_packages

tests_require = [
    'pytest',
    'pytest-cov',
    'tox'
]

setup(
    name='Deque Data Structure',
    version='0.0',
    description='Deque Data Structure',
    author='Orphelia and Alex',
    author_email='ajshort2010@hotmail.com',
    url='',
    keywords='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires='',
)
