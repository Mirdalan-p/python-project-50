from gendiff.engine import generate_diff



json_ = ('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
yaml_ = ('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml')
mixed = ('tests/fixtures/file1.json', 'tests/fixtures/file2.yml')


def get_result(file):
    with open(file) as expected_result:
        return expected_result.read()

def test_generate_diff_json():
    assert generate_diff(json_[0], json_[1], 'stylish') == \
           get_result('tests/fixtures/result_stylish')
    assert generate_diff(json_[0], json_[1], 'plain') == \
           get_result('tests/fixtures/result_plain')
    assert generate_diff(json_[0], json_[1], 'json') == \
           get_result('tests/fixtures/result_json')


def test_generate_diff_yaml():
    assert generate_diff(yaml_[0], yaml_[1], 'stylish') == \
           get_result('tests/fixtures/result_stylish')
    assert generate_diff(yaml_[0], yaml_[1], 'plain') == \
           get_result('tests/fixtures/result_plain')
    assert generate_diff(yaml_[0], yaml_[1], 'json') == \
           get_result('tests/fixtures/result_json')

def test_generate_diff_mixed():
    assert generate_diff(mixed[0], mixed[1], 'stylish') == \
           get_result('tests/fixtures/result_stylish')
    assert generate_diff(mixed[0], mixed[1], 'plain') == \
           get_result('tests/fixtures/result_plain')
    assert generate_diff(mixed[0], mixed[1], 'json') == \
           get_result('tests/fixtures/result_json')