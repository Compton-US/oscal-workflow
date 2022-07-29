import os, yaml
from pathlib import Path
from yaml import load

if 'ASSESSMENT_PLAN' not in os.environ:
    exit("Assessment Plan Environment Variable Not Found")

model = os.environ['ASSESSMENT_PLAN']

content = Path(model).read_text()
plan = yaml.safe_load(content)

print("*"*100)
print(model)
print(plan)


