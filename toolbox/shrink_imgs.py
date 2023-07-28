import os
import sys
from PIL import Image
'''
This script is used to shrink all product images to about 500px width
If image width > 1000px, resize 50%
The script might need to be run for multiple times
'''


def shrink_images(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            if os.path.isfile(file_path):
                try:
                    img = Image.open(file_path)
                    width, height = img.size
                    if width > 1000:
                        new_width = int(width * 0.5)
                        new_height = int(height * 0.5)
                        resized_img = img.resize((new_width, new_height))
                        resized_img.save(file_path)
                        print(f"Image '{filename}' resized to 50%.")
                except (IOError, OSError):
                    print(f"Failed to process image '{filename}'.")


# Specify the folder path
folder_path = sys.argv[1]
# Call the function to shrink the images
shrink_images(folder_path)
