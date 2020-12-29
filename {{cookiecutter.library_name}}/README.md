# {{cookiecutter.library_name}}  

## Purpose

Your motivation is described here.   

### Install

Python3.8+?  

```bat
pip install -e .
```

### Getting started.   

[tests/test_sample.py](./tests/test_sample.py) is the most basic and fundamental idea of the library is presented, 
so first of all, check this file.    


## For development

#### Execution of test.

* Execution of test: `pytest`
* Code formatter: `black`, `flake8`. 
* Dependency: See `setup.cfg`. 

#### Functions related to development  

Generally speaking, tests are the most crucial, coding format and type-annotations follow to that.   


* `setuptools` / `pip` : required
    - Command: `pip install .` 
    - Configuration: `setup.cfg`

* `pytest`: strongly recommended.
    - Command: `pytest`
    - Configuration: `pyproject.toml`
    - Purpose: Check the codes and displaying usage to the user.  
    - Comment: Only crude normal case check is desirable. 

* `black`: if possible. 
    - Command: `black`
    - Configuration: `pyproject.toml`
    - Purpose: Coding style check and revision.
    - Comment: It's easy.  

* `flake8`: if possible. 
    - Command: `pytest`
    - Configuration: `flake.ini`
    - Purpose: To eliminate unnecessary or unnatural codes.  

* `mypy`: if possible. 
    - Command: `mypy`
    - Configuration: `mypy.ini`
    - Purpose: To check type annotation.
    - Comment: It maybe a little bit hard to eliminate error completely.  
