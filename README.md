# blackjack

A pet project to exercise:

    * pytest
    * pytest-cov
    * test package in development mode
    * freeze package
    * create dist package
    * test dist package


#### python venv

```shell
(shell)$ source python-venv/bin/activate
(venv)$ python -m pip install -r requirements.txt
```

#### pytest

```shell \tiny
(venv)$ pytest --verbose

```

#### pytest-cov

```shell
(venv)$ pytest --cov blackjack --cov-report=term-missing

```

#### test package in development mode

```shell
(venv)$ python setup.py develop
(venv)$ python
>>> from blackjack.common import card_score
>>> card_score("JA")
21
>>>

```

#### freeze package
```shell
 (venv)$ python -m pip freeze | tee > requirements.txt
 
 ```

 #### create dist package
 ```shell
 # python -m pip install wheel if bdist_wheel is not recognized
 (venv)$ python setup.py bdist_wheel
 
 ```

 #### test dist package
 ```shell
 (venv)$ deactivate
 (shell)$ python3 -m pip install dist/blackjack-0.0.1-py2.py3-none-any.whl
 (shell)$ python3
>>> from blackjack.common import card_score
>>> card_score("JA")
21
>>>

```
