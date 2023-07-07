from pprint import pprint
import json

# read json file content and store it to policy
#should specify absolute path to the file
file_path = 'policy.json'
with open(file_path, 'r') as opened_file:
    policy = json.load(opened_file)
pprint(policy)

# update json field
policy['Statement']['Effect'] = 'Disable'
pprint(policy)

#store updated json to file
#should specify absolute path to the file
with open(file_path, 'w') as opened_file:
    policy = json.dump(policy, opened_file)
pprint(policy)