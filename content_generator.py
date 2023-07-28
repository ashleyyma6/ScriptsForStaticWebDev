import shutil
import os
import json
import sys

'''
This script generate the content of website:
1. Individual item page, fill the image slider
2. The code of item block on category page 
3. The formated search info entry for item serach page
'''


def load_dictionary(dict_json):
    # load category dictionary, item dictionary
    with open(dict_json, 'r') as file:
        loaded_dict = json.load(file)
        return loaded_dict


def gen_html_filename(category, data):
    # html file name format: item-itemID-category_code-itemColor.html
    category_code = category[data["category"]]["category_code"]
    file_name = "-".join(['item', data["ID"],
                          category_code, data["color"]])+'.html'
    return file_name


def get_img_directory(category_dict, data):
    category_code = category_dict[data["category"]]["img_directory_keyword"]
    directory = "-".join(['images', category_code]) + \
        '\\'+data["category"]+'\\'+data["ID"]
    # print(f"image directory {directory}")
    return '.\\'+directory


def gen_one_item_page(data, html_template, category_dict):
    '''
    2 Open html template file
    2.1 Using json content, make a new html file name
    2.2 Copy and rename html file
    2.3 Open the new html file
    2.4 Replace html content based on the json file
    Note: this function will be used for one row data, a for loop will call this function for all data
    [#itemCetegory#, #itemID#, #itemColor#, #itemDesription#, #itemPrice#, #backToCategoryPageURL#, #slider_images#] 
    '''
    # Get item page file name
    destination_file = gen_html_filename(
        category_dict, data)  # data_arr[0], data_arr[1], data_arr[2]
    data.update({"html_filename": destination_file})
    # Copy template and rename the html file
    shutil.copyfile(html_template, destination_file)

    # Open the HTML file
    with open(destination_file, 'r') as file:
        html_content = file.read()

        # Perform find and replace
        modified_content = html_content.replace(
            '#itemCategory#', category_dict[data["category"]]["category_keyword"].replace("_", " "))
        modified_content = modified_content.replace(
            '#itemCategoryLevel#', category_dict[data["category"]]["level_text"])
        modified_content = modified_content.replace('#itemID#', data["ID"])
        modified_content = modified_content.replace(
            '#itemColor#', data["color"])
        modified_content = modified_content.replace(
            '#itemPrice#', '$'+str(data["price"]))
        modified_content = modified_content.replace(
            '#backToCategoryPageURL#', category_dict[data["category"]]["category_html"])
        modified_content = modified_content.replace(
            '#itemDesription#', data["decription"])
        modified_content = update_images(get_img_directory(
            category_dict, data), modified_content)

    # Save the modified HTML content
    with open(destination_file, 'w') as file:
        file.write(modified_content)
    itemID = data["ID"]
    print(f"{itemID} page generated.")


def update_images(img_directory, webpage_code):
    image_slider_template = 'slider_img_block.html'
    with open(image_slider_template, 'r') as file:
        code_template = file.read()
        # print(code_template)
        code_blocks = ''

        # Specify the directory
        target_folder = os.path.abspath(img_directory)
        # Get the relative file paths
        current_folder = os.getcwd()

        file_paths = []
        for root, dirs, files in os.walk(target_folder):
            for file in files:
                # skip the profile imgae for category page
                if "profile" in file:
                    continue
                file_path = os.path.relpath(
                    os.path.join(root, file), current_folder)
                one_code_block = code_template
                one_code_block = one_code_block.replace(
                    '#image_path#', file_path)
                one_code_block += "\n"
                file_paths.append(file_path)
                code_blocks += one_code_block
        print(f"slider image blocks are ready. ")
        modified_code = webpage_code.replace('#slider_images#', code_blocks)
        print(f"slide image code inserted. ")
        return modified_code


def get_profile_img_path(item, category_dict):
    img_directory = get_img_directory(
        category_dict, item)+'\\'+item["ID"]+'_profile.jpg'
    # print(img_directory)
    return img_directory


def gen_one_item_code_blocks(data, category_block_template, search_template, category_dict):
    source_file = category_block_template
    # if run after item page generateion, html_filename updated in the dictionary
    html_filename = data["html_filename"]
    # if run from the json file
    # html_filename = gen_html_filename(category_dict, data)

    profile_img_dir = get_profile_img_path(data, category_dict)

    '''
    Generate category code block
    '''
    destination_file = 'category_item_block_output.txt'  # hardcoded
    modified_content = ''

    with open(source_file, 'r') as file:
        html_content = file.read()
        modified_content = html_content.replace(
            '#itemID#', data["ID"])
        modified_content = modified_content.replace(
            '#htmlFile#', html_filename)
        modified_content = modified_content.replace(
            '#profileImage#', profile_img_dir)

    with open(destination_file, 'a') as file:
        file.write(modified_content)
        file.write('\n')

    itemID = data["ID"]
    print(f"{itemID} block generated.")

    '''
    Generate serach entry block
    '''
    modified_content = ''
    destination_file = 'search_block.txt'
    with open(search_template, 'r') as file:
        html_content = file.read()
        modified_content = html_content.replace(
            '#itemID#', data["ID"])
        modified_content = modified_content.replace(
            '#htmlFile#', html_filename)
        modified_content = modified_content.replace(
            '#profileImage#', profile_img_dir)
    modified_content = modified_content.replace('\\', '/')

    with open(destination_file, 'a') as file:
        file.write(modified_content)
        file.write('\n')
    print(f"{itemID} search block generated.")


'''
=== Main ===
- load categroy dictionary
- read organized product data from item json file
- generate individual item pages
- generate category block + search info entry
Argument:
- data_json: product info in json file
- page_template: the individual product web page template
- category_block_template: th individual product code block template for putting on category page
- search_template: code block entries for search functions
- category_json: category json file

python content_generator.py
'''


def main(data_json, page_template, category_block_template, search_template, category_json):
    # get all item information
    category_dict = load_dictionary(category_json)
    items = load_dictionary(data_json)
    for key in items.keys():
        gen_one_item_page(items[key], page_template, category_dict)
        gen_one_item_code_blocks(
            items[key], category_block_template, search_template, category_dict)
    print("All content generated successfully!")


'''
python content_generator.py
hardccoded argumnet, should all be prepared before run the script
'''
main('item_dict.json', 'page_template.html',
     'category_item_block.html', 'search_template.txt', 'category_dict.json')
