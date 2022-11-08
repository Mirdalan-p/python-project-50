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
	poetry run pytest -vv

coverage-report:
	poetry run pytest --cov=src