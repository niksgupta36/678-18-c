from setuptools import setup
setup(
    name = '678-18-c',
    version = '0.1.0',
    packages = ['aggiestack'],
    entry_points = {
        'console_scripts': [
            '678-18-c = aggiestack.__main__:main'
        ]
    })