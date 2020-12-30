"""This script prepares the development environment for the library.  
"""

from pathlib import Path
import subprocess
import venv
import os

_this_folder = Path(__file__).absolute().parent
_venv_folder = _this_folder / "venv"

def main(clear=True):
    venv.create(_venv_folder, clear=clear, with_pip=True)
    # OS dependency. 
    bin_path = _venv_folder / "Scripts"
    env = dict(os.environ)
    env["PATH"] = f"{bin_path};{env['PATH']}"
    def _run(*args, shell=True, **kwargs):
        return subprocess.run(*args, shell=True, env=env, **kwargs)
    _run("python -m pip install -U pip", shell=True)
    os.chdir(_this_folder)
    _run(f"pip install -e .", check=True)


if __name__ == "__main__":
    main()

