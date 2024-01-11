

import os

# Define the base path of the ARMS Data API Tester & Explorer project
base_path = 'C:/Users/lnonino/OneDrive - DATAGRO/Documentos/GitHub/USDAdemoAPI'

file_groups = {
    'modules': [
        'modules/category.py',
        'modules/farmtype.py',
        'modules/report.py',
        'modules/state.py',
        'modules/surveydata.py',
        'modules/variable.py',
        'modules/year.py'
    ],
    'utils': [
        'utils/api_request_handler.py',
        'utils/csv_writer.py',
        'utils/url_generator.py'
    ],
    'root': [
        'config.py',
        'main.py',
        'README.md',
        'requirements.txt'
    ],
    'all': []  # Placeholder, will contain all files
}

# Populate the 'all' group
for group in file_groups.values():
    file_groups['all'].extend(group)

# Ask the user which group to process
group_names = input("Which group(s) do you want to process? Separate multiple groups with ';': ")

# Split the input into individual group names
group_names = group_names.split(';')

# Combine the files from the selected groups and remove duplicates
file_paths = []
for group_name in group_names:
    group_files = file_groups.get(group_name.strip())
    if group_files is not None:
        file_paths.extend(group_files)
file_paths = list(set(file_paths))  # Remove duplicates

if not file_paths:
    print(f"No such group: {group_names}")
    exit(1)

# Path to the output Markdown file
output_md_file = 'consolidated_documentation.md'

# Create and open the output Markdown file
with open(output_md_file, 'w') as md_file:
    print("Starting documentation consolidation...")
    for relative_path in file_paths:
        # Construct the full path
        full_path = os.path.join(base_path, relative_path)
        print(f"Processing file: {full_path}")

        # Check if the file exists
        if not os.path.exists(full_path):
            print(f"File not found: {full_path}")
            continue

        # Read the file content
        with open(full_path, 'r') as file:
            content = file.read()

        # Write the file path and content to the Markdown file
        md_file.write(f"## {relative_path}\n```\n{content}\n```\n")
    print("Documentation consolidation completed.")
