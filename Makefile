PYTHON=python3.6

VENV=venv
BIN=$(VENV)/bin

.PHONY: package clean test


package: test microhtml/__init__.pyi
	$(BIN)/python setup.py sdist

upload: package
	$(BIN)/pip install twine
	$(BIN)/twine upload dist/*

$(VENV):
	$(PYTHON) -m venv $(VENV)
	$(BIN)/pip install -r requirements.txt

microhtml/__init__.pyi: $(VENV) microhtml/*.py
	$(BIN)/pip install mypy
	install -d out
	$(BIN)/stubgen microhtml/__init__.py
	mv out/microhtml/__init__.pyi microhtml/
	$(BIN)/python microhtml/__init__.py >> microhtml/__init__.pyi
	rmdir out/*
	rmdir out

test: $(VENV)
	$(BIN)/pip install nose
	$(BIN)/nosetests microhtml_test.py

clean:
	rm -rf dist *.egg-info microhtml/__pycache__ __pycache__ $(VENV) out build microhtml/*.pyi
