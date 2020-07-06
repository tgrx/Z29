HERE := $(shell pwd)
VENV := $(shell pipenv --venv)
SRC := ${HERE}
PYTHONPATH := ${SRC}

RUN := pipenv run
PY := ${RUN} python

ifneq ($(OS),Windows_NT)
	VERIFY_USERNAMES="${HERE}/verify_usernames.sh"
else
	VERIFY_USERNAMES=echo '*** cannot verify usernames on Windows, skipping... ***'
endif


.PHONY: format
format:
	${RUN} isort --virtual-env "${VENV}" --recursive --apply "${HERE}"
	${RUN} black "${HERE}"


.PHONY: wformat
format:
	isort --virtual-env "${VENV}" --recursive --apply "${HERE}"
	black "${HERE}"


.PHONY: qa
qa:
	@${VERIFY_USERNAMES}
	${RUN} pytest checks/
	${RUN} black --check .
	${RUN} isort --virtual-env "${VENV}" --recursive --check-only "${HERE}"
	${RUN} flake8
	${RUN} pylint solutions/ checks/


.PHONY: wqa
wqa:
	pytest checks/
	black --check .
	isort --virtual-env "${VENV}" --recursive --check-only "${HERE}"
	flake8
	pylint solutions/ checks/
