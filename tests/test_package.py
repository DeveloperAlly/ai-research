import importlib.metadata
from pathlib import Path
import tomllib
import unittest

import ai_research


class PackageTest(unittest.TestCase):
    def test_package_exposes_version(self) -> None:
        self.assertEqual(ai_research.__version__, "0.1.0")

    def test_package_version_matches_project_metadata(self) -> None:
        with Path("pyproject.toml").open("rb") as pyproject_file:
            project_metadata = tomllib.load(pyproject_file)["project"]

        self.assertEqual(project_metadata["version"], ai_research.__version__)

    def test_installed_distribution_metadata_matches_package_version(self) -> None:
        try:
            installed_version = importlib.metadata.version("ai-research")
        except importlib.metadata.PackageNotFoundError:
            self.skipTest("distribution metadata is only available after installation")

        self.assertEqual(installed_version, ai_research.__version__)


if __name__ == "__main__":
    unittest.main()
