"""Creating a package."""

from setuptools import setup

extra_packages = {
    'testing': ['ipython', 'pytest', 'pytest-watch', 'tox']
}

setup(
    name='Linked_List',
    description='A Single Link-List.',
    version='0.5',
    author='Orphelia Yin and Alex Short',
    author_email='ajshort2010@hotmail.com',
    py_modules=['linked_list'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require=extra_packages,
    entry_points={'console_scripts': ['linked_list = linked_list:main']}
)
