#%%
import os, yaml, hashlib, subprocess
from pathlib import Path
from yaml import load

root_path = ""

if 'ASSESSMENT_PLAN' not in os.environ:
    model = f"{root_path}.oscal/assessment-plan/sample-plan.yaml"
else:
    model = os.environ['ASSESSMENT_PLAN']

print(model)

#%%
content = Path(model).read_text()
plan = yaml.safe_load(content)


# %%
def load_script(uuid):
    scripts = plan['assessment-plan']['back-matter']['resources']

    for script in scripts:
        if uuid == script['uuid']:
            return script

tasks = plan['assessment-plan']['tasks']

for task in tasks:
    for link in task['links']:
        script_id = link['href']
        script = load_script(script_id[1:len(script_id)])

        for resource in script['rlinks']:
            print("Resource",resource['href'])

            script_path = f"{root_path}{resource['href']}"
            script_content = Path(script_path).read_text()
            script_hash = hashlib.sha256(script_content.encode('utf-8')).hexdigest()

            for hash in resource['hashes']:
                if script_hash == hash['value']:
                    print(f"[ Execute Task ] {task['title']}")
                    assess_task = subprocess.run(["python", script_path])
                    print(f"The exit code was: {assess_task.returncode}")
                    print(assess_task.stdout)
                else:
                    raise RuntimeError(f"The hashes for {script_path} do not match.")

# %%
