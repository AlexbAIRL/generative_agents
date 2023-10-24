import os
import pandas as pd
import json

folder_path = "/Users/alexbrown/Documents/GitHub/generative_agents/environment/frontend_server/storage/CustomizedSim"

# For CSV files
for file in os.listdir(folder_path):
    if file.endswith(".csv"):
        csv_file_path = os.path.join(folder_path, file)
        df = pd.read_csv(csv_file_path)
        df['column_name'].replace("old_value", "new_value", inplace=True)
        df.to_csv(csv_file_path, index=False)

# For JSON files
for file in os.listdir(folder_path):
    if file.endswith(".json"):
        json_file_path = os.path.join(folder_path, file)
        with open(json_file_path, "r") as f:
            data = json.load(f)
        data['key'] = "new_value"
        with open(json_file_path, "w") as f:
            json.dump(data, f)
