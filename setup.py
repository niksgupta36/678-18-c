from setuptools import setup
setup(
    name = 'aggiestack',
    version = '0.1.0',
    packages = ['aggiestack_project'],
    entry_points = {
        'console_scripts': [
            'aggiestack = aggiestack_project.__main__:main'
        ]
    })