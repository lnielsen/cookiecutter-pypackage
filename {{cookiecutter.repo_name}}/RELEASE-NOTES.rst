{{ '=' * (cookiecutter.project_name|length + cookiecutter.version|length + 4) }}
 {{ cookiecutter.project_name }} v{{ cookiecutter.version }}
{{ '=' * (cookiecutter.project_name|length + cookiecutter.version|length + 4) }}

{{ cookiecutter.project_name }} v{{ cookiecutter.version }} was released on {{ cookiecutter.release_date }}

About
-----

{{ cookiecutter.project_short_description }}

Installation
------------

   $ pip install {{ cookiecutter.repo_name }}

What's new
----------

Documentation
-------------

   http://pythonhosted.org/{{ cookiecutter.repo_name }}/

Website
-------

   https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

