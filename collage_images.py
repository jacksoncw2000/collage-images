import os
import datetime
import math
import random
from PIL import Image, ExifTags

def collage_images(project_folder_name, png_folder_name, randomized_order=True):

    current_working_directory = os.getcwd()
    print(f"\nCurrent Working Directory: {current_working_directory}")

  
    current_date_time = datetime.datetime.now()
    current_date_time = current_date_time.strftime('%Y%m%d_%H%M%S')

    print(f'\nCollage images beginning {current_date_time}')

    image_files = os.listdir(f'{current_working_directory}/source_images/{project_folder_name}/{png_folder_name}')

    images_array = []

    for image_file in image_files:
        images_array.append(f"{png_folder_name}/{image_file}")

    if f"{png_folder_name}/.DS_Store" in images_array:
        images_array.remove(f"{png_folder_name}/.DS_Store")

    if randomized_order:  # Shuffle the images_array if randomized_order is True
        random.shuffle(images_array)

    number_of_images_uploaded = len(images_array)

    collage_width = int(math.sqrt(number_of_images_uploaded) * 1000)
    collage_height = int(math.sqrt(number_of_images_uploaded) * 1000)

    collage = Image.new("RGB", (collage_width, collage_height), (255, 255, 255))

    thumbnail_width = int(collage_width / math.sqrt(len(images_array)))
    thumbnail_height = int(collage_height / math.sqrt(len(images_array)))

    for i, image in enumerate(images_array):
        percentage_complete = (i + 1) / number_of_images_uploaded * 100
        print(f"{percentage_complete:.2f}% complete")

        image = Image.open(f'{current_working_directory}/source_images/{project_folder_name}/{image}')

        exif_data = image._getexif()
        if exif_data is not None:
            exif = {ExifTags.TAGS[k]: v for k, v in image._getexif().items() if k in ExifTags.TAGS}

        image = image.resize((thumbnail_width, thumbnail_height))

        if exif_data is not None:
            if 'Orientation' in exif:
                if exif['Orientation'] == 3:
                    image = image.rotate(180)
                elif exif['Orientation'] == 6:
                    image = image.rotate(270)
                elif exif['Orientation'] == 8:
                    image = image.rotate(90)

        x = i % int(math.sqrt(len(images_array))) * thumbnail_width
        y = i // int(math.sqrt(len(images_array))) * thumbnail_height

        collage.paste(image, (x, y))

    folder_name = "outputs"
    # Check if the outputs folder exists
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)  # Create the outputs folder
        print(f"Folder '{folder_name}' created.")
    else:
        print(f"Folder '{folder_name}' already exists.")

    collage.save(f"outputs/Collage {current_date_time}.png")

    print("\nCollage complete")
