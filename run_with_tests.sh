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

cd ..

echo "--------------------------------------------------"
echo "EXAMPLE"
python augmentation_generator $1 $2 $3