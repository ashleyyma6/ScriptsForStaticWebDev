import os
import shutil


def find_word_position(file_path, target_word):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if target_word in line:
                return i


def copy_content_between_words(file1_path, word1, word2):
    start = find_word_position(file1_path, word1)
    end = find_word_position(file1_path, word2)

    if start is None or end is None or start >= end:
        print("Could not find valid positions for word1 and word2.")
        return None

    with open(file1_path, 'r') as file:
        lines = file.readlines()
        copied_content = ''.join(lines[start:end])
        return copied_content


def insert_copied_content(file2_path, marker_word, copied_content):
    with open(file2_path, 'r') as file:
        lines = file.readlines()

    marker_line = None
    for i, line in enumerate(lines):
        if marker_word in line:
            marker_line = i
            break

    if marker_line is None:
        print(f"Marker word '{marker_word}' not found in file2.")
        return

    lines.insert(marker_line, copied_content)

    with open(file2_path, 'w') as file:
        file.write(''.join(lines))


def replace_content(file1, file2, w1, w2, marker):
    # Define the file paths and target words
    file1_path = file1  # 'file1.txt'
    file2_path = file2  # 'file2.txt'
    word1 = w1  # 'word1'
    word2 = w2  # 'word2'
    marker_word = marker  # 'INSERT_HERE'

    # Copy the content between word1 and word2 in file1
    copied_content = copy_content_between_words(file1_path, word1, word2)

    # Insert the copied content into file2 at the marker word
    if copied_content:
        insert_copied_content(file2_path, marker_word, copied_content)


def copy_and_rename_files(directory1, directory2, template_filename):
    for filename in os.listdir(directory1):
        file_path = os.path.join(directory1, filename)

        # Skip directories and only process files
        if not os.path.isfile(file_path):
            continue

        # Copy the template file from directory2
        template_file_path = os.path.join(directory2, template_filename)
        destination_path = os.path.join(directory2, filename)

        # Make a copy of the template file with the filename
        shutil.copyfile(template_file_path, destination_path)
        print(
            f"Template file '{template_filename}' copied and renamed to '{filename}'.")

        # Fill the item page content from old file to new file
        replace_content(file_path, destination_path, '<!-- Action Box 1 -->',
                        '<!-- Portfolio 1-->', '<!-- INSERT_HERE -->')


# Specify the directories and template filename
directory1 = 'dir1'
directory2 = 'dir2'
template_filename = 'template.html'

# Call the function to copy and rename the files
copy_and_rename_files(directory1, directory2, template_filename)
