# Python TDD

A pet project to exercise:

    * pytest
    * pytest-cov
    * test package in development mode
    * freeze package
    * create dist package
    * test dist package


#### python3 virtual env

```shell
(shell)$ python3 -m venv python3-venv
(shell)$ source python3-venv/bin/activate
```
Once inside the venv python3 will be the default version
```
(venv)$ python --version
Python 3.10.6
```

#### pytest

```shell \tiny
(venv)$ python -m pip install -r requirements.txt
(venv)$ pytest --verbose

```

#### pytest-cov

```shell
(venv)$ pytest --cov blackjack --cov-report=term-missing

```

#### test package in development mode

```shell
(venv)$ python setup.py develop --user
(venv)$ python
>>> from blackjack.common import card_score
>>> card_score("JA")
21
>>>

```

#### freeze package
```shell
 (venv)$ python -m pip freeze | tee > packageing.txt
 
 ```

 #### create dist package
 ```shell
 (venv)$ python setup.py bdist_wheel
 # run "python -m pip install wheel" if bdist_wheel is not recognized
 (venv)$ python -m pip install wheel
 ```
 A wheel file will be produced in the dist/ folder

 #### test dist package
 ```shell
 (venv)$ deactivate
 (shell)$ python -m pip install dist/blackjack-0.0.1-py2.py3-none-any.whl
 (shell)$ python
>>> from blackjack.common import card_score
>>> card_score("JA")
21
>>>

```

#### Automated Github Action

    A github action yaml file is in pace to run pytest coverage.
    Passing criteria with 100% test pass and 100% code coverage are set in .coveragerc
    PR with any failure will be blocked. 