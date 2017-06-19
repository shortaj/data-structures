"""Creating a package."""

from setuptools import setup

extra_packages = {
    'tsting': ['ipython', 'pytest', 'pytest-watch', 'tox']
}

setup(
    name='Stack',
    description='A Stack.',
    version='0.5',
    author='Orphelia Yin and Alex Short',
    author_email='ajshort2010@hotmail.com',
    py_modules=['stack', 'linked_list'],
    package_dir={'': 'src'},
    extras_require=extra_packages,
    entry_points={'console_scripts': ['stack = stack:main']}
)
