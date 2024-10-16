from tut4.examResult import ExamResult
import pytest
import json

class TestResult:

    @staticmethod
    def load_student_data_from_json(file_path):
        with open(file_path) as json_file:
            return json.load(json_file)

    @classmethod
    def setup_class(cls):
        cls.result = ExamResult()
        cls.result.connect('student_result.json')  # Load data once for the whole class

    @pytest.mark.parametrize("student", 
        [pytest.param(student) for student in load_student_data_from_json('student_result.json')])
    def test_record(self, student):
        # Test logic
        assert self.result.get_div1(student['Total']), f"Failed for student: {student['']}"