#Implement function parse_user(output_file, *input_files) for creating file that will contain only unique records (unique by key "name")
# by merging information from all input_files argument (if we find user with already existing name from previous file we should ignore it).
# Use pretty printing for writing users to json-file. If the function cannot find input files we need to log information with error level
#root - ERROR - File <file name> doesn't exist

import json
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def parse_user(output_file, *input_files):
    unique_records = set()
    final_list = []

    for file_path in input_files:
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)

            for item in data:
                if isinstance(item, dict) and "name" in item:
                    name = item["name"]
                    if name not in unique_records:
                        unique_records.add(name)
                        final_list.append(item)

        except FileNotFoundError:
            logging.error(f"File {file_path} doesn't exist")

    with open(output_file, 'w', encoding='utf-8') as out_f:
        json.dump(final_list, out_f, indent=4)
    return output_file



