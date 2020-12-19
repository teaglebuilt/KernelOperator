TEST_PATH=./

clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info

lint:
	flake8 --exclude=.tox
test: clean-pyc
	py.test --verbose --color=yes $(TEST_PATH)