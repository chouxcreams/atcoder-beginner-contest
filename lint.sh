#usr/local/bin/bash

flake8 "$1"
isort --check --diff "$1"
black --check "$1"