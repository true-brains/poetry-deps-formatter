import pytest
import re
from poetry_deps_formatter import DependenciesFormatter

pytestmark = pytest.mark.unit


class TestFormatter:
    @pytest.fixture()
    def formatter(self):
        return DependenciesFormatter()

    def test__describe_dependency__comment_added(self, formatter):
        package = {'description': 'pytest: simple powerful testing with Python', 'name': 'pytest'}
        package_name = package['name']
        dependency = 'pytest = "^5.2"'

        text = re.sub(
            f'^({package_name}[\s|=].*").*$',
            formatter._describe_dependency(package),
            dependency,
            flags=re.MULTILINE)

        assert text == ('pytest = "^5.2"                                   '
                        '# pytest: simple powerful testing with Python ·· https://pypi.org/project/pytest/ ')
