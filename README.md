# UnderWaterImageRectificationAndEnhancement
This project provides a solution for restoring underwater images by improving color balance, contrast, and overall visibility. It applies a series of image processing techniques such as color balancing, contrast enhancement, red channel optimization, and novel rectifier algorithms to enhance underwater images that may have color distortions, blurriness, or low contrast.

## Table of Contents
- [Project Description](#project-description)
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Functions](#functions)


## Project Description

The goal of this project is to restore underwater images using a combination of image enhancement techniques:

- **Color Balance**: Correcting the color distortions typical in underwater images.
- **Contrast Optimization**: Enhancing contrast using the CLAHE algorithm to make the image more vibrant and clear.
- **Red channel optimization**: Enhances the red channel to restore the natural vibrancy of the image, which is often subdued underwater.
- **Novel rectifier Algorithm**: Combining the original and enhanced images to obtain a final restored result.

The process works by sequentially applying the techniques mentioned above to an image, improving its quality and readability.

## Features

- Enhances underwater images by restoring natural colors and improving contrast.
- Processes images in bulk from a directory.
- Saves the restored images to an output directory.
- Visualization of the restoration process with intermediate steps.
  
## Requirements

- Python 3.x
- OpenCV (for image processing)
- NumPy (for numerical operations)
- Matplotlib (for visualization)
  
You can install the required dependencies using `pip`:

```bash
pip install opencv-python numpy matplotlib
```

## Setup

1. Clone or download this repository.
2. Make sure you have Python 3.x installed on your system.
3. Install the necessary libraries by running:

```bash
pip install -r requirements.txt
```

4. Prepare an input directory with underwater images (JPEG, PNG, BMP, etc.).
5. Specify an output directory where the processed images will be saved.

## Usage

### Image Restoration for Single Image:

You can restore a single image by calling the `underwater_image_restoration` function.

Example:

```python
restored_img = underwater_image_restoration('path_to_image.jpg')
```

### Process All Images in a Directory:

To process all images in a directory and save them to a separate directory, use the `process_directory` function.

```python
input_directory = "path_to_input_directory"
output_directory = "path_to_output_directory"
process_directory(input_directory, output_directory)
```

This will process all images in the input directory and save the restored images in the specified output directory.

## Functions

### `underwater_image_rectification(image_path)`
Restores the underwater image at the specified `image_path`. It applies color balancing, contrast enhancement, histogram stretching, and fusion algorithms to restore the image.

#### Parameters:
- `image_path`: Path to the input image file.

#### Returns:
- The restored image as a NumPy array.

### `balancing_color(img, percent=1)`
Applies color balancing by clipping pixel values at given percentiles.

#### Parameters:
- `img`: The input image as a NumPy array.
- `percent`: Percentile for clipping (default: 1%).

#### Returns:
- The color-balanced image.

### `contrast_enhancement(img)`
Enhances the contrast of the image using the CLAHE (Contrast Limited Adaptive Histogram Equalization) algorithm.

#### Parameters:
- `img`: The input image as a NumPy array.

#### Returns:
- The contrast-enhanced image.

### `red_channel_optimization(img)`
Applies histogram stretching to improve image intensity distribution.

#### Parameters:
- `img`: The input image as a NumPy array.

#### Returns:
- The histogram-stretched image.

### `novel_rectifier(original_img, enhanced_img)`
Fuses the original image and the enhanced image using weighted fusion to create the final restored image.

#### Parameters:
- `original_img`: The original image.
- `enhanced_img`: The enhanced image.

#### Returns:
- The final fused image.

### `process_directory(input_dir, output_dir)`
Processes all images in the specified input directory and saves the restored images to the output directory.

#### Parameters:
- `input_dir`: Path to the input directory containing image files.
- `output_dir`: Path to the output directory where the restored images will be saved.



