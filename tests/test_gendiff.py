from gendiff.comparer import generate_diff
import pytest

json_ = ('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
yaml_ = ('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml')
mixed = ('tests/fixtures/file1.json', 'tests/fixtures/file2.yml')


def read_file(file):
    with open(file) as expected_result:
        return expected_result.read()


@pytest.mark.parametrize("first,second", [(json_[0], yaml_[1]), (json_[0], json_[1]), (yaml_[0], yaml_[1])])
def test_generate_diff(first, second):
    assert generate_diff(first, second) == \
        read_file(('tests/fixtures/result_stylish'))
    assert generate_diff(first, second, 'json') == \
        read_file(('tests/fixtures/result.json'))
    assert generate_diff(first, second, 'plain') == \
        read_file(('tests/fixtures/result_plain'))
    assert generate_diff(first, first) != \
        read_file(('tests/fixtures/result_stylish'))
