import os

'''
The script is used to check if certain content is updated and existed in all the .html files of current folder
.html can be changed to any other file types
Warning: python file read do not support certain encoding
'''

# Specify the directory to check for HTML files
directory = '.\\'

# Define the content to check
word = ''

# Get all files in the directory
files = os.listdir(directory)

# Iterate over the .html files and check the content
for file in files:
    if file.endswith('.html'):
        file_path = os.path.join(directory, file)

        # Open the HTML file as a text file
        with open(file_path, 'r') as file:
            html_content = file.read()
            if word in html_content:
                print(f"Content found in file: {file_path}")
            else:
                print(f"!!! Content not found in file: {file_path}")
