"""Creating a package."""

from setuptools import setup

dependencies = ['ipython', 'pytest', 'pytest-watch', 'tox']

setup(
    name='Deque',
    description='A The Deque is the double-link list of the\
     Queue link-link data structure.',
    version='0.5',
    author='Ophelia Yin and Alex Short',
    author_email='ajshort2010@hotmail.com',
    py_modules=['deque'],
    package_dir={'': 'src'},
    install_requires=dependencies,
    entry_points={'console_scripts': ['deque = deque:main']}
)
