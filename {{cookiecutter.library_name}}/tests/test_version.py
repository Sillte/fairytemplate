"""Version's attribute test.
"""

import pytest
import {{cookiecutter.library_name}}  

def test_version(): 
    assert hasattr({{cookiecutter.library_name}}, "__version__" )


if __name__ == "__main__":
    pytest.main(["--capture=no"])
