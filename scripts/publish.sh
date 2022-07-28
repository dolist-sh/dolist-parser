#!/bin/bash

set -e

PYPI_USERNAME=__token__
API_TOKEN=$1

poetry publish --build --username $PYPI_USERNAME --password $API_TOKEN

exit 0

