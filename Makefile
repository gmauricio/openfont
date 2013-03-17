# OpenFont - Font Packaging Format
# https://github.com/heynemann/openfont

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

test:
	@PYTHONPATH=.:$$PYTHONPATH pyvows -vvv --cover --cover_package="openfont" --profile vows/

setup:
	@pip install -r requirements.txt --use-mirrors
