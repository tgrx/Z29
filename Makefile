HERE := $(shell pwd)
VENV := $(shell pipenv --venv)
SRC := ${HERE}
PYTHONPATH := ${SRC}

RUN := pipenv run
PY := ${RUN} python


.PHONY: format
format:
	${RUN} isort --virtual-env "${VENV}" --recursive --apply "${HERE}"
	${RUN} black "${HERE}"


.PHONY: qa
qa:
	${HERE}/qa.sh
