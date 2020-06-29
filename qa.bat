pipenv run pytest checks/
pipenv run black --check .
pipenv run flake8
pipenv run pylint solutions/ checks/
