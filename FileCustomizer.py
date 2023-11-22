import os
import pandas as pd
import json

# folder_path = "/Users/alexbrown/Documents/GitHub/generative_agents/environment/frontend_server/storage/CustomizedSim1" #customize simulation files
folder_path = "/Users/alexbrown/Documents/GitHub/generative_agents/environment/frontend_server/static_dirs/assets/the_ville/matrix/special_blocks" #customize shared base files
#NOTE TO SELF: If I want to edit only a single Persona, be sure to alter the path ^ to that SPECIFIC folder

# old_value = "Her"
# new_value = "His"

# old_value = "her"
# new_value = "his"

# old_value = "she"
# new_value = "he"

# old_value = "She"
# new_value = "He"


# old_value = "Isabella Rodriguez"
# new_value = "Ramsay Brown"
# old_value = "Isabella"
# new_value = "Ramsay"
# old_value = "Rodriguez"
# new_value = "Brown"

# old_value = "Klaus Mueller"
# new_value = "Alex Brown"
# old_value = "Mueller"
# new_value = "Brown"
# old_value = "Klaus"
# new_value = "Alex"

# old_value = "Maria Lopez"
# new_value = "Aidan Miles"
# old_value = "Lopez"
# new_value = "Miles"
# old_value = "Maria"
# new_value = "Aidan"

# old_value = "Hobbs Cafe"
# new_value = "Nanners"

# old_value = "Cafe"
# new_value = "Bar"

# old_value = "Hobbs"
# new_value = "Nanners"



def deep_replace(d):
    if isinstance(d, dict):
        new_dict = {}
        for k, v in d.items():
            new_key = k.replace(old_value, new_value)
            if k != new_key:
                print(f"Found substring '{old_value}' in key, replacing with '{new_value}'.")
            new_dict[new_key] = deep_replace(v)
        return new_dict
    elif isinstance(d, list):
        return [deep_replace(v) for v in d]
    elif isinstance(d, str):
        modified_str = d
        if old_value in d:
            print(f"Found substring '{old_value}' in JSON, replacing with '{new_value}'.")
            modified_str = modified_str.replace(old_value, new_value)
        if f"{old_value}'s" in d:
            print(f"Found possessive form '{old_value}'s' in JSON, replacing with '{new_value}'s.")
            modified_str = modified_str.replace(f"{old_value}'s", f"{new_value}'s")
        return modified_str
    return d

# Walk through folder and subfolders to find files
for dirpath, _, filenames in os.walk(folder_path):
    for file in filenames:
        if file.endswith(".json"):
            print("Found JSON")
            json_file_path = os.path.join(dirpath, file)
            with open(json_file_path, 'r') as f:
                data = json.load(f)
            modified_data = deep_replace(data)
            with open(json_file_path, 'w') as f:
                json.dump(modified_data, f, indent=4)
