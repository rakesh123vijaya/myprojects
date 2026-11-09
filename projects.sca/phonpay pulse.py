import os
import glob
import pandas as pd
import numpy as np

folders = {
    "aggregated_transaction": "aggregated_transaction.csv",
    "aggregated_user": "aggregated_user.csv",
    "map_transaction": "map_transaction.csv",
    "map_user": "map_user.csv",
    "top_transaction": "top_transaction.csv",
    "top_user": "top_user.csv"
}

output_dir = "final_merged_data"
os.makedirs(output_dir, exist_ok=True)

for data_type, filename in folders.items():

    csv_files = glob.glob("**/" + filename, recursive=True)

    if csv_files:
        df_list = [pd.read_csv(file) for file in csv_files]

        master_df = pd.concat(df_list, ignore_index=True)

        output_file = os.path.join(
            output_dir, f"master_{data_type}.csv"
        )

        master_df.to_csv(output_file, index=False)

        print("Successfully merged:", data_type)

    else:
        print("File not found:", filename)


