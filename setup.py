from setuptools import setup, find_packages

setup(
    name='Stripper',
    version='0.1',
    packages=find_packages(),
    package_data={},
    scripts=[
        'bin/stripper.py',
    ],
)
