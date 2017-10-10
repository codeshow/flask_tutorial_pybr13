from setuptools import setup

requirements = [
    'flask',
    'import_string',
    'pymongo',
    'tinymongo',
    'tinydb_serialization',
    'dynaconf',
    'awesome_slugify',
    'mistune',
    'flask_simplelogin',
    'flask_admin',
    'flask_wtf',
    'flask_bootstrap',
    'PyYAML',
    'gunicorn'
]


setup(
    name='cms',
    version='0.0.1',
    description="A simple CMS in Flask",
    author="Bruno Rocha",
    author_email='rochacbruno@gmail.com',
    url='https://github.com/cursodepythonoficial/',
    packages=['cms'],
    package_dir={'cms': 'cms'},
    entry_points={
        'console_scripts': [
            'cms=cms.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements
)
