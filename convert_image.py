import cv2
import argparse
import pillow_heif
from PIL import Image
import numpy as np
from multiprocessing import Pool, cpu_count
from pathlib import Path
from tqdm import tqdm


def process_image(params):
    """Process an individual image."""
    input_path, output_dir = params
    output_path = output_dir / (input_path.stem + ".jpg")
    extension = input_path.suffix.lower()

    try:
        if extension in ['.heic']:
            heif_file = pillow_heif.open_heif(str(input_path), convert_hdr_to_8bit=False, bgr_mode=True)
            img = np.asarray(heif_file)
        elif extension in ['.png', '.tiff']:  # PNG or TIFF
            img = cv2.imread(str(input_path))

        cv2.imwrite(str(output_path), img, [cv2.IMWRITE_JPEG_QUALITY, 100])
        # print(f"Done Processing: {str(input_path)}")
        return None
    except Exception as e:
        return f"Error processing {str(input_path)}: {str(e)}"

def convert_images(input_dir, output_dir):
    """Convert HEIC, PNG, and TIFF images to JPG format using multiprocessing."""
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    # Get all the image paths to be processed
    image_paths = [
        path
        for path in input_path.rglob("*")
        if path.suffix.lower() in ['.heic', '.png', '.tiff', '.tif']
    ]
    
    # Using a pool of worker processes to process images in parallel
    params = [(path, output_path) for path in image_paths]
    with Pool(cpu_count()) as p:
        results = list(tqdm(p.imap(process_image, params), total=len(params)))

    
    for error in filter(None, results):  # filter out the successful None results
        print(f"Error processing an image: {error}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert HEIC, PNG, and TIFF images to JPG format")
    parser.add_argument("--input-dir", "-i", type=str, default="/data", help="Input directory containing images (default: /data)")
    parser.add_argument("--output-dir", "-o", type=str, default="/output", help="Output directory for converted images (default: /output)")

    args = parser.parse_args()

    if not Path(args.input_dir).exists():
        print(f"Directory {args.input_dir} does not exist!")
        exit(-1)

    # Check if output directory exists, if not create it
    output_dir_path = Path(args.output_dir)
    output_dir_path.mkdir(parents=True, exist_ok=True)

    convert_images(args.input_dir, args.output_dir)
