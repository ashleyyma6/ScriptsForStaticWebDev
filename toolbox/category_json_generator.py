import csv
import json

dictionary = []

'''
This script creates a .json category dictionary from the initial CSV file for later use.

=== Category Dictionary Format ===
{category (in excel file): [img_directory_keyword, category_keyword, category_code, category_html, level_text]}
1 img_directory_keyword: The 1st level folder to store item images.
2 category_keyword: The category of the item on the website.
3 category_code: The short code representing the item category, which is placed in the HTML filename to differentiate items from different categories but share the same item ID.
4 category_html: The HTML file of the item's category page.
5 level_text: The text displayed on the item page, indicating the category level of the current item.
Note: The category keyword can generate the category HTML file and level text, but the current dictionary is sufficient.
'''


class category_dic_entry:
    def __init__(self, img_directory_keyword, category_keyword, category_code, category_html, level_text):
        self.img_directory_keyword = img_directory_keyword
        self.category_keyword = category_keyword
        self.category_code = category_code
        self.category_html = category_html
        self.level_text = level_text


def load_dictionary():
    dict_file = 'category.csv'
    data = {}
    # Open the CSV file
    with open(dict_file, 'r') as file:
        # Create a CSV reader
        reader = csv.reader(file)
        # Read and process each line in the CSV file
        for row in enumerate(reader):
            data.update({row[1][0]: category_dic_entry(
                row[1][1], row[1][2], row[1][3], row[1][4], row[1][5]).__dict__})
    with open('category_dict.json', 'w') as file:
        json.dump(data, file)


dictionary = load_dictionary()
