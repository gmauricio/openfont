setup:
	@pip install -r requirements.txt

test:
	@PYTHONPATH=.:$$PYTHONPATH pyvows -vvv --cover --cover_package="openfont" --profile vows/
