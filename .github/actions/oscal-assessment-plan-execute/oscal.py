#%%
import os, yaml, hashlib, subprocess
from pathlib import Path
from yaml import load

if 'ASSESSMENT_PLAN' not in os.environ:
    model = "../../../.oscal/assessment-plan.yaml"
    # exit("Assessment Plan Environment Variable Not Found")
else:
    model = os.environ['ASSESSMENT_PLAN']

print(model)

#%%
content = Path(model).read_text()
plan = yaml.safe_load(content)
root_path = "../../../"

#%%
# print("*"*100)
# print(model)
# print(plan)


# %%
def load_script(uuid):
    scripts = plan['assessment-plan']['back-matter']['resources']

    for script in scripts:
        if uuid == script['uuid']:
            return script

tasks = plan['assessment-plan']['tasks']

for task in tasks:
    for link in task['links']:
        # print(f"{task['title']} ({link['href']})")
        # print(task['links'])
        script_id = link['href']
        script = load_script(script_id[1:len(script_id)])

        for resource in script['rlinks']:
            print("Resource",resource['href'])
            script_content = Path(f"{root_path}{resource['href']}").read_text()
            script_hash = hashlib.sha256(script_content.encode('utf-8')).hexdigest()

            for hash in resource['hashes']:
                # print("Script:",script_hash,"Expected:",hash['value'])
                if script_hash == hash['value']:
                    print(f"[ Execute Task ] {task['title']}")
                    assess_task = subprocess.run(["python", f"{root_path}{resource['href']}"])
                    print(f"The exit code was: {assess_task.returncode}")
                    print(assess_task.stdout)
                else:
                    print(f"The hashes for {root_path}{resource['href']} do not match.")


# %%
