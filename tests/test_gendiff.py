from gendiff.scripts.make_diff import generate_diff
from gendiff.formatters.get_stylish import make_stylish
from gendiff.formatters.get_plain import make_plain
from gendiff.formatters.get_json import make_json
from gendiff.scripts.parser import make_parse


json_flat = (make_parse('tests/fixtures/file1.json'), make_parse('tests/fixtures/file2.json'))
flat_yaml = (make_parse('tests/fixtures/file3.yaml'), make_parse('tests/fixtures/file4.yaml'))
yaml_recursive = (make_parse('tests/fixtures/file1_recursive.yaml'), make_parse('tests/fixtures/file2_recursive.yaml'))


def get_result(file):
    with open(file) as expected_result:
        return expected_result.read()

def test_generate_diff_with_flat_json():
    assert make_stylish(generate_diff(json_flat)) == \
           get_result('tests/fixtures/output_1.txt')

def test_stylish():
    assert make_stylish(generate_diff(json_flat)) == \
           get_result('tests/fixtures/output_1.txt')
    assert make_stylish(generate_diff(flat_yaml)) == \
           get_result('tests/fixtures/output_1.txt')
    assert make_stylish(generate_diff(yaml_recursive)) == \
           get_result('tests/fixtures/output_stylish.txt')

def test_plain():
    assert make_plain(generate_diff(yaml_recursive)).strip() == \
           get_result('tests/fixtures/output_plain.txt')

def test_json_formatter():
    assert make_json(generate_diff(yaml_recursive)).strip() == \
           get_result('tests/fixtures/output.json')