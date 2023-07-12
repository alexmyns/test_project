import json

# Read the JSON file
with open('../assets/school_type.json', 'r') as file:
    content = file.read()

# Replace single quotes with double quotes
content = content.replace("'", "\"")

# Write the modified content back to the file
with open('./assets/school_type.json', 'w') as file:
    file.write(content)
