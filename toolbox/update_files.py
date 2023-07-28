import os

'''
The script is used to update certain content using replacement in all the .html files of current folder
.html can be changed to any other text file types
Multiple content can be replaced at once by adding more varibale pairs
Warning: python file read do not support certain encoding
'''

# Specify the directory to check for HTML files
directory = '.\\'

# Define the content to replace
old_content1 = ''
new_content1 = ''

with open('old.txt', 'r') as file:
    old_content1 = file.read()

with open('new.txt', 'r') as file:
    new_content1 = file.read()


# Get all files in the directory
files = os.listdir(directory)

# Iterate over the files and modify HTML content
for file in files:
    if file.endswith('.html'):
        file_path = os.path.join(directory, file)

        # Open the HTML file as a text file
        with open(file_path, 'r') as file:
            html_content = file.read()
            modified_content = html_content.replace(old_content1, new_content1)

        # Save the modified lines to the file
        with open(file_path, 'w') as modified_file:
            modified_file.write(modified_content)

        print(f"Content replaced in file: {file_path}")
