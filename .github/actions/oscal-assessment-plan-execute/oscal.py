import os, yaml
from pathlib import Path
from yaml import load


if 'ASSESSMENT_PLAN' not in os.environ:
    exit("Assessment Plan Environment Variable Not Found")


model = os.environ['ASSESSMENT_PLAN']


def test_the_load():
    """Load a model for interpretation"""
    model_file = Path(os.environ['ASSESSMENT_PLAN']).read_text()
    model = yaml.safe_load(model_file)
    print(model)


def test_to_pass():
    """Passing Test"""
    assert True == True