"""Creating a package."""

from setuptools import setup

dependencies = ['ipython', 'pytest', 'pytest-watch', 'tox']

setup(
    name='Queue',
    description='A Queue Link-List.',
    version='0.5',
    author='Orphelia Yin and Alex Short',
    author_email='ajshort2010@hotmail.com',
    py_modules=['que_'],
    package_dir={'': 'src'},
    install_requires=dependencies,
    entry_points={'console_scripts': ['que_ = que_:main']}
)
