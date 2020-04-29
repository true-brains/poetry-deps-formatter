What is it?
=================

This is sort of a plugin for poetry which add comments with description for every dependency in ``pyproject.toml`` based on ``poetry``.lock file.

So your dependencies will look like

.. code-block::

    [tool.poetry.dependencies]
    python = "^3.7"
    toml = "^0.10.0"            # Python Library for Tom's Obvious, Minimal Language ·· https://pypi.org/project/toml/

    [tool.poetry.dev-dependencies]
    pytest = "^5.2"             # pytest: simple powerful testing with Python ·· https://pypi.org/project/pytest/
    mock = "^4.0.2"             # Rolling backport of unittest.mock for all Pythons ·· https://pypi.org/project/mock/



How to install
------------------------

Install via poetry

.. code-block::

    poetry add --dev poetry-deps-formatter


Install via PIP

.. code-block::

    pip install poetry-deps-formatter



Then you have to add it to ``tool.poetry.scripts`` section of your ``pyproject.toml`` file.

.. code-block::

    [tool.poetry.scripts]
    format = "poetry_deps_formatter:formatter"


How to use
------------------------

.. code-block::

    poetry run formatter