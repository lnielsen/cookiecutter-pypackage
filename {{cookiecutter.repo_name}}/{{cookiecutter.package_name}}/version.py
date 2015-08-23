# -*- coding: utf-8 -*-
#
# This file is part of {{ cookiecutter.project_name }}
# Copyright (C) {{ cookiecutter.year }} {{ cookiecutter.copyright_holder }}.
#
# {{ cookiecutter.project_name }} is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Version information for {{ cookiecutter.project_name }}.

This file is imported by ``{{ cookiecutter.repo_name }}.__init__``, and parsed by
``setup.py`` as well as ``docs/conf.py``.
"""

# Do not change the format of this next line. Doing so risks breaking
# setup.py and docs/conf.py

__version__ = "{{ cookiecutter.version }}.dev{{ cookiecutter.release_date.replace('-', '') }}"
