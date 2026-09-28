import unittest

import ai_research


class PackageTest(unittest.TestCase):
    def test_package_exposes_version(self) -> None:
        self.assertEqual(ai_research.__version__, "0.1.0")


if __name__ == "__main__":
    unittest.main()
