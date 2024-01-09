from convert_image_files import convert_heic_to_png, convert_jpg_to_png
from batch_convert_image_files import batch_convert_image_files
from check_if_duplicate_images import check_if_duplicate_images
from collage_images import collage_images
from distribute_images import distribute_images

if __name__ == '__main__':

    # ---Batch Convert Images---------------------------
    folder_name = ''
    #batch_convert_images(folder_name)
    # --------------------------------------------

    # ---Check if Duplicate Images---------------------------
    png_folder_name = ''
    #check_if_duplicate_images(png_folder_name)
    # --------------------------------------------

    #---Collage Images---------------------------
    project_folder_name = 'Test Project'
    png_folder_name = 'Test Folder'
    collage_images(project_folder_name, png_folder_name, randomized_order=True)
    #--------------------------------------------

    # ---Distribute Images---------------------------
    input_folder = ""
    output_base_folder = ""
    num_folders = 5
    #distribute_images(input_folder, output_base_folder, num_folders)
    # --------------------------------------------

    #original_image_name = ""
    #original_image_extension = "jpeg"
    #orientation = 1
    #change_image_orientation(original_image_name, original_image_extension, orientation)