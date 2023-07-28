# ScriptsForStaticWebDev
Python script for automating static web page content update. 
Change code as needed.
## Root
When I was given many static web pages of a small business and was asked to create more for their new products
## Technique used
- Python + library: openxyl, panda
- Json
- CSV
- Excel
## How I use the script (in general)
### Prepare category and data (or change the .json file directly)
1. write category csv file or directly change an existed category json file.
2. If write csv file, run:
    ```
    python category_json_generator.py source.csv
    ```
3. Find product image source folder, excel file path, and add into info_organizer.py file, last line
4. Open excel file, run:
   ```
   python info_organizer.py
   ```
   If space in the excel filename cannot avoid, change the code and hardcode it. 
5. follow instructions, enter data positions, keep all character lowercase
6. get item_dict.json, images moved to structured folders

### Generate content
1. In "page_template.html", set up the template for product pages for content to change. 
2. In "slider_img_block.html", set up the slider image code template used on product page. 
3. In "category_item_block.html", set up item code block on category page template. 
4. In "search_template.txt", set up search entry template.
```
Tags used in item page: 
#itemCetegory#, #itemID#, #itemColor#, #itemDesription#, #itemPrice#, #backToCategoryPageURL#, #slider_images#

Tags used in slider image code block: 
#image_path#

Tag used in category item code block and search code blcok entry: 
#itemID#, #htmlFile#, #profileImage#
```
5. Run:
```
python content_generator.py
``` 
6. Individual item pages generated, move to the website folder to check result. (if you use js on the website)
7. Put the code in "category_item_block_output.txt" manually in to corredponsing position on category page. The category page code differs and contaisn existed code, manually works for now. 
8. Copy paste the content of "search_block.txt" after the existed serach entries. 

## Other Case: add new category / changes on nav bar for all the web pages
1. One the webpage, find a good piece of code for replacement. put into "old.txt". 
2. Put the existed code + code to add into "new\.txt". 
3. Put "update_files.py" in the same folder with webpage files, run:
    ```
    python update_files.py old.txt new.txt
    ```
4. To check if update exists in files, put new content into "content_to_check.txt", put "check_file_updated.py" in the same folder with webpages, run:
    ```
    python check_file_updated.py content_to_check.txt
    ```
5. The check result for every file will be print out. 

## Other Case: Shrink image size
1. If the piectures on the webpage is too big and make it slow to load, shrink the size of all pictures under a directory if its width is more than 1000px
2. Run:
   ```
   python shrink_imgs.py imgs_directory
   ``` 
3. Repeat runnig the script until no messages shows up

## Other case: move a section to another page
1. Find the locaion to put content in the template file, put marker
2. Find the start and end location of the content that need to be copied from the source webpage
3. Add markers, directories, templates in the script "item_page_mover.py"
4. Run:
    ```
    python item_page_mover.py
    ```
