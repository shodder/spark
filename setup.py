'''
spark
----

Python Small Plugin Sytem
'''

from setuptools import setup, find_packages


setup(
    name='spark',
    version='0.1',
    url='https://github.com/simonhodder/spark',
    license='GNU V3',
    author='Simon Hodder',
    author_email='hodder.simon@gmail.com',
    description='Python Small Plugin System',
    long_description=__doc__,
    include_package_data=True,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'click',
        'logbook',
        'sqlalchemy',
    ],
    tests_require=[
        'pytest',
        'pytest-xdist',
        'pytest-cov',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    extras_require={
        'testing': ['pytest', 'pytest-xdist', 'pytest-cov', ],
    },
    entry_points={
        'console_scripts': [
            'spark=spark.cli:cli',
        ],
    },
)
