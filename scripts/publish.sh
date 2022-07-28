#!/bin/bash

set -e

API_TOKEN=$1

export PYPI_USERNAME=__token__
export PYPI_PASSWORD="${API_TOKEN}"

poetry publish --build --username $PYPI_USERNAME --password $PYPI_PASSWORD

exit 0

