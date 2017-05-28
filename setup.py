from setuptools import setup
"""Setup for linked list, que and stack"""

setup(
    name=['linked_list.py', 'stack.py', 'que_.py'],
    description="build a linked list, stack and queue",
    version='0.1',
    author="Ophelia and Alex",
    license='MIT',
    py_modules=['mailroom'],
    #install_requires= ,
    package_dir={'': 'src'},
    extras_require={'testing': ['pytest', 'pytest-cov', 'tox']},
    #entry_points={'console_scripts': }
)
