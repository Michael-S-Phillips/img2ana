import numpy as np
from osgeo import gdal
from tkinter import filedialog
from PIL import Image
from scipy import ndimage


def create_anaglyph(left_cube_path, right_cube_path, output_path, angle):
    """
    Function to create an anaglyph image from left and right ISIS cube images.
    
    Arguments:
    - left_cube_path: path to the left ISIS cube image
    - right_cube_path: path to the right ISIS cube image
    - output_path: path to save the anaglyph image, must include a .png or .jpg file extension
    - angle: amount of rotation in degrees
    
    Returns:
    None
    """
    # Open left and right ISIS cube images
    left_image = gdal.Open(left_cube_path)
    right_image = gdal.Open(right_cube_path)

    print(type(left_image))

    # Read image data as NumPy arrays
    left_data = left_image.GetRasterBand(1).ReadAsArray()
    right_data = right_image.GetRasterBand(1).ReadAsArray()

    rows, cols = left_data.shape
    bands = 3
    anaglyph_shape = (rows, cols, bands)

    # Calculate the anaglyph image (red-cyan)
    anaglyph = np.zeros(anaglyph_shape)

    # Assign red channel to the left image data and green/blue channels to the right image data
    anaglyph[:, :, 0] = left_data
    anaglyph[:, :, 1] = right_data
    anaglyph[:, :, 2] = right_data

    # Normalize the values and convert to 8-bit unsigned integer
    anaglyph = 255 * (anaglyph / np.max(anaglyph))
    anaglyph = anaglyph.astype(np.uint8)

    # Rotate the anaglyph image
    anaglyph = rotate_array(anaglyph, angle)

    # Convert the NumPy array to a Pillow Image
    anaglyph_image = Image.fromarray(anaglyph)

    # Save the anaglyph image as a PNG file
    anaglyph_image.save(output_path)

def rotate_array(array, angle_degrees):
    """
    Function to rotate an array clockwise by a given angle.
    
    Arguments:
    - array: input array to be rotated
    - angle_degrees: amount of rotation in degrees
    
    Returns:
    - rotated_array: the input array after rotation
    """
    # Convert angle from degrees to radians
    angle_radians = np.deg2rad(angle_degrees)
    
    # Rotate the array clockwise
    rotated_array = ndimage.rotate(array, -np.degrees(angle_radians), reshape=False)
    
    return rotated_array

if __name__ == '__main__':
    # Ask user to provide the paths for left and right images, and output file
    left_cube_path = filedialog.askopenfilename(title="Select left image")
    right_cube_path = filedialog.askopenfilename(title="Select right image")
    output_path = filedialog.asksaveasfilename(title="Select the name to save file as, make sure to include file extension in the name (.png, .jpg, etc)")
    
    # Ask user for the rotation angle
    angle = input("Enter amount of rotation in degrees (0-360):\n")
    angle = float(angle)

    # Call the create_anaglyph function with the provided arguments
    create_anaglyph(left_cube_path, right_cube_path, output_path, angle=angle)
