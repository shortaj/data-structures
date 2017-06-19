"""Creating a package."""

from setuptools import setup

tests_require = ['ipython', 'pytest', 'pytest-watch', 'tox']

setup(
    name='Deque',
    description='A The Deque is the double-link list of the\
     Queue link-link data structure.',
    version='0.5',
    author='Ophelia Yin and Alex Short',
    author_email='ajshort2010@hotmail.com',
    py_modules=['deque'],
    package_dir={'': 'src'},
    install_requires= '',
    extras_require={
        'testing': tests_require,
    },
)
