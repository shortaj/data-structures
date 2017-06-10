"""Setup for data structure modules."""


from setuptools import setup


setup(
    name='data structures',
    description='homework assignments',
    version='0.1',
    author='',
    author_email='',
    license='MIT',
    py_modules=['binheap', 'deque', 'graph', 'graph2'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={
        'testing': ['ipython', 'pytest', 'pytest-watch', 'pytest-cov', 'tox']
    }
    # entry_points={
    #     'console_scripts': [
    #         'client = client:client'
    #     ]
    # }
)
