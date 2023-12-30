import os
import datetime
from PIL import Image
from pillow_heif import register_heif_opener

def check_if_duplicate_images(png_folder_name):

    ACTIVE_DIRECTORY_PATH = ''
    project_folder_name = ''

    current_date_time = datetime.datetime.now()
    # Format the date and time as YYYYMMDD_HHMMSS
    current_date_time = current_date_time.strftime('%Y%m%d_%H%M%S')

    print(f'\nCheck if Duplicate Images {current_date_time}\n')

    image_files = os.listdir(f'{ACTIVE_DIRECTORY_PATH}/source_images/{project_folder_name}/{png_folder_name}')

    if '.DS_Store' in image_files:
        image_files.remove('.DS_Store')

    image_files_count = len(image_files)
    #print(f'Image Files Count: {image_files_count}')

    count = 0
    hashes = {}
    for filename in image_files:
        image_path = f'{ACTIVE_DIRECTORY_PATH}/source_images/{project_folder_name}/{png_folder_name}/{filename}'
        with Image.open(image_path) as img:
            # Calculate the hash of the pixel data
            img_hash = hash(img.tobytes())
            # Check if the hash already exists
            if img_hash in hashes:
                # If the hash already exists, it means the images are duplicates
                print(f'\n\n{filename} is a duplicate of {hashes[img_hash]}\n\n')
            else:
                # If the hash doesn't exist, store the hash with the filename
                hashes[img_hash] = filename
        count = count + 1
        print(f'{round((count/image_files_count)*100, 2)}% complete')

    print("\nCheck if duplicate images complete")
