from setuptools import setup
setup(
    name = 'aggiestack',
    version = '0.2',
    packages = ['aggiestack_project','aggiestack_project.functions','aggiestack_project.definitions','aggiestack_project.database'],
    entry_points = {
        'console_scripts': [
            'aggiestack = aggiestack_project.__main__:main'
        ]
    })