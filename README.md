# fairytemplate

This is a template for personal python library.   

## Memorandum 


* `flake8`:
* `black`:
* `mypy`:

I'd like to incorporate configuration of [PEP621](https://www.python.org/dev/peps/pep-0621/).      
After the above is installed, I'll do my best!  

### Configuration files for provided functions.

* `pytest with coverage`:
    - `pyproject.toml`

* `flake8`:
    - `.flake8`
    - If it would become possible, migrate to `pyproject.toml`.

* `mypy`:
    - `pyproject.toml`. 

* `setuptools` (Building tool):
    - `setup.cfg`.
    - If it would become possible, migrate to `pyproject.toml`.

* `black`:
    - `pyproject.toml`.

## Usage

This repository uses [cookiecutter](https://github.com/cookiecutter/cookiecutter).  

```
pip install cookiecutter
cookiecutter https://github.com/sillte/fairytemplate
```

## Test

Only basic workflow is tested.     

```
pip install . 
pytest
```


## Policy for development
* My environment is Windows 10, and only this environment is considered. 

* Setting files are described in `pyproject.toml` as much as possible.  
    - Since a personal repository are expected to have so much dependencies that the management of a single setting `toml` is difficult to handle. 

* Input with `cookiecutter` should be minimized. 
    - This is a personal repository, narrow scope for easiness!


