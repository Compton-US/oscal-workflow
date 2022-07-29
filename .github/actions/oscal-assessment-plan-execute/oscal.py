import os, yaml
from yaml import load


if 'ASSESSMENT_PLAN' not in os.environ:
    exit("Assessment Plan Environment Variable Not Found")


model = os.environ['ASSESSMENT_PLAN']


def test_the_load():
    """Load a model for interpretation"""
    model = yaml.load(os.environ['ASSESSMENT_PLAN'])
    print(model)


def test_to_pass():
    """Passing Test"""
    assert True == True