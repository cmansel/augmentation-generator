#!/bin/bash
cd "$(dirname "$0")"

echo "--------------------------------------------------" 
echo "LINTING"
pylint ./src

echo "--------------------------------------------------"
echo "TYPECHECKING"
mypy ./src

echo "--------------------------------------------------"
echo "INTEGRATIONTESTS"
pytest

echo "--------------------------------------------------"
echo "DEMO"
python __main__.py $1 $2 $3