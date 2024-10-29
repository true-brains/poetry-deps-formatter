import os
import toml
import re
from typing import Callable


class DependenciesFormatter:
    parsed_lock = None

    def _describe_dependency(self, package) -> Callable:
        def repl(m):
            return f'{m.group(1):50s}# {package["description"]} ·· https://pypi.org/project/{package["name"]}/ '

        return repl

    def _parse_lock(self, poetry_lock_file):
        with open(f'{poetry_lock_file}', 'r') as file:
            text = file.read()
            return toml.loads(text)

    def __call__(self):
        cwd = os.getcwd()

        poetry = os.path.join(cwd, 'poetry.lock')
        self.parsed_lock = self._parse_lock(poetry)

        pyproject = os.path.join(cwd, 'pyproject.toml')
        with open(f'{pyproject}', 'r+') as file:
            text = file.read()

            packages = self.parsed_lock['package']
            for package in packages:
                name = package['name']
                text = re.sub(
                    fr'^({name}[\s|=].*").*$',
                    self._describe_dependency(package),
                    text,
                    flags=re.MULTILINE)
            file.seek(0)
            file.write(text)
            file.truncate()


formatter = DependenciesFormatter()
