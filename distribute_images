import os
import shutil
import random

def distribute_images(input_folder, output_base_folder, num_folders):

    if not os.path.exists(output_base_folder):
        os.makedirs(output_base_folder)

    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.png')]
    random.shuffle(image_files)

    images_per_folder = len(image_files) // num_folders

    for i in range(num_folders):
        output_folder = os.path.join(output_base_folder, f"folder_{i+1}")
        os.makedirs(output_folder)

        images_to_move = image_files[i * images_per_folder:(i + 1) * images_per_folder]

        for image in images_to_move:
            src = os.path.join(input_folder, image)
            dst = os.path.join(output_folder, image)
            shutil.copy(src, dst)

    print("\nDistribute images complete")
