# image2jpg

This repository contains a script that converts HEIC, PNG, and TIFF images to JPG format using multiprocessing for efficient processing. It provides options for specifying input and output directories.

## ⚙️ Prerequisites

- Python 3.x
- OpenCV (cv2)
- pillow_heif
- numpy
- tqdm

You can install the required dependencies using pip:

```bash
pip install opencv-python-headless pillow_heif numpy tqdm
```

Or you can use the `requirements.txt` file included in the repository:
```bash
pip install -r requirements.txt
```

## 🚀 Getting Started Locally

1. Clone this repository or download the `conv
ert_images.py` script.

2. Ensure you have the necessary input images in a directory. The script supports HEIC, PNG, and TIFF image formats.

3. Run the script with the desired input and output directories:

    ```bash
    python convert_images.py --input-dir /path/to/input --output-dir /path/to/output
    ```

    - `--input-dir` (or `-i`): Specifies the input directory containing the images to be converted (default: `/data`).
    - `--output-dir` (or `-o`): Specifies the output directory where the converted JPG images will be saved (default: `/output`).

4. The script will convert the images in parallel and save the resulting JPG images in the specified output directory.

## 🚀 Getting Started in a Container

### 🛠️ Building from Scratch

1. Clone this repository.

2. Build the container image: 
    ```
    docker build -t image2jpg:latest .
    ```

This will create an image `image2jpg` in your local container repository for your use.

### ⬇️ Pulling the Image

Pull the container image by doing:
```
docker pull ghcr.io/xaviermerino/image2jpg:latest
docker tag ghcr.io/xaviermerino/image2jpg:latest image2jpg:latest
```

### 🏃 Running the Container

You may then run the container by doing:
```bash
docker run \
-v /path/to/input:/data \
-v /path/to/output:/output \
image2jpg:latest -i /data -o /output
```

- `-v /path/to/input:/data` specifies the directory with images and its location once mounted in the container.
- `-v /path/to/output:/output` specifies the directory where the converted images will be stored in and its location once mounted in the container. 
- `--input-dir` (or `-i`): Specifies the input directory containing the images to be converted (default: `/data`).
- `--output-dir` (or `-o`): Specifies the output directory where the converted JPG images will be saved (default: `/output`).

4. The script will convert the images in parallel and save the resulting JPG images in the specified output directory.

## 📄 File Formats Supported

The script can convert the following image formats to JPG:
- HEIC (High-Efficiency Image File Format)
- PNG (Portable Network Graphics)
- TIFF (Tagged Image File Format)

