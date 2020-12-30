"""Virtual Environment Handler. 

Environment  

(2020-08-30) Currently, this module works only for Windows. 

"""
import venv
from pathlib import Path
import subprocess
import os


class EnvController:
    """Environment Path Solver.
    This class receives `Path` which points to a virtual environment. 

    * `@property` returns `Path` which corresponds the command.     
    * `method` performs typical operations to the virtual environment.
    """

    def __init__(self, folder):
        self.folder = Path(folder).absolute()
        assert os.name == "nt"

        if not (self.folder / "Scripts").exists():
            raise ValueError(f"`{self.folder}` is not a virtual env.")

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

    @property
    def bin(self) -> Path:
        return self.folder / "Scripts"
        

    def run(self, *args, shell=True, **kwargs):
        """This is a wrapper for `subprocess.run`, 
        with intended to called within the virtual environment. 

        Note
        -------------------------
        Default `shell` is `True`.  
        """

        assert "env" not in kwargs, "`env` is not accepted."
        env = dict(os.environ)
        env["PATH"] = f"{self.bin};{env['PATH']}"
        return subprocess.run(*args, shell=True, env=env, **kwargs)

    
    @classmethod
    def ready_development(cls,
                          library_folder: Path,
                          env_folder: Path = None):
        """Prepare the development virtual environment.
        """
        if output_folder is None:
            output_folder = Path(library_folder) / "venv"

        cls.create(env_folder, with_pip=True)
        cont = EnvController(env_folder)
        cont.run("python -m pip install -U pip", shell=True)

        os.chdir(library_folder)
        cont.run(f"pip install -e .", check=True)


    @classmethod
    def create(cls,
               env_dir,
               system_site_packages=False,
               clear=False,
               symlinks=False,
               with_pip=True,
               prompt=None):
        """ Crude wrapper for `venv.create`.  

        However, default `with_pip` is True.
        """
        venv.create(env_dir,
                    system_site_packages=system_site_packages,
                    clear=clear,
                    symlinks=symlinks,
                    with_pip=with_pip,
                    prompt=prompt)
        return cls(env_dir)


if __name__ == "__main__":
    cont = EnvController.create("__venv__")
    cont.run("pip install pytest")
    cont.run("where pip")

