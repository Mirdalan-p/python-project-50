install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 gendiff
test:
	poetry run pytest
	
test-coverage:
	poetry run pytest --cov=gendiff tests/ --cov-report xml

project-install:
	poetry build
	python3 -m pip install --user dist/*.whl --force-reinstall

stylish-complex:
	gendiff tests/fixtures/file1_recursive.yaml tests/fixtures/file2_recursive.yaml

stylish-flat:
	gendiff tests/fixtures/file1.json tests/fixtures/file2.json

plain:
	gendiff -f plain tests/fixtures/file1_recursive.yaml tests/fixtures/file2_recursive.yaml