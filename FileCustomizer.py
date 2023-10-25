import os
import pandas as pd
import json

folder_path = "/Users/alexbrown/Documents/GitHub/generative_agents/environment/frontend_server/storage/CustomizedSim"
old_value = "Isabella"
new_value = "Ramsay"

# df['column_name'].replace("Isabella", "Ramsay", inplace=True)
# df['column_name'].replace("Rodriguez", "Brown", inplace=True)
# df['column_name'].replace("Klaus", "Alex", inplace=True)
# df['column_name'].replace("Mueller", "Brown", inplace=True)
# df['column_name'].replace("Maria", "Aidan", inplace=True)
# df['column_name'].replace("Lopez", "Miles", inplace=True)

# For CSV files
for file in os.listdir(folder_path):
    if file.endswith(".csv"):
        csv_file_path = os.path.join(folder_path, file)
        df = pd.read_csv(csv_file_path)
        
        for col in df.columns:
            df[col] = df[col].replace(old_value, new_value)
            
        df.to_csv(csv_file_path, index=False)

# For JSON files
for file in os.listdir(folder_path):
    if file.endswith(".json"):
        json_file_path = os.path.join(folder_path, file)
        
        with open(json_file_path, "r") as f:
            data = json.load(f)
        
        def deep_replace(d):
            if isinstance(d, dict):
                return {k: deep_replace(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [deep_replace(v) for v in d]
            elif d == old_value:
                return new_value
            else:
                return d

        modified_data = deep_replace(data)
        
        with open(json_file_path, "w") as f:
            json.dump(modified_data, f)

