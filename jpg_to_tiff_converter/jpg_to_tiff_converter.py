import os
from PIL import Image

def convert_image(input_path, output_folder):
    with Image.open(input_path) as im:
        tiff_path = os.path.join(output_folder, os.path.splitext(os.path.basename(input_path))[0] + ".tiff")
        im.save(tiff_path, format="TIFF", quality=100)

def main():
    print("Welcome to JPG to TIFF Converter!")
    while True:
        jpg_folder = input("Enter the path to the folder containing JPG images: ")
        if os.path.exists(jpg_folder):
            break
        else:
            print("The folder does not exist.")
    while True:
        tiff_folder = input("Enter the path to the folder where converted TIFF images will be saved: ")
        if os.path.exists(tiff_folder):
            break
        else:
            print("The folder does not exist.")
    # Create the TIFF folder if it doesn't exist yet
    if not os.path.exists(tiff_folder):
        os.makedirs(tiff_folder)
    # Convert images
    for filename in os.listdir(jpg_folder):
        if filename.endswith('.jpg'):
            input_path = os.path.join(jpg_folder, filename)
            convert_image(input_path, tiff_folder)
    print("All images converted successfully to TIFF format and saved in the chosen folder!")

if __name__ == "__main__":
    main()

# softy_plug