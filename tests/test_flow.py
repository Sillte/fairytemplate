"""Workflow test for `fairytemplate`.  

Requirement: `git`. 

Here, we'd like to confirm that 
the initialized library accepts basic operations
such as `pip install .`, `pytest`.  

If this test passes, normal usage is assured to be correct.
(Though, only normal cases are considered!)

"""

import pytest
from pathlib import Path 
import os
import venv
import subprocess
import shutil
import cookiecutter

from cookiecutter.generate import generate_context, generate_files

_this_folder = Path(__file__).absolute().parent

class EnvHandler:
    def __init__(self, folder):
        self.folder = Path(folder).absolute()
        assert (self.folder / "Scripts.bat")

    @property
    def pip(self) -> Path:
        return self.folder / "Scripts/pip3.exe" 

    @property
    def pytest(self) -> Path:
        return self.folder / "Scripts/pytest.exe" 

    @property
    def flake8(self) -> Path:
        return self.folder / "Scripts/flake8.exe" 

    @property
    def mypy(self) -> Path:
        return self.folder / "Scripts/mypy.exe" 

    @property
    def black(self) -> Path:
        return self.folder / "Scripts/black.exe" 

    @property
    def python(self) -> Path:
        return self.folder / "Scripts/python.exe" 


@pytest.fixture(scope="session")
def repo_folder():
    def _inner(folder):
        if (folder / ".git").exists():
            return folder
        return _inner(folder.parent)
    return _inner(_this_folder)

@pytest.fixture(scope="session")
def output_folder():
    folder = _this_folder / "_test_flow_output"
    if folder.exists():
        shutil.rmtree(folder)
    return folder


@pytest.fixture(scope="session")
def env_folder():
    """Return the virtual environment for the trial environment. 
    To reduce the time, crude re-use mechanism is adopted. 
    """
    folder = _this_folder / "__venv__"
    if not folder.exists():
        venv.create(folder, with_pip=True)
    return folder


def test_flow(repo_folder, output_folder, env_folder):
    """Crudely performs basic processing of library. 
    """
    assert repo_folder.exists()
    config_path = repo_folder / "cookiecutter.json"
    assert config_path.exists()

    context = generate_context(config_path)
    generate_files(repo_folder, context=context, output_dir=output_folder)

    library_name = context["cookiecutter"]["library_name"]
    library_folder = output_folder / library_name
    assert library_folder.exists()

    # Git (for setuptools_scm)
    subprocess.run(f"git init", cwd=library_folder)

    # pip.
    env_handler = EnvHandler(env_folder)
    python_path = env_handler.python
    subprocess.run(f"{python_path} -m pip install -U pip")
    pip_path = env_handler.pip
    os.chdir(library_folder)
    subprocess.run(f"{pip_path} install -e .")

    # pytest with coverage.
    pytest_path = env_handler.pytest
    subprocess.run(f"{pytest_path}", check=True, cwd=library_folder)
    assert (library_folder / "htmlcov").exists(), "Coverage."

    # flake8.
    flake8_path = env_handler.flake8
    subprocess.run(f"{flake8_path}", cwd=library_folder)

    # mypy.
    mypy_path = env_handler.mypy
    subprocess.run(f"{mypy_path} .", cwd=library_folder)

    # black.
    black_path = env_handler.black
    subprocess.run(f"{black_path} .", cwd=library_folder)

    subprocess.run(f'{python_path} {library_folder / "ready.py"}', shell=True)

if __name__ == "__main__":
    assert pytest.__version__ >= "6.0", "pyproject.toml"
    pytest.main(["--capture=no"])
