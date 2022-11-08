from gendiff.scripts.make_diff import generate_diff



def get_result(file):
    with open(file) as expected_result:
        return expected_result.read()

def test_generate_diff_with_lesson_data():
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == \
           get_result('tests/fixtures/output_1.txt')