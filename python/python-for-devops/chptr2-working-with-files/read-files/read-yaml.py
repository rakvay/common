from pprint import pprint
import yaml

#should specify absolute path to the file
file_path = 'playbook.yaml'
with open(file_path, 'r') as opened_file:
    playbook = yaml.safe_load(opened_file)
pprint(playbook)

#should specify absolute path to the file
updated_path = 'playbook-updated.yaml'
with open(updated_path, 'w') as opened_file:
    yaml.dump(updated_path, opened_file)