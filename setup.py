"""Creating a package."""

from setuptools import setup

dependencies = ['ipython', 'pytest', 'pytest-watch', 'tox']

setup(
    name='Stack',
    description='A Stack.',
    version='0.5',
    author='Orphelia Yin and Alex Short',
    author_email='ajshort2010@hotmail.com',
    py_modules=['stack'],
    package_dir={'': 'src'},
    install_requires=dependencies,
    entry_points={'console_scripts': ['stack = stack:main']}
)
