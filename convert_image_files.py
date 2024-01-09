from PIL import Image
from pillow_heif import register_heif_opener

def convert_heic_to_png(original_image_file_path, original_image_name, original_image_extension="HEIC", output_file_path):
    register_heif_opener()
    heic_image = Image.open(f'{original_image_file_path}/{original_image_name}.{original_image_extension}')
    heic_image.save(f"{output_file_path}/{original_image_name}.png", "PNG")
    print(f"\n{original_image_name} HEIC image converted to PNG successfully.")

#original_image_file_path = ""
#original_image_name = ""
#original_image_extension = "HEIC"
#output_file_path = ""
#convert_heic_to_png(original_image_file_path, original_image_name, original_image_extension, output_file_path)

def convert_jpg_to_png(original_image_file_path, original_image_name, original_image_extension, output_file_path):
    jpg_image = Image.open(f'{original_image_file_path}/{original_image_name}.{original_image_extension}')
    jpg_image.save(f"{output_file_path}/{original_image_name}.png", "PNG")
    print(f"\n{original_image_name} JPG image converted to PNG successfully.")

#original_image_file_path = ""
#original_image_name = ""
#original_image_extension = "JPG"
#output_file_path = ""
#convert_jpg_to_png(original_image_file_path, original_image_name, original_image_extension, output_file_path)