# -*- coding: utf-8 -*-
#
# This file is part of {{ cookiecutter.project_name }}
# Copyright (C) {{ cookiecutter.year }} {{ cookiecutter.copyright_holder }}.
#
# {{ cookiecutter.project_name }} is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""{{cookiecutter.project_short_description}}"""

import os
import re
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):

    """Integration of PyTest with setuptools."""

    user_options = [('pytest-args=', 'a', 'Arguments to pass to py.test')]

    def initialize_options(self):
        """Initialize options."""
        TestCommand.initialize_options(self)
        try:
            from ConfigParser import ConfigParser
        except ImportError:
            from configparser import ConfigParser
        config = ConfigParser()
        config.read("pytest.ini")
        self.pytest_args = config.get("pytest", "addopts").split(" ")

    def finalize_options(self):
        """Finalize options."""
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        """Run tests."""
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


# Get the version string.  Cannot be done with import!
with open(os.path.join('{{ cookiecutter.repo_name }}', 'version.py'), 'rt') as f:
    version = re.search(
        '__version__\s*=\s*"(?P<version>.*)"\n',
        f.read()
    ).group('version')


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('CHANGES.rst') as history_file:
    history = history_file.read().replace('.. :changes:', '')

requirements = [
]

extras_requirements = {}

test_requirements = [
    'pytest-cache>=1.0',
    'pytest-cov>=2.0.0',
    'pytest-isort>=0.1.0',
    'pytest-pep8>=1.0.6',
    'pytest>=2.8.0',
    'coverage>=4.0',
]

setup(
    name='{{ cookiecutter.repo_name }}',
    version=version,
    description=__doc__,
    long_description=readme + '\n\n' + history,
    author="{{ cookiecutter.full_name }}",
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=[
        '{{ cookiecutter.package_name }}',
    ],
    include_package_data=True,
    install_requires=requirements,
    extras_require=extras_requirements,
    license="BSD",
    zip_safe=False,
    keywords='{{ cookiecutter.repo_name }}',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    tests_require=test_requirements,
    cmdclass={'test': PyTest},
)
