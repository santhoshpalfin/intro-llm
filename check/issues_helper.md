# For fixing issues when running the code

## To create virtual environment run this
virtualenv venv --python=3.11

## To activate the virtual env 
### in the powershell
venv/scripts/activate.ps1
### windows command shell
venv/scripts/acivate.bat
### Mac
venv/bin/activate

## For issue with ssl run below. Ensure you are in the virtual env when running these.

pip install certifi
pip install --trusted-host=pypi.org --trusted-host=files.pythonhosted.org  pip-system-certs

## or try this
pip install pip-system-certs
pip install --upgrade certifi

