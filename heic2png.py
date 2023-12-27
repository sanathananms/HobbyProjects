import os
from PIL import Image
import pillow_heif

def convert_heic_to_png(input_dir, output_dir):
    """Converts all .HEIC files in the input directory to PNG format and saves them in the output directory."""

    for filename in os.listdir(input_dir):
        if filename.endswith(".HEIC"):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + ".png")

            try:
                heif_file = pillow_heif.read_heif(input_path)
                image = Image.frombytes(
                    heif_file.mode, heif_file.size, heif_file.data, "raw"
                )
                image.save(output_path, "PNG")
                print(f"Converted {filename} to {output_path}")
            except Exception as e:
                print(f"Error converting {filename}: {e}")

# Example usage:
input_dir = "C:/Users/user/Downloads/56 Day Function"  # Replace with the actual path to your HEIC files
output_dir = "C:/Users/user/Downloads/56 Day Function/png"  # Replace with the desired output directory
convert_heic_to_png(input_dir, output_dir)
