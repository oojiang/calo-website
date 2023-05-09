from PIL import Image
import os
import shutil

def resize_images(input_directory, output_directory, width):
    for root, dirs, files in os.walk(input_directory):
        # Determine the corresponding subdirectory in the output directory
        relative_path = os.path.relpath(root, input_directory)
        output_subdirectory = os.path.join(output_directory, relative_path)

        # Create the subdirectory in the output directory if it doesn't exist
        os.makedirs(output_subdirectory, exist_ok=True)

        for filename in files:
            if filename.endswith('.jpg') or filename.endswith('.png'):
                input_path = os.path.join(root, filename)
                output_path = os.path.join(output_subdirectory, filename)
                print(output_path)

                # Open the image file
                image = Image.open(input_path)

                # Resize the image while preserving the aspect ratio
                height = int((float(image.size[1]) / image.size[0]) * width)
                resized_image = image.resize((width, height), Image.ANTIALIAS)

                # Save the resized image to the output directory
                resized_image.save(output_path)

                # Close the image file
                image.close()

# Specify the input and output directories
input_directory = 'img/eboc/eboc-2023'
output_directory = 'img/eboc-2023-2000px'

# Call the function to resize images
resize_images(input_directory, output_directory, 2000)
