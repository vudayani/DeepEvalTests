import pytest
from typing import List
from deepeval import assert_test
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCase
from deepeval.test_case import LLMTestCaseParams

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

ACTUAL_OUTPUT_1 = read_file('../../spring-petclinic/README-ai-spring-petclinic.md')
EXPECTED_OUTPUT_1 = read_file('../../spring-petclinic/README-ai-jpa-expected-output.md')

ACTUAL_OUTPUT_2 = read_file('../../fortune-service/README-ai-fortune-service.md')
EXPECTED_OUTPUT_2 = read_file('../../fortune-service/README-ai-jpa-expected-output.md')

def test_case_boot_3():
    correctness_metric = GEval(
        name="Correctness",
        evaluation_steps=[
            "Check whether 'actual output' has all the files or code snippets(Controlller, service, entity, repository) from 'expected output'",
            "The entity class import statements should use 'jakarta.persistence' instead of 'javax.persistence'",
            "Check if the correct dependeniencies are added in the 'pom.xml' file",
        ],
        evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT],
        threshold=0.8
    )

    # assert_test(test_case, [correctness_metric])
    test_case = LLMTestCase(
        input="JPA functionality",
        actual_output=ACTUAL_OUTPUT_1,
        expected_output=EXPECTED_OUTPUT_1
    )

    correctness_metric.measure(test_case)
    print(correctness_metric.score)
    print(correctness_metric.reason)
    assert_test(test_case, [correctness_metric])


def test_case_boot_2():
    correctness_metric = GEval(
        name="Correctness",
        evaluation_steps=[
            "Check whether 'actual output' has all the files or code snippets(Controlller, service, entity, repository) from 'expected output'",
            "The entity class import statements should use 'javax.persistence'",
            "Check if the correct dependeniencies are added in the 'pom.xml' file",
        ],
        evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT],
        threshold=0.8
    )

    # assert_test(test_case, [correctness_metric])
    test_case = LLMTestCase(
        input="JPA functionality",
        actual_output=ACTUAL_OUTPUT_2,
        expected_output=EXPECTED_OUTPUT_2
    )

    correctness_metric.measure(test_case)
    print(correctness_metric.score)
    print(correctness_metric.reason)
    assert_test(test_case, [correctness_metric])

