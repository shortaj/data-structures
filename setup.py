"""Creating a package."""

from setuptools import setup

extra_packages = {
    'testing': ['ipython', 'pytest', 'pytest-watch', 'tox']
}

setup(
    name='Double_Link_List',
    description='A Double Link-List.',
    version='0.5',
    author='Ophelia Yin and Alex Short',
    author_email='ajshort2010@hotmail.com',
    py_modules=['dll'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require=extra_packages,
    entry_points={'console_scripts': ['dll = doubly_link:main']}
)
