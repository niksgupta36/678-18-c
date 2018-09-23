from setuptools import setup
setup(
    name = 'aggiestack',
    version = '0.1.0',
    packages = ['aggiestack_project','aggiestack_project.commands','aggiestack_project.utility'],
    entry_points = {
        'console_scripts': [
            'aggiestack = aggiestack_project.__main__:main'
        ]
    })