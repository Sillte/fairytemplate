"""Version's attribute test.
"""

import pytest
import fairytool


def test_version():
    assert hasattr(fairytool, "__version__")


if __name__ == "__main__":
    pytest.main(["--capture=no"])
