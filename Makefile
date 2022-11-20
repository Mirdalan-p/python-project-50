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

try:
	gendiff /home/mirdalan/hexlet-projects/python-project-50/tests/fixtures/file1_recursive.yaml /home/mirdalan/hexlet-projects/python-project-50/tests/fixtures/file2_recursive.yaml

try2:
	gendiff /home/mirdalan/hexlet-projects/python-project-50/tests/fixtures/file1.json /home/mirdalan/hexlet-projects/python-project-50/tests/fixtures/file2.json