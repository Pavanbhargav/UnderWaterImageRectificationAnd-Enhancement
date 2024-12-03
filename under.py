import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

def underwater_image_rectification(image_path):
    # Step 1: Read the image from the path
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Image at path {image_path} could not be loaded.")
    
    # Clip the pixel values to ensure they are between 0 and 255
    img = np.clip(img, 0, 255).astype(np.uint8)

    # Convert the image from BGR to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Step 1: Apply Color Balance
    balanced_img = balancing_color(img)

    # Step 2: Contrast Optimization
    contrast_img = contrast_enhancement(balanced_img)

    # Step 3: Histogram Stretching
    stretched_img = red_channel_optimization(contrast_img)

    # Step 4: Fusion Algorithm (combines the original image with the stretched image)
    final_img = novel_rectifier(img, stretched_img)

    return final_img


def balancing_color(img, percent=1):
    """
    Perform color balancing by clipping pixel values at given percentages.
    """
    channels = cv2.split(img)
    out_channels = []
    for channel in channels:
        # Calculate percentiles
        lower_bound = np.percentile(channel, percent)
        upper_bound = np.percentile(channel, 100 - percent)

        # Clip and normalize channel
        channel = np.clip(channel, lower_bound, upper_bound)
        channel = cv2.normalize(channel, None, 0, 255, cv2.NORM_MINMAX)
        out_channels.append(channel)

    return cv2.merge(out_channels)


def contrast_enhancement(img):
    """
    Enhance contrast using CLAHE.
    """
    img = np.clip(img, 0, 255).astype(np.uint8)
    lab = cv2.cvtColor(img, cv2.COLOR_RGB2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    l = clahe.apply(l)
    enhanced_img = cv2.merge((l, a, b))
    return cv2.cvtColor(enhanced_img, cv2.COLOR_LAB2RGB)


def red_channel_optimization(img):
    """
    Optimize the red channel to enhance the red tones in underwater images.
    """
    # Split the image into channels
    r, g, b = cv2.split(img)

    # Apply a scaling factor to the red channel to enhance the red tones
    scale_factor = 1.3  # This factor can be adjusted to fine-tune the enhancement
    r = np.clip(r * scale_factor, 0, 255).astype(np.uint8)

    # Merge the channels back together
    return cv2.merge((r, g, b))


def novel_rectifier(original_img, enhanced_img):
    """
    Fuse the original and enhanced images for a final result.
    """
    # Convert to float32 for blending
    original_img = original_img.astype(np.float32)
    enhanced_img = enhanced_img.astype(np.float32)

    # Fusion weights
    weight_original = 0.4
    weight_enhanced = 0.6

    # Perform weighted fusion
    fused_img = cv2.addWeighted(original_img, weight_original, enhanced_img, weight_enhanced, 0)

    # Convert back to uint8
    return fused_img.astype(np.uint8)


# Process all images in the input directory and save the restored images
def process_directory(input_dir, output_dir):
    """
    Process all image files in the input directory and save results to the output directory.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate through all files in the input directory
    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        
        # Check if the file is an image
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            try:
                # Perform restoration
                restored_img = underwater_image_rectification(input_path)

                # Save the restored image
                output_path = os.path.join(output_dir, filename)
                cv2.imwrite(output_path, cv2.cvtColor(restored_img, cv2.COLOR_RGB2BGR))
                print(f"Processed and saved: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Define input and output directories
input_directory = "/Users/pavanbhargav/Documents/Data_Science_and_AI/PROJECT/under_water/Train/Raw"
output_directory = "/Users/pavanbhargav/Documents/Data_Science_and_AI/PROJECT/under_water/enchanced2_images"

# Process all images
process_directory(input_directory, output_directory)
