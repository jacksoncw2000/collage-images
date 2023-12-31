from PIL import Image
from pillow_heif import register_heif_opener

from collage_images import collage_images
from batch_convert_images import batch_convert_images
from check_if_duplicate_images import check_if_duplicate_images
from distribute_images import distribute_images


def convert_heic_to_png(original_image_name, original_image_extension):
    register_heif_opener()
    heic_image = Image.open(f'Original Images/{original_image_name}.{original_image_extension}')
    heic_image.save(f"PNG Images/{original_image_name}.png", "PNG")
    print("\nHEIC to PNG conversion complete")

def convert_jpg_to_png(original_image_name, original_image_extension):
    jpg_image = Image.open(f'Original Images/{original_image_name}.{original_image_extension}')
    jpg_image.save(f"PNG Images/{original_image_name}.png", "PNG")
    print("\nJPG to PNG conversion complete")


if __name__ == '__main__':

    ##---Collage Images---------------------------
    project_folder_name = ''
    png_folder_name = ''
    #collage_images(project_folder_name, png_folder_name, randomized_order=True)
    ##--------------------------------------------

    # ---Collage Images---------------------------
    project_folder_name = ''
    png_folder_name = ''
    #collage_images(project_folder_name, png_folder_name, randomized_order=True)
    # --------------------------------------------

    # ---Batch Convert Images---------------------------
    folder_name = ''
    #batch_convert_images(folder_name)
    # --------------------------------------------

    # ---Check if Duplicate Images---------------------------
    png_folder_name = ''
    #check_if_duplicate_images(png_folder_name)
    # --------------------------------------------

    # ---Distribute Images---------------------------
    input_folder = ""
    output_base_folder = ""
    num_folders = 5
    #distribute_images(input_folder, output_base_folder, num_folders)
    # --------------------------------------------


    #original_image_name = "IMG_7594"
    #original_image_extension = "HEIC"
    #convert_heic_to_png(original_image_name, original_image_extension)

    #original_image_name = "DSC04722"
    #original_image_extension = "JPG"
    #convert_jpg_to_png(original_image_name, original_image_extension)

    #original_image_name = "Photo of Moose by Harris"
    #original_image_extension = "jpeg"
    #orientation = 1
    #change_image_orientation(original_image_name, original_image_extension, orientation)