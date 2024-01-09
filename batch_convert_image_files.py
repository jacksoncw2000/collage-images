import os
import datetime
from PIL import Image
from pillow_heif import register_heif_opener
from pathlib import Path
from tqdm import tqdm

def save_as_png(image_path, output_path):
    try:
        img = Image.open(image_path)
        img.save(output_path, "PNG")
    except Exception as e:
        print(f"Failed to convert {image_path} to PNG: {e}")

def batch_convert_image_files(source_folder_path, output_folder_path, output_folder_name):
    current_date_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    print(f'\Batch convert image files started at {current_date_time}')

    source_folder = Path(f'{source_folder_path}')
    output_folder = Path(f'{output_folder_path}/{current_date_time}_{output_folder_name}')
    output_folder.mkdir(parents=True, exist_ok=True)

    image_files = list(source_folder.iterdir())
    for image_file in tqdm(image_files, desc="Converting images", unit="file"):
        if image_file.suffix.lower() in ['.heic', '.jpg', '.jpeg']:
            if image_file.suffix.lower() == '.heic':
                register_heif_opener()
            output_path = output_folder / f"{image_file.stem}.png"
            save_as_png(image_file, output_path)

    print("\nHEIC, JPG, JPEG to PNG conversion complete.")