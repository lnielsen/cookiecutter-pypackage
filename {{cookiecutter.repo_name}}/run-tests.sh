# This file is part of {{ cookiecutter.project_name }}
# Copyright (C) {{ cookiecutter.year }} {{ cookiecutter.copyright_holder }}.
#
# {{ cookiecutter.project_name }} is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

pep257 {{ cookiecutter.repo_name }} && \
sphinx-build -qnNW docs docs/_build/html && \
python setup.py test && \
sphinx-build -qnNW -b doctest docs docs/_build/doctest
